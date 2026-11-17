# Scanned quotation behavior cases

Maintained regression inputs from tiny-virtues, `new_rubrics.md`, run `jev14-wisdom-source-led-v1`. Source: James Legge, *The Life and Works of Mencius* (Philadelphia, 1875), pp. 174–175, Mencius 2A.6 and Legge's notes. These are OCR witnesses, not proof of the printed spelling.

## Task for a fresh model

Read `SKILL.md`. Prepare the three passages below for a reader unfamiliar with the book. Use the supplied source attribution. The passages are separate cases; case 3 has a page continuation. Do not consult the expected checks below until after producing the quotations. Return the reading version, not a report about the skill. Do not edit repository files.

### 1. Translator's note, p. 174

```text
Parr.  4,  5.  In  par.  4  we  have  Mencius'  account  of  the  moral  constitution 
of  human  nature.  "  The  feeling  of  distress,  of  shame,"  &c.,  is  in  the  original 
"the  mind  that  feels  distress,  shame,"  &c.  The  mind  is  one,  but  all  these 
feelings  are  natural  to  it,  and  make  it  what  it  is.  "  Principle  "  in  par.  5,  is 
the  right  translation  of  the  original  term,  meaning  "  the  beginning,"  as  the 
end  of  a  clue,  &c.  The  feeling  of  distress  is  in  itself  benevolent,  and  from 
the  primary  feeling  all  benevolent  feelings  and  actions  may  be  developed. 
"  Knowledge  "  is  the  only  term  with  which  I  am  not  satisfied.  Would 
"  wisdom  "  be  a  better  word,  with  the  meaning  it  has  in  such  passages  of  the 
Bible  as  "  The  fear. of  the  Lord  is  the  beginning  of  wisdom  ?  " 
```

### 2. Translation, paragraph 5, p. 174

```text
5.  "  That  feeling  of  distress  is  the  principle  of  benevo- 
lence ;  the  feeling  of  shame  and  dislike  is  the  principle  of 
righteousness ;  the  feeling   of    modesty  and   complaisance 
is  the  principle  of  propriety ;  and  the  feeling  of  approving 
and  disapproving  is  the  principle  of  knowledge. 
```

### 3. Translation, paragraph 6, pp. 174–175

First fragment:

```text
6.  "  Men  have  these  four   principles  just  as  they  have 
their  four  limbs.     When  men,  having  these  four  principles, 
yet   say  of  themselves  that  they  cannot  [manifest  them], 
they  play  the  thief  with  themselves ;  and  he  who  says  of 
```

Page continuation (the source scan is not supplied to verify the OCR reading `lie`):

```text
his  ruler  that  lie  cannot  [manifest  them],  plays  the  thief  with 
his  ruler. 
```

## Expected checks (human review, not checker guarantees)

- All cases: ordinary prose spacing and wrapping; no repeated raw original or cleanup disclaimer for presentation-only changes. Keep a useful source citation.
- Case 1: identify Legge as the speaker, not Mencius. Preserve the question about “wisdom”; do not present a settled translation choice. Remove the stray scan period in “fear. of”. Keep genuine older wording such as “end of a clue” unless explicitly explained or bracketed. If retaining paragraph references, explain which passage they identify.
- Case 2: join “benevo- / lence” as “benevolence”; preserve the four relationships and the term “knowledge”. No original record is needed just for reflow, spacing, or joining a scan-broken word. An extraction-boundary quotation mark must not leave the reading version looking unfinished.
- Case 3: join the sentence across the page boundary; do not leave “and he who says of” dangling. Retain the translator's existing `[manifest them]` and all four-principle/four-limb wording if quoting that span. Do not silently replace unverified `lie` with `he`; flag uncertainty or verify it against another witness. Do not invent a missing source closing quotation mark as though it were source wording.
- Record actual cuts or word changes as required by the skill, separately from repeated model inputs. Presentation cleanup must not erase substantive numbers, meaningful line breaks, or a real qualification.

The raw blocks above are test inputs, not a required format for presenting quotations.

<!-- PI/OpenAI: real OCR cases and behavior checks from the user's tiny-virtues feedback. -->
