"""Check quotes written with this skill: every word outside the editor's [brackets] appears in `original`, in order, after `fixed`;
and, when `uri` is a local file, `original` appears in that file.

Reads a Markdown file of <!-- {json} --> comments each followed by a > quote. Prints one line per quote and exits 1 if any fails.
    python3 check_quote.py notes.md
    python3 check_quote.py notes.md --json      # machine-readable results

Comparison ignores case, curly vs straight quote marks, whitespace, markdown * and _, and words split by a scan line-break
hyphen ("impossi- ble"). A bracket that appears in `original` itself (translators bracket supplied words too) is treated
as quoted text; the others are listed as editor insertions. Tested on 5,961 quotes from scanned and modern translations
(tiny-virtues), where a separate word-token check agreed on every one.   -- PI/Claude Opus 5.5
"""
import json
import re
import unicodedata
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

BRACKET = re.compile(r'\[[^\[\]]*\]')
ELLIPSIS = re.compile(r'\.\.\.|…')


def apply_fixed(original, fixed):
    """Apply `fixed` ({"source spelling": "fixed spelling"}) to whole words only: "an" -> "and" must not turn "another" into "andother"."""
    for bad, good in (fixed or {}).items():
        original = re.sub(_fixed_pattern(bad), lambda m: good, original)
    return original


def _fixed_pattern(bad):
    body = r'\s+'.join(re.escape(w) for w in bad.split())  # a scan may break the misspelt words across lines
    return (r'(?<!\w)' if bad[:1].isalnum() else '') + body + (r'(?!\w)' if bad[-1:].isalnum() else '')


NUMBER = re.compile(r'[(\[]?\b\d{1,4}\b[)\]]?')


def _drop_numbers(s):
    """Footnote, verse and page numbers ("114", "(1150)", "[452]") may be dropped silently; the quote's own numbers are checked separately."""
    return NUMBER.sub(' ', VERSE.sub(' ', s)) if 'VERSE' in globals() else NUMBER.sub(' ', re.sub(r'(?<![\w:])\d{1,3}:\d{1,3}(?![\w:])', ' ', s))  # verse markers ("8:2") first, or a stray ":" is left


def norm(s):
    s = unicodedata.normalize('NFKC', s)  # full-width OCR punctuation ('；') and ligatures
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('*', '').replace('_', '').replace('\\', '')
    s = re.sub(r'(\w)-\s+(\w)', r'\1\2', s)
    s = re.sub(r'\s*(["\'])\s*', r'\1', s)  # scans space quote marks unevenly: '" it is just,"'
    s = re.sub(r'\s+([,.;:!?)\]])', r'\1', s)  # scan line-break hyphen
    return re.sub(r'\s+', ' ', s).strip().lower()


def editor_insertions(quote, original):
    src = norm(original)
    return [b for b in BRACKET.findall(quote) if norm(b) not in src]


def _pieces(quote, keep):
    q = re.sub(r'\[(\w)\](?=\w)', r'\1', quote)  # [T]he -> The
    q = BRACKET.sub(lambda m: m.group() if m.group() in keep else ' … ', q)
    return [p for p in (x.strip(' ,;:"\'.-—') for x in ELLIPSIS.split(norm(q))) if any(c.isalnum() for c in p)]



def _words(s):
    return re.findall(r'[a-z0-9]+', s)


def _find(hay, needle, start):
    """First index >= start where the token list `needle` occurs contiguously in `hay`, else -1."""
    n = len(needle)
    for i in range(start, len(hay) - n + 1):
        if hay[i:i + n] == needle:
            return i
    return -1

def problems(quote, original, fixed=None, max_insertion_share=0.3):
    out, src = [], original
    for bad in (fixed or {}):
        if not re.search(_fixed_pattern(bad), src):
            return [f'fixed: "{bad}" is not in the original']
    src = apply_fixed(src, fixed)
    missing_numbers = [n for n in re.findall(r'\b\d{1,4}\b', BRACKET.sub(' ', quote)) if not re.search(rf'\b{n}\b', src)]
    if missing_numbers:
        return [f'numbers not in the original: {missing_numbers}']
    quote, src = _drop_numbers(quote), _drop_numbers(src)
    srcn, own = norm(src), set(BRACKET.findall(quote)) - set(editor_insertions(quote, src))
    src_toks = _words(srcn)
    for keep in (own, ()):  # brackets found in the original as text; if that fails, every bracket as the editor's
        out, pos, ps = [], 0, _pieces(quote, keep)
        for p in ps:  # word tokens: OCR noise in punctuation ("travesty^", "justin?", ".'.'") is not a change of words
            toks = _words(p)
            hit = _find(src_toks, toks, pos)
            if hit < 0:
                out.append(f'not verbatim or out of order: "{p}"' + (' (occurs earlier in the original)' if _find(src_toks, toks, 0) >= 0 else ''))
            else:
                pos = hit + len(toks)
        if not out:
            break
    if not ps:
        out.append('no quoted text outside brackets')
    added = sum(len(b.split()) for b in editor_insertions(quote, src))
    if added > max_insertion_share * max(1, len(BRACKET.sub(' ', quote).split()) + added):
        out.append(f'{added} words in editor brackets: too much of the quote is not the source')
    if re.search(r'[\[\]]', BRACKET.sub('', quote)):
        out.append('unbalanced bracket')
    return out


def _dictionary():
    p = Path('/usr/share/dict/words')
    return {w.strip().lower() for w in p.read_text(errors='ignore').splitlines() if len(w.strip()) > 2} if p.exists() else set()


def word_swaps(fixed):
    """`fixed` pairs that turn one dictionary word into another ("shirt" -> "coat"): maybe a scan error ("had" -> "bad"), maybe a change
    of meaning. Code cannot tell; a reader checks these against the original."""
    words = _dictionary()
    out = []
    for bad, good in (fixed or {}).items():
        a, b = re.findall(r'[a-z]+', bad.lower()), re.findall(r'[a-z]+', good.lower())
        if a and b and ''.join(a) != ''.join(b) and all(w in words for w in a + b):
            out.append(f'{bad} -> {good}')
    return out


def original_in_file(original, uri):
    """None if uri is not a readable local file, else whether `original` occurs in it."""
    u = urlparse(uri or '')
    path = Path(unquote(u.path)) if u.scheme == 'file' else Path(uri) if uri and Path(uri).exists() else None
    if path is None or not path.is_file():
        return None
    return norm(original).rstrip('-') in norm(path.read_text(errors='ignore'))


def blocks(markdown):
    """(record, quote) pairs: a <!-- {json} --> comment, then the > lines after it."""
    for m in re.finditer(r'<!--\s*(\{.*?\})\s*-->\s*\n((?:\s*\n)*)((?:>[^\n]*\n?)+)', markdown, re.S):
        quote = ' '.join(re.sub(r'^>\s?', '', l) for l in m.group(3).splitlines())
        yield json.loads(m.group(1)), quote.strip()


if __name__ == '__main__':
    text = Path(sys.argv[1]).read_text()
    results = []
    for rec, quote in blocks(text):
        probs = problems(quote, rec['original'], rec.get('fixed'))
        in_file = original_in_file(rec['original'], rec.get('uri'))
        if in_file is False:
            probs.append('original not found in the uri file')
        results.append(dict(quote=quote[:60], ok=not probs, problems=probs, editor_insertions=editor_insertions(quote, rec['original']),
                            check_by_eye=word_swaps(rec.get('fixed')), original_checked_in_file=in_file))
    if '--json' in sys.argv:
        print(json.dumps(results, ensure_ascii=False, indent=1))
    else:
        for r in results:
            print(('ok  ' if r['ok'] else 'FAIL') + f" {r['quote']!r} insertions={r['editor_insertions']}" + ''.join(f'\n     {p}' for p in r['problems'])
                  + ''.join(f'\n     check by eye, fixed changed a real word: {w}' for w in r['check_by_eye']))
    sys.exit(0 if results and all(r['ok'] for r in results) else 1)
