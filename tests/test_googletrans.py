import unittest
from translator.googletrans.translator import (
    initialize_translator,
    translate_word,
    translate_sentence,
)


class TestGoogleTranslator(unittest.TestCase):
    def setUp(self):
        """Set up the GoogleTranslator instance before each test."""
        self.translator = initialize_translator()

    def test_translate_valid_word(self):
        """Test translation of a single valid word."""
        print("test_translate_valid_word")
        word = "Hello"
        source_lang = "en"  # English
        target_lang = "es"  # Spanish
        translated_word = translate_word(
            self.translator, word, source_lang, target_lang
        )
        self.assertIsInstance(translated_word, str)
        self.assertNotEqual(translated_word, word)  # Ensure translation occurred

    def test_translate_valid_sentence(self):
        """Test translation of a valid sentence."""
        print("test_translate_valid_sentence")
        sentence = "How are you?"
        source_lang = "en"  # English
        target_lang = "es"  # Spanish
        translated_sentence = translate_sentence(
            self.translator, sentence, source_lang, target_lang
        )
        self.assertIsInstance(translated_sentence, str)
        self.assertNotEqual(
            translated_sentence, sentence
        )  # Ensure translation occurred

    def test_translate_invalid_language_code(self):
        """Test translation with an invalid source language code."""
        print("test_translate_invalid_language_code")
        sentence = "Hello"
        source_lang = "xx"  # Invalid language code
        target_lang = "es"  # Spanish
        with self.assertRaises(
            Exception
        ):  # Expecting an exception for invalid language code
            translate_sentence(self.translator, sentence, source_lang, target_lang)

    def test_translate_empty_text(self):
        """Test translation of an empty string."""
        print("test_translate_empty")
        sentence = ""
        source_lang = "en"  # English
        target_lang = "es"  # Spanish
        translated_sentence = translate_sentence(
            self.translator, sentence, source_lang, target_lang
        )
        self.assertEqual(
            translated_sentence, ""
        )  # Empty input should return empty output

    def test_translate_large_text(self) -> None:
        print("test_translate_large_text")
        """Test translation of a large text."""
        sentence = "Hello " * 1000  # Large input text
        source_lang = "en"  # English
        target_lang = "es"  # Spanish
        translated_sentence = translate_sentence(
            self.translator, sentence, source_lang, target_lang
        )
        self.assertIsInstance(translated_sentence, str)
        self.assertNotEqual(
            translated_sentence, sentence
        )  # Ensure translation occurred

    def test_translate_with_keywords(self):
        text = "Hello admin and guest"
        keywords = ["admin", "guest"]
        result = self.translator.translate(text, "en", "pt", keywords=keywords)
        self.assertIn("admin", result)
        self.assertIn("guest", result)
        self.assertNotIn("__1__", result)


if __name__ == "__main__":
    unittest.main()
