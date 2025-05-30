"""
Shared utility functions used by both online and offline translators.
"""

from .handletext import (
    read_file,
    segment_text,
    protect_keywords,
    restore_keywords,
    normalize_text,
    log_translation,
    define_keywords,
    extract_keywords
)
from .network import is_connected

__all__ = [
    "read_file",
    "segment_text",
    "protect_keywords",
    "restore_keywords",
    "normalize_text",
    "log_translation",
    "is_connected",
    "define_keywords",
    "extract_keywords"
]
