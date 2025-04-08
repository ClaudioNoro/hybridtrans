from enum import StrEnum
from googletrans import Translator
from translator.BaseTranslator import BaseTranslator
from translator.utils.handletext import segment_text\



class GoogleTranslator(BaseTranslator):
    """A translator class that uses the Google Translate API
    Args:
        BaseTranslator (class): Base class for translation
    """

    class TypeLanguage(StrEnum):
        """ Enum for language types.
        
        StrEnum:
        --------
        - `ENGLISH`: English
        - `PORTUGUESE`: Portuguese
        - `SPANISH`: Spanish
        - `FRENCH`: French
        """

        ENGLISH = "en"
        PORTUGUESE = "pt"
        SPANISH = "es"
        FRENCH = "fr"

        # get all languages
        @classmethod
        def get_all_languages(cls) -> list[str]:
            """Returns all languages as a list of strings."""
            return [lang.value for lang in cls]

    def __init__(self) -> None:
        self._translator = Translator()
        self._source_lang = None
        self._target_lang = None
        self._text = None
        self._translated_text = None
        self_keywords = None

    def translate(self, text: str, source_lang: TypeLanguage, target_lang: TypeLanguage) -> str:
        """ Translates text from source_lang to target_lang.
         
        Arg:
        ----
        - text (`str`): The text to translate.
        - source_lang (`TypeLanguage`): The source language code (e.g., TypeLanguage.ENGLISH).
        - target_lang (`TypeLanguage`): The target language code (e.g., TypeLanguage.PORTUGUESE).
         
        Return:
        -------
        - `str`:  The translated text.

        Raise:
        ------
        - `ValueError`: If the translation fails or returns an empty response.

        Example:
        --------
        >>> translator = GoogleTranslator()
        >>> translated_text = translator.translate("Hello, world!", "en", "pt")
        >>> print(translated_text)
        Olá, mundo!
        """
        try:
            segments = segment_text(text, 100)  # Segment the text into smaller parts |||||||||||||||||| remove hardcode
            translated_segments = []

            for segment in segments:
                result = self._translator.translate(segment, src=source_lang, dest=target_lang)
                translated_segments.append(result.text)

            return " ".join(translated_segments)

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
            result = self._translator.detect(text)
            return result.lang  # mesmo de cima
        except Exception as e:
            self.handle_exceptions(e)
            return "unknown"  # Return a default value if detection fails

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

    def translate_json(self, json_path: str, source_lang: str, target_lang: str) -> str:
        """ Translates the data from a JSON without changing the structure of the JSON.
         
        Arg:
        ----
        - json_path (`str`): Path to the JSON file.
        - source_lang (`str`): The source language code (e.g., 'en').
        - target_lang (`str`): The target language code (e.g., 'pt').
         
        Return:
        -------
        - `str`: The translated data in JSON format.
        """

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
