from translator.googletrans import GoogleTranslator
from translator.googletrans.utils import log_translation


def run_translator():
    """
    Run the Google Translator CLI.
    """
    translator = GoogleTranslator()

    print("=== Google Translator CLI ===")
    source_lang = input("Idioma de origem (ex: en): ")
    target_lang = input("Idioma de destino (ex: pt): ")
    text = input("Texto a traduzir: ")

    try:
        translated = translator.translate(text, source_lang, target_lang)
        log_translation(text, translated)
        print(f"\nTradução: {translated}")
    except Exception as e:
        print(f"Erro: {e}")
