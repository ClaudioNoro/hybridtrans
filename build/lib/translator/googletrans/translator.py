"""
Main module for Google Translate.
Provides an implementation of BaseTranslator using googletrans.
"""

from typing import List
import re
from textblob import TextBlob
from googletrans import Translator
from translator.BaseTranslator import BaseTranslator


class GoogleTranslator(BaseTranslator):
    """A translator class that uses the Google Translate API
    Args:
        BaseTranslator (class): Base class for translation
    """

    def __init__(self, source_lang=None, target_lang=None, text=""):
        super().__init__(source_lang, target_lang, text)
        self._translator = Translator()

    def set_keywords(self, keywords: List[str]) -> None:
        """Define keywords to protect during translation.

        Args:
            keywords (List[str]): A list of keywords to protect.
        """
        self.keywords = keywords

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """Translates text from source_lang to target_lang.

        Args:
            text (str): The text to translate.
            source_lang (str): The source language code (e.g., 'en').
            target_lang (str): The target language code (e.g., 'pt').

        Returns:
            str: The translated text.

        Raises:
            ValueError: If the translation fails or returns an empty response.
        """
        try:
            self.text = text
            self.source_lang = source_lang
            self.target_lang = target_lang

            protected_text = self._protect_keywords(text, self.keywords)
            segments = self._segment_text(protected_text, 100)
            translated_segments = []

            for segment in segments:
                result = self._translator.translate(segment, src=source_lang, dest=target_lang)
                if result is None or not hasattr(result, "text"):
                    raise ValueError("Translation failed: Empty or malformed response.")
                translated_segments.append(result.text)

            translated_text = " ".join(translated_segments)
            self.translated_text = self._restore_keywords(translated_text, self.keywords)
            return self.translated_text

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
            return result.lang
        except Exception as e:
            self.handle_exceptions(e)
            return None

    def translate_sentence(self, sentence: str, source_lang: str, target_lang: str) -> str:
        """
        Translates a sentence using the Google Translate API.
        segment_text is Recommended for consistence in larger texts.

        Args:
            sentence (str): The sentence to translate.
            source_lang (str): The source language code (e.g., 'en').
            target_lang (str): The target language code (e.g., 'pt').

        Returns:
            str: The translated sentence.
        """
        return self.translate(sentence, source_lang, target_lang)

    def handle_exceptions(self, exception):
        """Handles exceptions raised by the Google Translate API."""
        print(f"An error occurred: {exception}")
        raise exception

    def _segment_text(self, text: str, max_sentences: int = 100) -> List[str]:
        """Splits the text into sentences for more reliable translation.

        Args:
            text (str): The text to segment.
            max_sentences (int): The maximum number of sentences to return.

        Returns:
            List[str]: A list of sentences.
        """
        blob = TextBlob(text)
        sentences = [str(sentence) for sentence in blob.sentences]
        return sentences[:max_sentences]

    def _protect_keywords(self, text: str, keywords: List[str]) -> str:
        """Replaces each keyword with a numbered placeholder.

        Args:
            text (str): The text to process.
            keywords (List[str]): A list of keywords to protect.

        Returns:
            str: Text with keywords replaced.
        """
        for idx, keyword in enumerate(keywords, start=1):
            placeholder = f"__{idx}__"
            text = text.replace(keyword, placeholder)
        return text

    def _restore_keywords(self, text: str, keywords: List[str]) -> str:
        """Restores original keywords in place of placeholders.

        Args:
            text (str): The translated text.
            keywords (List[str]): The list of original keywords.

        Returns:
            str: The text with keywords restored.
        """
        for idx, keyword in enumerate(keywords, start=1):
            pattern = re.compile(rf"__{idx}__")
            text = pattern.sub(keyword, text)
        return text
