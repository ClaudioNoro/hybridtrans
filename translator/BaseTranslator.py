"""
Base class for translation services.
This module defines the `BaseTranslator` class, which serves as an
    abstract base
class for all translation services. It provides a common interface for
translating text, detecting languages, and handling keywords.
"""

from abc import ABC, abstractmethod
from enum import StrEnum
from typing import List, Union
from translator.utils.handletext import (
    extract_keywords,
    protect_keywords,
    restore_keywords,
)


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
        - `DEFAULT`: Default language (English)
        """

        ENGLISH = "en"
        PORTUGUESE = "pt"
        SPANISH = "es"
        FRENCH = "fr"
        DEFAULT = ENGLISH

    @abstractmethod
    def __init__(
        self,
        source_lang: TypeLanguage,
        target_lang: TypeLanguage,
        text: str = "",
        keywords: List[str] = None,
    ):
        """
        Initialize the BaseTranslator with source language, target language, text, and keywords.

        Args:
            source_lang (TypeLanguage): The source language code (e.g., 'ENGLISH').
            target_lang (TypeLanguage): The target language code (e.g., 'PORTUGUESE').
            text (str): The text to translate (default is an empty string).
            keywords (List[str]): A list of keywords to protect (default is None).
        """
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.text = text
        self.translated_text = ""
        self.keywords = keywords or []

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

    def translate_json(self, json_data: dict[str, Union[str, int]]) -> dict[str, Union[str, int]]:
        """
        Translates the string values of a JSON-like dictionary in memory.

        Args:
          json_data (dict[str, [str, int]]): A dictionary with string values to be translated.

        Returns:
            dict[str, [str, int]]: A dictionary with translated string values.
        """
        translated_data = {}

        for key, value in json_data.items():
            if isinstance(value, str):
                protected = protect_keywords(value, self.keywords)
                translated = self.translate(
                    protected, self.source_lang, self.target_lang
                )
                restored = restore_keywords(translated, self.keywords)
                translated_data[key] = restored
            else:
                translated_data[key] = value  # keep as-is if not string

        return translated_data

    def set_keywords_from_text(self, text: str, method: str = "curly") -> None:
        """
        Extracts and sets self._keywords using a regex pattern method.

        Args:
            text (str): The input text containing keywords to extract.
            method (str): Extraction method (e.g., 'curly', 'brackets', 'allcaps', etc.).
        """
        self.keywords = extract_keywords(text, method)
