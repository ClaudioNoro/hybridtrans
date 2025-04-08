from googletrans import Translator
from translator.BaseTranslator import BaseTranslator


class GoogleTranslator(BaseTranslator):
    """A translator class that uses the Google Translate API
    Args:
        BaseTranslator (class): Base class for translation
    """

    def __init__(self) -> None:
        self.translator = Translator()

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """Translates text from source_lang to target_lang.
        Args:
            text (str): The text to translate.
            source_lang (str): The source language code (e.g., 'en').
            target_lang (str): The target language code (e.g., 'pt').
            returns:
                str: The translated text.
        Raises: 
            ValueError: If the translation fails or returns an empty response.
        Example:
            >>> translator = GoogleTranslator()
            >>> translated_text = translator.translate("Hello, world!", "en", "pt")
            >>> print(translated_text)
            Olá, mundo!
        """
        try:
            result = self.translator.translate(text, src=source_lang, dest=target_lang)
            if result is None or not hasattr(result, "text"):
                raise ValueError("Translation failed: Empty or malformed response.")

            return result.text
        except Exception as e:
            self.handle_exceptions(e)
            return "[ERROR] Translation failed."

    def detect_language(self, text: str) -> str:
        """Detects the language of the input text.
        Args:
            text (str): The text whose language is to be detected.
        Returns:
            str: The detected language code (e.g., 'en' for English).
        Raises:
            ValueError: If the language detection fails or returns an empty response.
        """
        try:
            result = self.translator.detect(text)
            return result.lang
        except Exception as e:
            self.handle_exceptions(e)
            return None

    def translate_sentence(
        self, sentence: str, source_lang: str, target_lang: str
    ) -> str:
        """
        - Translates a sentence using the Google Translate API.
        - segment_text is Recommended for consistence in larger texts.
        Args:
            sentence (str): The sentence to translate.
            source_lang (str): The source language code (e.g., 'en').
            target_lang (str): The target language code (e.g., 'pt').

        Returns:
            str: The translated sentence.

        Raises:
            - ValueError: If the translation fails or returns an empty response.
        """
        return self.translate(sentence, source_lang, target_lang)

    def handle_exceptions(self, exception):
        """Handles exceptions raised by the Google Translate API."""
        print(f"An error occurred: {exception}")
        raise exception


def initialize_translator() -> GoogleTranslator:
    """
    Initializes and returns a GoogleTranslator instance.
    """
    return GoogleTranslator()


# Utility functions


def detect_language(translator: GoogleTranslator, text: str) -> str:
    """Detects the language of the input text using the provided translator."""
    return translator.detect_language(text)


def translate_word(
    translator: GoogleTranslator, word: str, source_lang: str, target_lang: str
) -> str:
    """Translates a single word using the provided translator."""
    return translator.translate(word, source_lang, target_lang)


def translate_sentence(
    translator: GoogleTranslator, sentence: str, source_lang: str, target_lang: str
) -> str:
    """Translates a sentence using the provided translator."""
    return translator.translate(sentence, source_lang, target_lang)
