# quote-with-provenance

An agent skill for quoting sources faithfully in Markdown. Quotes follow [Wikipedia's quotation rules](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Quotations): `...` for cuts, `[brackets]` for the editor's words, small typos fixed. Each edit also gets an HTML comment holding the source's exact words, so the raw file shows what changed and the rendered page does not.

## Example

Original ([Seneca, *On Anger* III.12, trans. John W. Basore, p. 285](https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html)):

> Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. Later, when a friend who happened to come in asked him what he was doing, he said, "I am exacting punishment from an angry man."

Quote with metadata:

```txt
<!--{"type":"quotation","style":"wikipedia","source_url":"https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html","author":"Seneca","work":"Moral Essays, Volume I, On Anger","translator":"John W. Basore","edition":"Loeb Classical Library, 1928–1935","locator":"On Anger III.12, p. 285","editor":"PI/Claude"}-->

> Plato once, when he was angry with his slave, ...<!--{"type":"edit","op":"omit","original":"was unable to impose delay upon himself, and,"}--> bent upon flogging him with his own hand, ordered him [at once]<!--{"type":"edit","op":"replace","original":"forthwith","rendered":"[at once]","reason":"Archaic word."}--> to ...<!--{"type":"edit","op":"omit","original":"take off his shirt and"}--> bare his shoulders for the blows; but ...<!--{"type":"edit","op":"omit","original":"afterwards"}--> realizing that he was angry he [held back]<!--{"type":"edit","op":"replace","original":"stayed","rendered":"[held back]","reason":"'stayed' in this sense is unfamiliar."}--> his uplifted hand, and ...<!--{"type":"edit","op":"omit","original":"just as he was"}--> stood with his hand<!--{"type":"edit","op":"replace","original":"band","rendered":"hand","reason":"Scan error; Wikipedia fixes small typos without marking them."}--> in the air like one in the act of striking. Later, when a friend ...<!--{"type":"edit","op":"omit","original":"who happened to come in"}--> asked him what he was doing, [Plato]<!--{"type":"edit","op":"replace","original":"he","rendered":"[Plato]","reason":"'he' could be read as the friend."}--> said, "I am [punishing]<!--{"type":"edit","op":"replace","original":"exacting punishment from","rendered":"[punishing]","reason":"Shorter, plainer wording."}--> an angry man."

Seneca, *On Anger* III.12, trans. John W. Basore, p. 285.
```

Quote rendered:

```md
> Plato once, when he was angry with his slave, ... bent upon flogging him with his own hand, ordered him [at once] to ... bare his shoulders for the blows; but ... realizing that he was angry he [held back] his uplifted hand, and ... stood with his hand in the air like one in the act of striking. Later, when a friend ... asked him what he was doing, [Plato] said, "I am [punishing] an angry man."

Seneca, *On Anger* III.12, trans. John W. Basore, p. 285.
```

The reader sees cuts and bracketed substitutions. The comments keep every removed or replaced word, including the scan error `band` → `hand`, which Wikipedia allows fixing without a visible mark.

## Install

```sh
git submodule add https://github.com/wassname/quote-with-provenance.git skills/quote-with-provenance
```

Or copy [SKILL.md](SKILL.md) and [references/metadata.md](references/metadata.md). MIT license.
