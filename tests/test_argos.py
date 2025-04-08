import unittest
from translator.argos.translator import ArgosTranslator


class TestArgosTranslator(unittest.TestCase):
    def setUp(self):
        """Set up the ArgosTranslator instance before each test."""
        self.translator = ArgosTranslator()

    def test_translate_valid_languages(self):
        """Test translation with valid source and target languages."""
        text = "Hello"
        source_lang = "en"  # English
        target_lang = "es"  # Spanish
        translated_text = self.translator.translate(text, source_lang, target_lang)
        self.assertIsInstance(translated_text, str)
        self.assertNotEqual(translated_text, text)  # Ensure translation occurred

    def test_translate_invalid_languages(self):
        """Test translation with unsupported source or target languages."""
        text = "Hello"
        source_lang = "xx"  # Invalid language code
        target_lang = "es"  # Spanish
        with self.assertRaises(ValueError):
            self.translator.translate(text, source_lang, target_lang)


if __name__ == "__main__":
    unittest.main()
