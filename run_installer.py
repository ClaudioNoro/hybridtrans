from translator.utils.argos_installer import install_languages_from_config, get_installed_argos_models
from translator.googletrans import GoogleTranslator
import time

#  install_languages_from_config()
print(get_installed_argos_models())


if __name__ == "__main__":
    # Example usage of the GoogleTranslator class
    translator = GoogleTranslator()
    text = "In a small village nestled between rolling hills, a curious cat named Whiskers embarked on an unexpected adventure. One sunny morning, Whiskers discovered a hidden path leading to an enchanted forest. As he ventured deeper, he encountered talking animals, magical plants, and a wise old owl who shared ancient secrets. Whiskers learned about the importance of friendship, bravery, and the wonders of nature. By the time he returned home, he was forever changed, carrying with him the wisdom and memories of his extraordinary journey. The village never looked the same, and Whiskers became a legend among the villagers!" * 10
    source_lang = translator.TypeLanguage.ENGLISH
    target_lang = translator.TypeLanguage.PORTUGUESE

    startTime = time.time()
    translated_text = translator.translate(text, source_lang, target_lang)
    endTime = time.time()
    print(f"Translated text: {translated_text}")
    print(f"time taken: {endTime - startTime:.2f} seconds")

    # startTime = time.time()
    # translated_text = translator.translate(text, source_lang, target_lang)
    # endTime = time.time()
    # print(f"Translated text: {translated_text}")
    # print(f"time taken: {endTime - startTime:.2f} seconds")

    # startTime = time.time()
    # translated_text = translator.translate(text, source_lang, target_lang)
    # endTime = time.time()
    # print(f"Translated text: {translated_text}")
    # print(f"time taken: {endTime - startTime:.2f} seconds")

    # startTime = time.time()
    # translated_text = translator.translate(text, source_lang, target_lang)
    # endTime = time.time()
    # print(f"Translated text: {translated_text}")
    # print(f"time taken: {endTime - startTime:.2f} seconds")
    ####################################################################### LISTA DE ARGUMENTOS PARA VARIAS KEYWORDS