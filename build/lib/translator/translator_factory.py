"""A factory for creating translator instances based on the selected mode."""

from translator.googletrans.translator import GoogleTranslator
from translator.argos.translator import ArgosTranslator
from translator.BaseTranslator import BaseTranslator
from translator.utils.network import is_connected  # Check for internet connection


def get_translator(mode: str = "auto") -> BaseTranslator:
    """
    Returns a translator instance based on the selected mode.
    - "online": uses Google Translate
    - "offline": uses Argos Translate
    - "auto": checks internet connection and selects accordingly
    """
    if mode == "online":
        return GoogleTranslator()
    if mode == "offline":
        return ArgosTranslator()
    if mode == "auto":
        if is_connected():
            print(
                "[INFO] Internet connection detected. Using GoogleTranslator (online)."
            )
            return GoogleTranslator()
        print("[INFO] No internet connection. Using ArgosTranslator (offline).")
        return ArgosTranslator()

    raise ValueError(f"Invalid mode: {mode}")
