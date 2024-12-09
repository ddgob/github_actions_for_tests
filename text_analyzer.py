class TextAnalyzer:

    def __init__(self, text):
        self.text = text

    def count_words(self):
        """Counts the number of words in a given text."""
        return len(self.text.split())

    def count_characters(self):
        """Counts the number of characters in a given text."""
        return len(self.text)
