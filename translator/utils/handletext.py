"""Text handling utilities for translation tasks."""
import json
import re
from typing import List
from textblob import TextBlob


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


# averiguar max_sentences, multithreading em menos sentencas, return com joins


def define_keywords(text: str, pattern: str) -> List[str]:
    """
    Extracts keywords from text using a regular expression pattern.

    Args:
        text (str): The input text to search in.
        pattern (str): A regex pattern to match keywords (e.g., r"[A-Z]{2,}" \
            for uppercase keywords,
             r"\{.*?\}" for keywords surrounded by curly braces:{example}).

    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    matches = re.findall(pattern, text)
    # Remove duplicates while preserving order
    return list(dict.fromkeys(matches))


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


# mais liberdade keyword {[]}


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
    Replaces numbered placeholders (__1__, __2__, ...) \
        with the original keywords.

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


# elborar


def normalize_text(text: str) -> str:
    """
    Performs basic normalization (lowercase, strip spaces).
    Args:
        text (str): Text to normalize.
    Returns:
        str: Normalized text.
    """
    return text.strip()


def log_translation(
    original_text: str, translated_text: str,
    log_path: str = "translation_log.txt"
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


def json_to_dict(json_string: str) -> dict:
    """
    Converts a JSON string to a Python dictionary.
    Args:
        json_string (str): The JSON string to convert.
    Returns:
        dict: The converted dictionary.
    Raises:
        json.JSONDecodeError: If the JSON string is invalid.
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}") from e


def dict_to_list(data_dict: dict) -> List[str]:
    """
    Converts a dictionary to a list of strings in the format "key: value".
    Args:
        data_dict (dict): The dictionary to convert.
    Returns:
        List[str]: The converted list of strings.
    """
    return [f"{key}: {value}" for key, value in data_dict.items()]

# regex function to extract keywords from text


def allcaps_keywords(text: str) -> List[str]:
    """
    Extracts all uppercase keywords from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique uppercase keywords found in the text.
    """
    pattern = r"\b[A-Z]{2,}\b"
    return define_keywords(text, pattern)


def curly_braces_keywords(text: str) -> List[str]:
    """
    Extracts keywords surrounded by curly braces from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    pattern = r"\{.*?\}"
    return define_keywords(text, pattern)


def brackets_keywords(text: str) -> List[str]:
    """
    Extracts keywords surrounded by square brackets from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    pattern = r"\[.*?\]"
    return define_keywords(text, pattern)


def parentheses_keywords(text: str) -> List[str]:
    """
    Extracts keywords surrounded by parentheses from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    pattern = r"\(.*?\)"
    return define_keywords(text, pattern)


def barackets_keywords(text: str) -> List[str]:
    """
    Extracts keywords surrounded by angle brackets from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    pattern = r"<.*?>"
    return define_keywords(text, pattern)


def slash_keywords(text: str) -> List[str]:
    """
    Extracts keywords surrounded by slashes from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    pattern = r"/.*?/"
    return define_keywords(text, pattern)


def backslash_keywords(text: str) -> List[str]:
    """
    Extracts keywords surrounded by backslashes from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    pattern = r"\\.*?\\"
    return define_keywords(text, pattern)


def underscore_keywords(text: str) -> List[str]:
    """
    Extracts keywords surrounded by underscores from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    pattern = r"_(.*?)_"
    return define_keywords(text, pattern)


def semicolon_keywords(text: str) -> List[str]:
    """
    Extracts keywords surrounded by semicolons from the text.
    Args:
        text (str): The input text to search in.
    Returns:
        List[str]: A list of unique keywords found in the text.
    """
    pattern = r";(.*?);"
    return define_keywords(text, pattern)
