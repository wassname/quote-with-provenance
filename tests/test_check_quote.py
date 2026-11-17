"""Regression tests for quote-record parsing. -- PI/OpenAI"""

import importlib.util
import re
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location(
    "check_quote", Path(__file__).parents[1] / "scripts" / "check_quote.py"
)
check_quote = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_quote)


class QuoteRecordParsingTests(unittest.TestCase):
    def test_unpaired_example_record_does_not_consume_next_comment(self):
        markdown = '''<!--
{"original":"placeholder"}
-->

An example follows.

<!-- PI/OpenAI: example attribution. -->

<!--
{"original":"Before. Main point. After."}
-->

> Before. **Main point.** After.
'''
        self.assertEqual(
            list(check_quote.blocks(markdown)),
            [({"original": "Before. Main point. After."}, "Before. **Main point.** After.")],
        )


class ScannedQuotationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cases = Path(__file__).with_name("ocr_cleanup.md").read_text()
        cls.originals = re.findall(r"```text\n(.*?)\n```", cases, re.S)

    def test_legge_note_allows_spacing_and_scan_punctuation_cleanup(self):
        quote = '''Parr. 4, 5. In par. 4 we have Mencius' account of the moral constitution of human nature. "The feeling of distress, of shame," &c., is in the original "the mind that feels distress, shame," &c. The mind is one, but all these feelings are natural to it, and make it what it is. "Principle" in par. 5, is the right translation of the original term, meaning "the beginning," as the end of a clue, &c. The feeling of distress is in itself benevolent, and from the primary feeling all benevolent feelings and actions may be developed. "Knowledge" is the only term with which I am not satisfied. Would "wisdom" be a better word, with the meaning it has in such passages of the Bible as "The fear of the Lord is the beginning of wisdom?"'''
        self.assertEqual(check_quote.problems(quote, self.originals[0]), [])

    def test_line_end_hyphen_is_layout_not_a_word_substitution(self):
        quote = '''5. "That feeling of distress is the principle of benevolence; the feeling of shame and dislike is the principle of righteousness; the feeling of modesty and complaisance is the principle of propriety; and the feeling of approving and disapproving is the principle of knowledge.'''
        self.assertEqual(check_quote.problems(quote, self.originals[1]), [])
        self.assertTrue(check_quote.problems(quote.replace("knowledge", "wisdom"), self.originals[1]))

    def test_page_continuation_keeps_translator_brackets(self):
        quote = '''6. "Men have these four principles just as they have their four limbs. When men, having these four principles, yet say of themselves that they cannot [manifest them], they play the thief with themselves; and he who says of his ruler that lie cannot [manifest them], plays the thief with his ruler.'''
        original = self.originals[2] + "\n" + self.originals[3]
        self.assertEqual(check_quote.problems(quote, original), [])
        self.assertEqual(check_quote.editor_insertions(quote, original), [])

    def test_checker_fixtures(self):
        for filename, should_pass in (("should_pass.md", True), ("should_fail.md", False)):
            blocks = list(check_quote.blocks(Path(__file__).with_name(filename).read_text()))
            self.assertTrue(blocks)
            for record, quote in blocks:
                with self.subTest(filename=filename, quote=quote):
                    problems = check_quote.problems(quote, record["original"], record.get("fixed"))
                    self.assertEqual(not problems, should_pass, problems)


if __name__ == "__main__":
    unittest.main()
