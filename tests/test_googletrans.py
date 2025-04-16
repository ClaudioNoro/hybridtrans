import unittest
from translator.googletrans.translator import GoogleTranslator


class TestGoogleTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = GoogleTranslator()
        self.translator.source_lang = "pt"
        self.translator.target_lang = "en"

    def test_basic_translation(self):
        result = self.translator.translate("Olá mundo", "pt", "en")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.lower(), "olá mundo")

    def test_translation_with_keywords(self):
        text = "Olá, {USUARIO}!"
        self.translator.set_keywords(["{USUARIO}"])
        result = self.translator.translate(text, "pt", "en")
        self.assertIn("{USUARIO}", result)

    def test_detect_language(self):
        lang = self.translator.detect_language("Bonjour le monde")
        self.assertEqual(lang, "fr")

    def test_translate_json(self):
        data = {
            "title": "Bem-vindo",
            "button": "Clique aqui",
            "value": 42 
        }
        self.translator.set_keywords([])
        result = self.translator.translate_json(data)
        self.assertIsInstance(result["title"], str)
        self.assertEqual(result["value"], 42)

    def test_translation_of_long_text(self):
        long_text = ("Olá, mundo! " * 100).strip()
        result = self.translator.translate(long_text, "pt", "en")
        self.assertIsInstance(result, str)
        self.assertNotIn("Olá", result)


if __name__ == "__main__":
    unittest.main()
