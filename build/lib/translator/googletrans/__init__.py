"""
Google Translate implementation (online).
Exposes key functions and class.
"""

from .translator import (
    GoogleTranslator,
    translate_word,
    translate_sentence,
    initialize_translator
)

__all__ = [
    "GoogleTranslator",
    "translate_word",
    "translate_sentence",
    "initialize_translator"
]
