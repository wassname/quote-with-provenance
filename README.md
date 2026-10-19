# quote-with-provenance

An agent skill for making quotations easy to parse and understand for a new reader who has not read the surrounding document, while preserving the source's meaning as faithfully as possible. Use fair cuts, small clarifications, and enough visible context. Put our explanations, interpretations, and opinions outside the quote and attribute them to us, so the reader can distinguish our view from the author's. Bold the main sentence, cite the source, and use more quotation than editorial.

The reader gets a selected, simplified account that can lose information. The auditor can recover the exact stored source passage when edits are made; this makes the complete record lossless for that passage, not for the whole document.

An unchanged passage needs a visible citation, not a duplicate original. Bold emphasis and line wrapping do not count as edits. When shortening helps, use `...` for cuts and `[brackets]` for changed words. For edited quotations, an HTML comment holds the exact original, including errors, so a reader can check the edits in the raw Markdown. Read [SKILL.md](SKILL.md) for the procedure, record format, and optional claim-verification checks.

<!-- PI/OpenAI: examples checked against the linked Seneca transcription. -->

## Generous quotation

Seneca describes Plato stopping himself before punishing a slave while angry:

> Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. **Later, when a friend who happened to come in asked him what he was doing, he said, "I am exacting punishment from an angry man."** As if stunned he maintained that attitude, unbecoming to a philosopher, of a man in the act of venting his passion, forgetful now of the slave since he had found another whom he was more anxious to punish.

Seneca, [*On Anger* III.12](https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html), trans. John W. Basore, *Moral Essays*, vol. I, p. 285. Emphasis added; apparent scan error `band` retained verbatim. Page update date not stated.

Source context: an online transcription of Basore's translation; Seneca is retelling an anecdote, not providing a transcript of Plato.

## Shortened and clarified quotation

<!--
{"uri":"https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html","original":"Plato once, when he was angry with his slave, was unable to impose delay upon himself, and, bent upon flogging him with his own hand, ordered him forthwith to take off his shirt and bare his shoulders for the blows; but afterwards realizing that he was angry he stayed his uplifted hand, and just as he was stood with his band in the air like one in the act of striking. Later, when a friend who happened to come in asked him what he was doing, he said, \"I am exacting punishment from an angry man.\" As if stunned he maintained that attitude, unbecoming to a philosopher, of a man in the act of venting his passion, forgetful now of the slave since he had found another whom he was more anxious to punish.","fixed":{"band":"hand"}}
-->

> Plato once, when he was angry with his slave, ... bent upon flogging him with his own hand, ordered him [at once] to ... bare his shoulders for the blows;
> but ... realizing that he was angry he [held back] his uplifted hand, and ... stood with his hand in the air like one in the act of striking.
> **Later, when a friend ... asked him what he was doing, [Plato] said, "I am [punishing] an angry man."**

Seneca, [*On Anger* III.12](https://extra.shu.ac.uk/emls/iemls/stoics/seneca_essays_book_1.html), trans. John W. Basore, p. 285. Shortened; emphasis added. Page update date not stated.

The first example keeps the sentences either side of the bolded sentence. The second shortens the passage and marks plainer wording (`[at once]`, `[held back]`, `[punishing]`) and a clarified pronoun (`[Plato]`). Only the edited example duplicates the exact source passage in a JSON comment, including the recorded `band` → `hand` correction. The unchanged example needs no duplicate; both need visible context and a citation.

## Check a saved quotation

From this skill's directory:

```sh
uv run scripts/check_quote.py /path/to/notes.md
```

The checker tests recorded quotations against each `original`, and checks the original against `uri` when it is a readable local file. It skips unrecorded quotations, does not fetch web sources, and does not decide whether an edit changes the meaning.

## Install

Clone into your agent's skills folder, e.g. for Claude Code:

```sh
git clone https://github.com/wassname/quote-with-provenance.git ~/.claude/skills/quote-with-provenance
```

If your skills folder is a git repo, add it as a submodule instead:

```sh
cd ~/.claude/skills
git submodule add https://github.com/wassname/quote-with-provenance.git quote-with-provenance
git commit -m "Add quote-with-provenance skill"
```

Or with [vercel-labs/skills](https://github.com/vercel-labs/skills): `npx skills add wassname/quote-with-provenance`. Or copy [SKILL.md](SKILL.md). MIT license.
