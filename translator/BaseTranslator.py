"""
Base class for translation services.
This module defines the `BaseTranslator` class, which serves as an \
    abstract base
class for all translation services. It provides a common interface for \
translating text, detecting languages, and handling keywords.
"""
from abc import ABC, abstractmethod
from enum import StrEnum
from typing import List


class BaseTranslator(ABC):
    """Base class for translation services."""

    class TypeLanguage(StrEnum):
        """Enum for language types.

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

    @abstractmethod
    def translate(
        self, text: str, source_lang: TypeLanguage, target_lang: TypeLanguage
    ) -> str:
        """Translate text from source_lang to target_lang.

        Args:
            text (str): The text to translate.
            source_lang (TypeLanguage): The source language code \
                (e.g., 'ENGLISH').
            target_lang (TypeLanguage): The target language code \
                (e.g., 'PORTUGUESE').

        Returns:
            str: The translated text.
        """
        raise NotImplementedError(
            "translate() must be implemented by subclasses of BaseTranslator"
        )

    @abstractmethod
    def detect_language(self, text: str) -> str:
        """Detect the language of the input text.

        Args:
            text (str): The text whose language is to be detected.

        Returns:
            str: The detected language code (e.g., 'en' for English).
        """
        raise NotImplementedError(
            "detect_language() must be implemented by subclasses of \
                BaseTranslator"
        )

    @abstractmethod
    def set_keywords(self, keywords: List[str]) -> None:
        """Define keywords to protect during translation.

        Args:
            keywords (List[str]): A list of keywords to protect.
        """
        raise NotImplementedError(
            "set_keywords() must be implemented by subclasses of \
                BaseTranslator"
        )

    @abstractmethod
    def translate_sentence(
        self, sentence: str, source_lang: TypeLanguage,
        target_lang: TypeLanguage
    ) -> str:
        """Translate a sentence to the target language.

        Args:
            sentence (str): The sentence to translate.
            source_lang (TypeLanguage): The source language code (e.g., \
                'ENGLISH').
            target_lang (TypeLanguage): The target language code (e.g., \
                'PORTUGUESE').

        Returns:
            str: The translated sentence.
        """
        raise NotImplementedError(
            "translate_sentence() must be implemented by subclasses of \
                BaseTranslator"
        )

    @abstractmethod
    def translate_json(
        self, json_path: str, source_lang: TypeLanguage,
        target_lang: TypeLanguage
    ) -> str:
        """Translate a JSON object from source_lang to target_lang.

        Args:
            json_path (str): The JSON file path to translate.
            source_lang (TypeLanguage): The source language code \
                (e.g., 'ENGLISH').
            target_lang (TypeLanguage): The target language code \
                (e.g., 'PORTUGUESE').

        Returns:
            str: The translated JSON object.
        """
        raise NotImplementedError(
            "translate_json() must be implemented by subclasses of \
                BaseTranslator"
        )
