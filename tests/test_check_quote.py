"""Regression tests for quote-record parsing. -- PI/OpenAI"""

import importlib.util
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


if __name__ == "__main__":
    unittest.main()
