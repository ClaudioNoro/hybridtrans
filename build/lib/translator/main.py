import sys
import asyncio
from translator.translator_factory import get_translator


async def main() -> None:
    """
    Main async function to run the translator via command line.
    
    Arguments:
        text: str - Text to be translated
        source_lang: str - Source language code (e.g., 'en')
        target_lang: str - Target language code (e.g., 'pt')
        mode: str - Translation mode ('auto', 'online', or 'offline')
    
    Example:
        - python -m translator.main "hello world" en pt auto
        - python -m translator.main "hello world" en pt online
        - python -m translator.main "hello world" en pt offline
    """
    if len(sys.argv) < 4:
        print("Usage: python -m translator.main <text> <source_lang> <target_lang> [mode]")
        print('Example: python -m translator.main "hello world" en pt auto')
        sys.exit(1)

    text = sys.argv[1]
    source_lang = sys.argv[2]
    target_lang = sys.argv[3]
    mode = sys.argv[4] if len(sys.argv) > 4 else "auto"

    translator = get_translator(mode=mode)

    # Suporte tanto para métodos assíncronos quanto síncronos
    try:
        if hasattr(translator.translate, "__call__") and asyncio.iscoroutinefunction(translator.translate):
            translated_text = await translator.translate(text, source_lang, target_lang)
        else:
            translated_text = translator.translate(text, source_lang, target_lang)

        print(f"\n[Translated Text]\n{translated_text}")
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
