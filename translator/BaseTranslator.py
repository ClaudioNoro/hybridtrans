from abc import ABC, abstractmethod
from enum import StrEnum


class BaseTranslator(ABC):
    """Base class for translation services."""

    class TypeLanguage(StrEnum):
        """ Enum for language types.
        
        StrEnum:
        --------
        - `ENGLISH`: English
        - `PORTUGUESE`: Portuguese
        - `SPANISH`: Spanish
        - `FRENCH`: French
        - `GERMAN`: German
        """

        ENGLISH = "en"
        PORTUGUESE = "pt"
        SPANISH = "es"
        FRENCH = "fr"
        GERMAN = "de"
        
    @abstractmethod
    def translate(self, text: str, source_lang: TypeLanguage, target_lang: TypeLanguage) -> str:
        """Translate text from source_lang to target_lang.
        Args:
            text (str): The text to translate.
            source_lang (TypeLanguage): The source language code (e.g., 'ENGLISH').
            target_lang (TypeLanguage): The target language code (e.g., 'PORTUGUESE').
        Returns:
            str: The translated text.
        """
        raise NotImplementedError(
            "translate() must be implemented by subclasses of BaseTranslator"
        )

    @abstractmethod
    def detect_language(self, text: str) -> str:
        """Detect the language of the input text.
        >>> DOES NOT WORK FOR ARGOS TRANSLATE.
        Args:
            text (str): The text whose language is to be detected.
        Returns:
                str: The detected language code (e.g., 'en' for English)."""
        raise NotImplementedError("translate() must be implemented by subclasses of BaseTranslator")

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
        raise NotImplementedError("translate() must be implemented by subclasses of BaseTranslator")
    
    @abstractmethod
    def translate_json(self, json_path: str, source_lang: str, target_lang: str) -> str:
        """Translate a JSON object from source_lang to target_lang.
        Args:
            json_path (str): The JSON file path to translate.
            source_lang (str): The source language code (e.g., 'en').
            target_lang (str): The target language code (e.g., 'pt').
        Returns:
            dict: The translated JSON object.
        """
        raise NotImplementedError("translate() must be implemented by subclasses of BaseTranslator")
