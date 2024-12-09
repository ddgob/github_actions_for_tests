import unittest
from text_analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):
    def test_count_words(self):
        analyzer = TextAnalyzer("Hello world")
        self.assertEqual(analyzer.count_words(), 2)

    def test_count_characters(self):
        analyzer = TextAnalyzer("Hello world")
        self.assertEqual(analyzer.count_characters(), 11)

if __name__ == "__main__":
    unittest.main()
