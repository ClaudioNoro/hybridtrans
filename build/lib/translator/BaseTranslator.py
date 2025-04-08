from abc import ABC, abstractmethod


class BaseTranslator(ABC):
    """Base class for translation services."""

    @abstractmethod
    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """Translate text from source_lang to target_lang.
        Args:
            text (str): The text to translate.
            source_lang (str): The source language code (e.g., 'en').
            target_lang (str): The target language code (e.g., 'pt').
        Returns:
            str: The translated text.
        """
        pass

    @abstractmethod
    def detect_language(self, text: str) -> str:
        """Detect the language of the input text.
        >>> DOES NOT WORK FOR ARGOS TRANSLATE.
        Args:
            text (str): The text whose language is to be detected.
        Returns:
                str: The detected language code (e.g., 'en' for English)."""
        pass

    @abstractmethod
    def translate_sentence(self, sentence: str, target_lang: str) -> str:
        """Translate a sentence to the target language.
        - segment_text is Recommended for consistence in larger texts.
        Args:
            sentence (str): The sentence to translate.
            target_lang (str): The target language code (e.g., 'pt').
        Returns:
            str: The translated sentence.
        """
        pass
