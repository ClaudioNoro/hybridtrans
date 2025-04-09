""" Module for Google Translate API integration.
This module provides a class for translating text using the \
      Google Translate API.
It includes methods for translating text, detecting language,\
      and handling exceptions.
It also provides functionality to protect specific keywords from translation.
"""
from enum import StrEnum
import re
from typing import List
from googletrans import Translator
from translator.BaseTranslator import BaseTranslator

from textblob import TextBlob


class GoogleTranslator(BaseTranslator):
    """
    A translator class that uses the Google Translate API with\
    integrated text handling.
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
        # Enum for language types
        ENGLISH = "en"
        PORTUGUESE = "pt"
        SPANISH = "es"
        FRENCH = "fr"

        @classmethod
        def get_all_languages(cls) -> list[str]:
            """Returns all supported languages as a list of strings."""
            return [lang.value for lang in cls]

    def __init__(self) -> None:
        """Initializes the GoogleTranslator instance."""
        self._translator = Translator()
        self._source_lang = None
        self._target_lang = None
        self._text = None
        self._translated_text = None
        self._keywords = []  # Store user-defined keywords

    def set_keywords(self, keywords: List[str]) -> None:
        """Allows the user to define keywords to protect during translation.

        Args:
            keywords (List[str]): A list of keywords to protect.
        """
        self._keywords = keywords

    def translate(self, text: str, source_lang: TypeLanguage,
                  target_lang: TypeLanguage) -> str:
        """Translates text from the source language to the target language."""
        try:
            # Validate inputs
            if not text:
                raise ValueError(
                    "The text to translate cannot be None or empty.")
            if not source_lang:
                raise ValueError("The source language cannot be None.")
            if not target_lang:
                raise ValueError("The target language cannot be None.")

            # Set private variables
            self._text = text
            self._source_lang = source_lang
            self._target_lang = target_lang

            # Protect keywords
            protected_text = self._protect_keywords(self._text, self._keywords)

            # Segment text
            segments = self._segment_text(protected_text, 100)
            translated_segments = []

            # Translate each segment
            for segment in segments:
                result = self._translator.translate(
                    segment, src=self._source_lang, dest=self._target_lang)
                translated_segments.append(result.text)

            # Combine translated segments
            translated_text = " ".join(translated_segments)

            # Restore keywords
            self._translated_text = self._restore_keywords(
                translated_text, self._keywords)
            return self._translated_text

        except Exception as e:
            self.handle_exceptions(e)
            return "[ERROR] Translation failed."

    def detect_language(self, text: str) -> str:
        """Detects the language of the input text."""
        try:
            self._text = text
            result = self._translator.detect(self._text)
            return result.lang
        except Exception as e:
            self.handle_exceptions(e)
            return "unknown"

    # Private methods for text handling

    def _segment_text(self, text: str, max_sentences: int = 100) -> List[str]:
        """Segments a block of text into a list of sentences."""
        blob = TextBlob(text)
        sentences = [str(sentence) for sentence in blob.sentences]
        return sentences[:max_sentences]

    def _protect_keywords(self, text: str, keywords: List[str]) -> str:
        """
        Replaces each keyword with a numbered \
        placeholder to prevent translation.
        """
        for idx, keyword in enumerate(keywords, start=1):
            placeholder = f"__{idx}__"
            text = text.replace(keyword, placeholder)
        return text

    def _restore_keywords(self, text: str, keywords: List[str]) -> str:
        """Replaces numbered placeholders with the original keywords."""
        for idx, keyword in enumerate(keywords, start=1):
            pattern = re.compile(rf"__{idx}__")
            text = pattern.sub(keyword, text)
        return text

    def handle_exceptions(self, exception):
        """Handles exceptions raised by the Google Translate API."""
        print(f"An error occurred: {exception}")
        raise exception
