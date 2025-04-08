"""
Translator core package.
Exposes shared configs and factory method.
"""

from .config import SUPPORTED_LANGUAGES
from .translator_factory import get_translator

__all__ = ["SUPPORTED_LANGUAGES", "get_translator"]
