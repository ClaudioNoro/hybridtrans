import unittest
from translator.utils.handletext import protect_keywords, restore_keywords


class TestHandleText(unittest.TestCase):
    def setUp(self):
        self.keywords = ["admin", "guest"]
        self.original_text = "Hello admin and guest!"

    def test_protect_keywords(self):
        protected = protect_keywords(self.original_text, self.keywords)
        self.assertIn("__1__", protected)
        self.assertIn("__2__", protected)
        self.assertNotIn("admin", protected)
        self.assertNotIn("guest", protected)

    def test_restore_keywords(self):
        text_with_placeholders = "Olá __1__ e __2__!"
        restored = restore_keywords(text_with_placeholders, self.keywords)
        self.assertIn("admin", restored)
        self.assertIn("guest", restored)
        self.assertNotIn("__1__", restored)
        self.assertNotIn("__2__", restored)


if __name__ == "__main__":
    unittest.main()
