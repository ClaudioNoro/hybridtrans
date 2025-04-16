"""
Main module for Argos Translate.
This module provides a class for translating text using the Argos Translate
translation modules that can be found at:
.
"""
import re
from typing import List
from enum import StrEnum
from argostranslate import translate
from translator.BaseTranslator import BaseTranslator
from textblob import TextBlob


class ArgosTranslator(BaseTranslator):
    """
    Offline translator using Argos Translate with integrated text handling.
    """

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

        @classmethod
        def get_all_languages(cls) -> list[str]:
            """Returns all supported languages as a list of strings."""
            return [lang.value for lang in cls]

    def __init__(self, source_lang=None, target_lang=None, text=""):
        super().__init__(source_lang, target_lang, text)
        self.installed_languages = translate.get_installed_languages()
        if not self.installed_languages:
            raise RuntimeError(
                "No Argos Translate language packages installed.\n"
                "Please install a '.argosmodel' file to enable offline translation."
            )

    def set_keywords(self, keywords: List[str]) -> None:
        """Allows the user to define keywords to protect during translation.

        Args:
            keywords (List[str]): A list of keywords to protect.
        """
        self.keywords = keywords

    def translate(self, text: str, source_lang: TypeLanguage,
                  target_lang: TypeLanguage) -> str:
        """Translates text using Argos Translate.

        Args:
            text (str): The text to translate.
            source_lang (TypeLanguage): The source language code (e.g., 'ENGLISH').
            target_lang (TypeLanguage): The target language code (e.g., 'PORTUGUESE').

        Returns:
            str: The translated text.
        """
        try:
            if not text:
                raise ValueError("The text to translate cannot be None or empty.")
            if not source_lang:
                raise ValueError("The source language cannot be None.")
            if not target_lang:
                raise ValueError("The target language cannot be None.")

            self.text = text
            self.source_lang = source_lang
            self.target_lang = target_lang

            protected_text = self._protect_keywords(self.text, self.keywords)
            segments = self._segment_text(protected_text, 100)
            translated_segments = [self._translate_segment(segment) for segment in segments]
            translated_text = " ".join(translated_segments)
            self.translated_text = self._restore_keywords(translated_text, self.keywords)

            return self.translated_text

        except Exception as e:
            self.handle_exceptions(e)
            return "[ERROR] Translation failed."

    def detect_language(self, text: str) -> str:
        """Language detection is not supported by Argos Translate."""
        raise NotImplementedError("Language detection is not supported in Argos Translate.")

    def _translate_segment(self, segment: str) -> str:
        """Translates a single segment of text."""
        from_lang = next((lang for lang in self.installed_languages if lang.code == self.source_lang), None)
        to_lang = next((lang for lang in self.installed_languages if lang.code == self.target_lang), None)

        if not from_lang or not to_lang:
            raise ValueError(
                f"Translation not supported for language pair: {self.source_lang} → {self.target_lang}.\n"
                "Make sure the appropriate Argos model is installed."
            )

        translation = from_lang.get_translation(to_lang)
        return translation.translate(segment)

    def _segment_text(self, text: str, max_sentences: int = 100) -> List[str]:
        """Segments a block of text into a list of sentences.

        Args:
            text (str): The text to process.
            max_sentences (int): Maximum number of sentences to segment.

        Returns:
            List[str]: A list of sentences.
        """
        blob = TextBlob(text)
        sentences = [str(sentence) for sentence in blob.sentences]
        return sentences[:max_sentences]

    def _protect_keywords(self, text: str, keywords: List[str]) -> str:
        """
        Replaces each keyword with a numbered placeholder to prevent translation.

        Args:
            text (str): The text to process.
            keywords (List[str]): A list of keywords to protect.

        Returns:
            str: The processed text with keywords replaced by placeholders.
        """
        for idx, keyword in enumerate(keywords, start=1):
            placeholder = f"__{idx}__"
            text = text.replace(keyword, placeholder)
        return text

    def _restore_keywords(self, text: str, keywords: List[str]) -> str:
        """Replaces numbered placeholders with the original keywords.

        Args:
            text (str): The text to process.
            keywords (List[str]): A list of keywords to restore.

        Returns:
            str: The processed text with placeholders replaced by original keywords.
        """
        for idx, keyword in enumerate(keywords, start=1):
            pattern = re.compile(rf"__{idx}__")
            text = pattern.sub(keyword, text)
        return text

    def handle_exceptions(self, exception):
        """Handles exceptions raised by Argos Translate.

        Args:
            exception (Exception): The exception to handle.

        Raises:
            exception: Re-raises the exception after logging it.
        """
        print(f"An error occurred: {exception}")
        raise exception
