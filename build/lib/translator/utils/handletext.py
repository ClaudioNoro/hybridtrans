from textblob import TextBlob
from typing import List
import re


def read_file(file_path: str) -> str:
    """
    Reads the content of a text file.
    Args:
        file_path (str): Path to the text file.
    Returns:
        str: Content of the file.
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def segment_text(text: str, max_sentences: int = 100) -> List[str]:
    """
    Segments a block of text into a list of sentences using TextBlob.
    Args:
        text (str): Text to be segmented.
        max_sentences (int): Maximum number of sentences to return.
    Returns:
        List[str]: List of sentences.
    """
    blob = TextBlob(text)
    sentences = [str(sentence) for sentence in blob.sentences]
    return sentences[:max_sentences]


def protect_keywords(text: str, keywords: List[str]) -> str:
    """
    Replaces each keyword with a numbered placeholder: __1__, __2__, etc.
    This prevents them from being translated.

    Args:
        text (str): Original text.
        keywords (List[str]): List of keywords to protect.

    Returns:
        str: Text with protected placeholders.
    """
    for idx, keyword in enumerate(keywords, start=1):
        placeholder = f"__{idx}__"
        text = text.replace(keyword, placeholder)
    return text


def restore_keywords(text: str, keywords: List[str]) -> str:
    """
    Replaces numbered placeholders (__1__, __2__, ...) with the original keywords.

    Args:
        text (str): Text after translation.
        keywords (List[str]): Original keywords in order.

    Returns:
        str: Text with keywords restored.
    """
    for idx, keyword in enumerate(keywords, start=1):
        pattern = re.compile(rf"__{idx}__")
        text = pattern.sub(keyword, text)
    return text


def normalize_text(text: str) -> str:
    """
    Performs basic normalization (lowercase, strip spaces).
    Args:
        text (str): Text to normalize.
    Returns:
        str: Normalized text.
    """
    return text.strip().lower()


def log_translation(
    original_text: str, translated_text: str, log_path: str = "translation_log.txt"
) -> None:
    """
    Appends original and translated text to a log file.

    Args:
        original_text (str): The original source text.
        translated_text (str): The translated output.
        log_path (str): Path to the log file (default: 'translation_log.txt').
    Returns:
        None
    Raises:
        IOError: If there is an issue writing to the log file.
    """
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write("Original:\n" + original_text + "\n")
        log_file.write("Translated:\n" + translated_text + "\n")
        log_file.write("-" * 40 + "\n")
