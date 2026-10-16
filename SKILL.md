---
name: quote-with-provenance
description: "Quotes and shortens sources by Wikipedia's rules, e.g. `ordered him [at once] to ... bare his shoulders`, and keeps the exact original passage in an HTML comment so a reader can see every cut and change. Use when quoting, excerpting or shortening a source so a reader can check what changed."
license: MIT
---

# quote-with-provenance

Readers see a normal quotation. The raw Markdown also holds the source and the exact original passage, so anyone can compare the two and judge whether each edit is fair.

## Quote

Follow [Wikipedia's quotation rules](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Quotations):

- Keep the source's words in order.
- `...` marks a cut inside the quote. Never join two pieces without it.
- `[brackets]` mark every word you add or change: a name for a pronoun, a plainer word for an archaic one, a grammar fix.
- Fix small spelling and scan errors without a visible mark. Keep a real error and add `[sic]`.
- Quote a translation in the translator's words, and name the translator.

Edits must not change the meaning. Do not cut a "not", a condition, or who did what to whom. Do not add a fact, motive or verdict the source does not state. Do not swap a relationship or status (slave, father) for another. If the result no longer says what the source says, it is a paraphrase: present it outside quotation marks.

## Record

Put one JSON comment before the quote, with a blank line between them:

```md
<!--
{"url":"https://...",
"original":"the exact passage",
"fixed":{"band":"hand"}}
-->
```

- `original`: the passage copied exactly, errors included. The quoted span plus enough around it to show context, not the whole page.
- `fixed`: typos corrected without a visible mark, as `{"source spelling": "fixed spelling"}`. Leave it out if there are none.
- `url`: leave it out if the source has none (an email, a printed book).
- If a string contains `--`, `<` or `>`, write them as `\u002d`, `\u003c`, `\u003e` so the text cannot close the comment.

Below the quote, add a visible citation in whatever form suits the source: author, work, translator, page; site and date; sender and date.

## Example

Original ([Seneca, *On Anger* III.12, trans. John W. Basore, p. 285](https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html)):

> Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. Later, when a friend who happened to come in asked him what he was doing, he said, "I am exacting punishment from an angry man."

Quote with metadata:

```md
<!--
{"url":"https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html",
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

- Every word outside `[brackets]` appears in `original`, in order, after applying `fixed`.
- Delete the comment: the quote still reads correctly.
- Read the quote alone: it still says what the source says.
