from . import ArgosTranslator


def run_translator():
    """
    Main function to run the Argos Translator.
    """
    translator = ArgosTranslator()
    source_lang = input("Source language (ex: en): ")
    target_lang = input("Target language (ex: pt): ")
    text = input("Text to translate: ")

    try:
        translated = translator.translate(text, source_lang, target_lang)
        print(f"Translated: {translated}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run_translator()
