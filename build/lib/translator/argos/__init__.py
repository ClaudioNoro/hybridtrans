"""
Argos Translate implementation (offline).
Exposes core translator class and installer interface.
"""

from translator.utils.argos_installer import (
    install_argos_model,
    uninstall_argos_model,
    install_languages_from_config,
)
from .translator import ArgosTranslator

__all__ = [
    "ArgosTranslator",
    "install_argos_model",
    "uninstall_argos_model",
    "install_languages_from_config",
]
