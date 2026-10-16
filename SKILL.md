---
name: quote-with-provenance
description: "Quotes and shortens sources by Wikipedia's rules, e.g. `ordered him [at once] to ... bare his shoulders`, and keeps each cut or replaced word (forthwith; take off his shirt and) in an HTML comment. Use when quoting, excerpting or shortening a source so a reader can check what changed."
license: MIT
---

# quote-with-provenance

Readers see a normal quotation. The raw Markdown also holds the source and, for every edit, the words it replaced.

## Quote

Follow [Wikipedia's quotation rules](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Quotations):

- Keep the source's words in order.
- `...` marks a cut inside the quote. Never join two pieces without it.
- `[brackets]` mark every word you add or change: a name for a pronoun, a plainer word for an archaic one, a grammar fix.
- Fix small spelling and scan errors without a visible mark. Keep a real error and add `[sic]`.
- Quote a translation in the translator's words, and name the translator.

Edits must not change the meaning. Do not cut a "not", a condition, or who did what to whom. Do not add a fact, motive or verdict the source does not state. Do not swap a relationship or status (slave, father) for another. If the result no longer says what the source says, it is a paraphrase: present it outside quotation marks.

## Record

Put one source comment on its own line before the quote. Use `null` for anything unknown; never guess a URL or edition.

```md
<!--{"type":"quotation","source_url":"...","author":"...","work":"...","translator":"...","locator":"p. 285","editor":"agent/model"}-->
```

Put an edit comment directly after each change, on the same line:

| op | goes after | fields |
|:--|:--|:--|
| `omit` | the `...` | `original`: the exact cut text |
| `replace` | the new text | `original`, `rendered` (new text with its brackets), `reason` |
| `insert` | the added text | `original: ""`, `rendered`, `reason` |

Copy `original` exactly from the source, errors included. Record unmarked fixes too. Comments are JSON; if a string contains `--`, `<` or `>`, write them as `\u002d`, `\u003c`, `\u003e` so the text cannot close the comment.

Below the quote, add a visible citation: author, work, translator, locator, link.

## Example

Original ([Seneca, *On Anger* III.12, trans. John W. Basore, p. 285](https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html)):

> Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. Later, when a friend who happened to come in asked him what he was doing, he said, "I am exacting punishment from an angry man."

Quote with metadata:

```txt
<!--{"type":"quotation","source_url":"https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html","author":"Seneca","work":"Moral Essays, Volume I, On Anger","translator":"John W. Basore","edition":"Loeb Classical Library, 1928–1935","locator":"On Anger III.12, p. 285","editor":"PI/Claude"}-->

> Plato once, when he was angry with his slave, ...<!--{"type":"edit","op":"omit","original":"was unable to impose delay upon himself, and,"}--> bent upon flogging him with his own hand, ordered him [at once]<!--{"type":"edit","op":"replace","original":"forthwith","rendered":"[at once]","reason":"Archaic word."}--> to ...<!--{"type":"edit","op":"omit","original":"take off his shirt and"}--> bare his shoulders for the blows; but ...<!--{"type":"edit","op":"omit","original":"afterwards"}--> realizing that he was angry he [held back]<!--{"type":"edit","op":"replace","original":"stayed","rendered":"[held back]","reason":"'stayed' in this sense is unfamiliar."}--> his uplifted hand, and ...<!--{"type":"edit","op":"omit","original":"just as he was"}--> stood with his hand<!--{"type":"edit","op":"replace","original":"band","rendered":"hand","reason":"Scan error; Wikipedia fixes small typos without marking them."}--> in the air like one in the act of striking. Later, when a friend ...<!--{"type":"edit","op":"omit","original":"who happened to come in"}--> asked him what he was doing, [Plato]<!--{"type":"edit","op":"replace","original":"he","rendered":"[Plato]","reason":"'he' could be read as the friend."}--> said, "I am [punishing]<!--{"type":"edit","op":"replace","original":"exacting punishment from","rendered":"[punishing]","reason":"Shorter, plainer wording."}--> an angry man."

Seneca, *On Anger* III.12, trans. John W. Basore, p. 285.
```

Quote rendered:

```md
> Plato once, when he was angry with his slave, ... bent upon flogging him with his own hand, ordered him [at once] to ... bare his shoulders for the blows; but ... realizing that he was angry he [held back] his uplifted hand, and ... stood with his hand in the air like one in the act of striking. Later, when a friend ... asked him what he was doing, [Plato] said, "I am [punishing] an angry man."

Seneca, *On Anger* III.12, trans. John W. Basore, p. 285.
```

## Check

- Undo every edit using its `original`: you get back the exact source passage.
- Delete the comments: the quote still reads correctly.
- Read the quote alone: it still says what the source says.
