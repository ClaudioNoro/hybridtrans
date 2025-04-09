"""A factory for creating translator instances based on the selected mode."""

from enum import StrEnum
from translator.googletrans.translator import GoogleTranslator
from translator.argos.translator import ArgosTranslator
from translator.BaseTranslator import BaseTranslator
from translator.utils.network import is_connected


class Typetranslator(StrEnum):
    """Enum for translator types.

    StrEnum:
    --------
    - `ONLINE`: Google Translate (online)
    - `OFFLINE`: Argos Translate (offline)
    - `AUTO`: Automatically selects the translator based on internet \
        connection status.
    """

    ONLINE = "online"
    OFFLINE = "offline"
    AUTO = "auto"


def get_translator(
        mode: Typetranslator = Typetranslator.AUTO
        ) -> BaseTranslator:
    """
    Returns a translator instance based on the selected mode.
    - `Typetranslator.ONLINE`: uses Google Translate
    - `Typetranslator.OFFLINE`: uses Argos Translate
    - `Typetranslator.AUT`: checks internet connection and selects accordingly
    """
    if mode == Typetranslator.ONLINE:
        return GoogleTranslator()
    if mode == Typetranslator.OFFLINE:
        return ArgosTranslator()
    if mode == Typetranslator.AUTO:
        if is_connected():
            print(
                "[INFO] Internet connection detected. Using GoogleTranslator (online)."
            )
            return GoogleTranslator()
        print("[INFO] No internet connection. Using ArgosTranslator (offline).")
        return ArgosTranslator()

    raise ValueError(f"Invalid mode: {mode}")
