---
name: quote-with-provenance
description: "Makes quotations easy to parse and understand for a new reader without the surrounding document, while preserving the source's meaning as faithfully as possible. Records exact originals for edited passages. Use when quoting, excerpting, simplifying sources, or verifying claims with quoted evidence."
license: MIT
---

# quote-with-provenance

Make the selected passage easy to parse and understand for a new reader who has not read the surrounding document. Preserve the source's meaning as faithfully as possible; keep the context and qualifications needed to avoid misleading the reader.

The reader sees a selection and simplification, which can lose information. When wording is edited, preserve the exact original passage so an auditor can recover what changed. The complete record is lossless with respect to that stored passage, not the whole source document. Recoverability does not excuse a misleading visible quotation.

<!-- PI/OpenAI: reader understanding is the goal; recoverable originals support the audit. -->

## Select and present

- Use the source's words rather than replacing the evidence with editorial. Select, shorten, or clarify them when that helps the reader understand. Keep the full paragraph when it is needed; do not impose a one-sentence cap or reproduce whole works.
- Include the surrounding source context needed to preserve the meaning; a sentence before and after is often useful, not a quota. For repeated judge inputs, select the useful teaching rather than copying entire paragraphs by rule. Never invent missing context.
- **Bold the main sentence** inside the quote. Bold is emphasis added by the editor, not a change to the source's words.
- Use more quotation than editorial. Usually one plain sentence before and one after is enough. Put our explanations, interpretations, and opinions outside the quote, attributed to us rather than the author. Such commentary can be useful; keep the reader able to distinguish it from the author's view.
- Cite the author, title, link or location, and visible date (or "not stated"). For books and papers, include a page or section when available and name the translator.
- Identify whose words they are: distinguish an author's text from a translator's note, editor's commentary, or nested quotation. Attribute “I” and preserve uncertainty about translation choices. Add a short source-context note only when it affects interpretation.

For claim verification, also read [references/claim-verification.md](references/claim-verification.md). Ordinary quotation does not need a verification report.

<!-- PI/OpenAI: generous quotation and minimal editorial, from wassname's varglight preference. -->

## Reduce reader burden

Optimize for the new reader's understanding, not word count or number of edits. The quotation and any clearly separated explanation should make sense without the surrounding document or hidden original. Retain needed source context; put additional background or interpretation outside the quote. A shorter quote is not automatically better.

- Cut repetition and detours while retaining who did what, negations, conditions, and qualifications. Keep enough visible context to understand the point without opening the original.
- Use small bracketed clarifications for equivalent wording or referents clearly established by the source. If a clarification adds a claim, interpretation, or background explanation, put it outside the quote and identify whose explanation it is.
- Read the edited quote on its own: does it take less effort to understand, and does it still say what the source says? Undo cuts that leave fragments or make the reader reconstruct the argument. Check that retained references and images still have a clear referent or explanation in the visible quote, not only in a heading, editorial, or hidden original. Restore needed context, add a small source-supported bracketed clarification, or omit the dependent wording too.
- Reconstruct paragraphs and sentences across scan or page breaks before selecting a passage; separate running text from headers and notes. Do not present a broken sentence as two independent quotations.
- Leave clear wording unchanged. Do not add substitutions to demonstrate activity, turn unfamiliar ideas into familiar but different ones, or rewrite the whole passage inside brackets.

<!-- PI/OpenAI: useful compression and clarification, not merely fewer words or more edit marks. -->

Follow [Wikipedia's quotation rules](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Quotations):

- Keep the source's words in order.
- `...` marks a cut inside the quote. Never join two pieces without it.
- `[brackets]` mark every word you add or change: a name for a pronoun, a plainer word for an archaic one, a grammar fix.
- Clean presentation by default: collapse repeated spaces, reflow scan-wrapped prose, join words split by line-end hyphens, remove spaces inside quotation marks or before punctuation, and repair clear scan-punctuation artifacts. Remove clearly identified citation/footnote markers, not meaningful numbers. These changes need no brackets, ellipses, cleanup disclaimer, or duplicate original. Preserve meaningful layout (verse, code), punctuation under discussion, and uncertain readings.
- Fix small spelling and scan errors without a visible mark; record textual corrections below. Keep a real author error and add `[sic]`.
- Quote a translation in the translator's words, and name the translator. Preserve genuine archaic wording; explain it outside the quote or mark a substitution with brackets.

[Wikipedia's typographic-conformity guidance](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Typographic_conformity) says: “A quotation is not a facsimile” and permits purely typographical adaptations “without comment”, provided they do not change or obscure meaning or intent. The cleanup rule above applies that distinction to scanned sources.

<!-- PI/OpenAI: explicit default cleanup, separate from textual editing and translation. -->

Edits must not change the meaning. Do not cut a "not", a condition, or who did what to whom. Do not add a fact, motive or verdict the source does not state. Do not swap a relationship or status (slave, father) for another. If you rewrite a passage in your own words, present it outside quotation marks as a cited paraphrase. A paraphrase must still preserve the source's meaning.

## Record

For an unchanged, contiguous passage with a visible citation, do not duplicate the original in a JSON comment. Bold emphasis and the presentation cleanup above do not count as textual edits. The source citation is still required; a separate citation for cleanup is not. Choosing where a passage starts and ends is ordinary quotation; retain enough visible context to preserve its meaning. If an edited passage's exact original is already retained in a source record, reference it rather than making another copy.

If you cut within the passage, shorten a sentence at either end, add or replace words, or correct a typo, preserve the exact original. For standalone Markdown, use a JSON comment before the quote. For model prompts and other repeated inputs, keep that record in a separate source file linked by the build; do not send HTML comments, local paths, audit IDs, agent signatures or generic epistemic-status notes to the judge. Keep a short useful citation and clearly separate quotations from explanation.

A short explanation outside the quotation is allowed when source context or bracketed clarification cannot make the teaching clear. Explain the missing context, not our review process. Formatting cleanup does not require a disclaimer on every quote.

<!-- PI/Sol: preserve audit records separately from repeated judge teaching; normalize OCR without changing meaning. -->

```md
<!--
{"uri":"https://...",
"original":"the exact passage",
"fixed":{"band":"hand"}}
-->
```

- `original`: the passage copied exactly, errors included. The quoted span plus enough around it to show context, not the whole page.
- `fixed`: typos corrected without a visible mark, as `{"source spelling": "fixed spelling"}`. Leave it out if there are none.
- `uri`: where to find the original, e.g. `https://...`, `file:///path/book.pdf`, `doi:10.1000/xyz`, `urn:isbn:9780674992566`, `magnet:?xt=...`. Leave it out if there is none (an email, a conversation).
- `bibtex`: optional, for papers and books. One JSON string, `\n` for newlines; page ranges like `285--287` need the escape below.
- If a string contains `--`, `<` or `>`, write them as `\u002d`, `\u003c`, `\u003e` so the text cannot close the comment.

Below the quote, add the visible citation. The hidden record does not replace it. For presentation-only changes, compare the source and quote after the same cleanup rather than demanding a raw-string match. For wording edits, the exact `original` is the searchable passage.

<!-- PI/OpenAI: distinguish source wording from marked edits without losing provenance. -->

## Example: edited quotation

Original ([Seneca, *On Anger* III.12, trans. John W. Basore, p. 285](https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html)):

> Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. Later, when a friend who happened to come in asked him what he was doing, he said, "I am exacting punishment from an angry man."

Quote with metadata:

```md
<!--
{"uri":"https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html",
"original":"Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. Later, when a friend who happened to come in asked him what he was doing, he said, \"I am exacting punishment from an angry man.\"",
"fixed":{"band":"hand"}}
-->

> Plato once, when he was angry with his slave, ... bent upon flogging him with his own hand, ordered him [at once] to ... bare his shoulders for the blows;
> but ... realizing that he was angry he [held back] his uplifted hand, and ... stood with his hand in the air like one in the act of striking.
> Later, when a friend ... asked him what he was doing, [Plato] said, "I am [punishing] an angry man."

Seneca, *On Anger* III.12, trans. John W. Basore, p. 285.
```

Quote rendered:

> Plato once, when he was angry with his slave, ... bent upon flogging him with his own hand, ordered him [at once] to ... bare his shoulders for the blows;
> but ... realizing that he was angry he [held back] his uplifted hand, and ... stood with his hand in the air like one in the act of striking.
> Later, when a friend ... asked him what he was doing, [Plato] said, "I am [punishing] an angry man."

Seneca, *On Anger* III.12, trans. John W. Basore, p. 285.

## Check

- For unchanged quotes, check the quoted passage directly against the cited source.
- For edited quotes, every word outside `[brackets]` appears in `original`, in order, after applying `fixed`.
- If there is a record, delete the comment: the quote still reads correctly.
- Read the quote alone: it still says what the source says, with the conditions and surrounding context intact.

For a saved Markdown file, run `uv run scripts/check_quote.py /path/to/notes.md` from this skill's directory. This checks recorded quotes against `original` (and a readable local `uri`); unrecorded quotes are not checked. It does not decide whether cuts or bracketed changes preserve meaning; review those yourself.

When changing the cleanup rules, use the real scanned passages in `tests/ocr_cleanup.md` for a fresh-model behavior test. Run `uv run python -m unittest discover -s tests -v` for the maintained checker regressions.

<!-- PI/OpenAI: route the existing checker and state its limits. -->
