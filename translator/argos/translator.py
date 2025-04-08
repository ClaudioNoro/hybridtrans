from enum import StrEnum
from argostranslate import translate
from translator.BaseTranslator import BaseTranslator


class ArgosTranslator(BaseTranslator):
    """
    Offline translator using Argos Translate.
    """
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

        # get all languages
        @classmethod
        def get_all_languages(cls) -> list[str]:
            """Returns all languages as a list of strings."""
            return [lang.value for lang in cls]
        
    def __init__(self):
        self.installed_languages = translate.get_installed_languages()
        if not self.installed_languages:
            raise RuntimeError(
                "No Argos Translate language packages installed.\n"
                "Please install a '.argosmodel' file to enable offline translation."
            )
        self._source_lang = None
        self._target_lang = None
        self._text = None
        self._translated_text = None
        self_keywords = None

    def translate(self, text: str, source_lang: TypeLanguage, target_lang: TypeLanguage) -> str:
        """
        Translate text using Argos Translate.

        Args:
            text (str): The text to translate.
            source_lang (TypeLanguage): The source language code (e.g., 'ENGLISH').
            target_lang (TypeLanguage): The target language code (e.g., 'PORTUGUESE').

        Returns:
            str: The translated text.
        Example:
            >>> translator = ArgosTranslator()
            >>> translated_text = translator.translate("Hello, world!", "en", "pt")
            >>> print(translated_text)
            Olá, mundo!
        """
        from_lang = next(
            (lang for lang in self.installed_languages if lang.code == source_lang),
            None,
        )
        to_lang = next(
            (lang for lang in self.installed_languages if lang.code == target_lang),
            None,
        )

        if not from_lang or not to_lang:
            raise ValueError(
                f"Translation not supported for language pair: {source_lang} → {target_lang}.\n"
                "Make sure the appropriate Argos model is installed."
            )

        translation = from_lang.get_translation(to_lang)
        return translation.translate(text)

    def detect_language(self, text: str) -> str:
        """
        Language detection is not supported by Argos Translate.

        Raises:
            NotImplementedError
        """
        raise NotImplementedError(
            "Language detection is not supported in Argos Translate."
        )

    def translate_sentence(
        self, sentence: str, source_lang: str, target_lang: str
    ) -> str:
        """
        - Translates a single sentence using the same logic as `translate`.
        - segment_text is Recommended for consistence in larger texts.
        Args:
            sentence (str): The sentence to translate.
            source_lang (str): Source language code.
            target_lang (str): Target language code.

        Returns:
            str: Translated sentence.
        """
        return self.translate(sentence, source_lang, target_lang)
