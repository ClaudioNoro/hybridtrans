"""Text handling utilities for translation tasks."""

import json
import re
from typing import List, Literal
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

def extract_keywords(text: str, method: Literal[
    "allcaps", "curly", "brackets", "parentheses", "barackets", "slash",
    "underscore", "semicolon", "pipe", "percent", "dollar", "ampersand", "at",
    "caret", "exclamation", "tilde", "hash", "backtick", "plus", "minus",
    "dot", "comma", "question", "asterisk", "double_quotes", "single_quotes",
    "curly_quotes"
]) -> List[str]:
    """
    Extracts keywords from text based on the selected method.
    Args:
        text (str): The input text to search in.
        method (str): The method for keyword extraction. Options include:
            - "allcaps": Extracts all-uppercase words.
            - "curly": Extracts text within curly braces.
            - "brackets": Extracts text within square brackets.
            - "parentheses": Extracts text within parentheses.
            - "barackets": Extracts text within angle brackets.
            - "slash": Extracts text within slashes.
            - "underscore": Extracts text within underscores.
            - "semicolon": Extracts text within semicolons.
            - "pipe": Extracts text within pipes.
            - "percent": Extracts text within percent signs.
            - "dollar": Extracts text within dollar signs.
            - "ampersand": Extracts text within ampersands.
            - "at": Extracts text within at symbols.
            - "caret": Extracts text within caret symbols.
            - "exclamation": Extracts text between exclamation marks.
            - "tilde": Extracts text within tildes.
            - "hash": Extracts text within hash symbols.
            - "backtick": Extracts text within backticks.
            - "plus": Extracts text between plus signs.
            - "minus": Extracts text between minus signs.
            - "dot": Extracts text between dots.
            - "comma": Extracts text between commas.
            - "question": Extracts text between question marks.
            - "asterisk": Extracts text between asterisks.
            - "double_quotes": Extracts text within double quotes.
            - "single_quotes": Extracts text within single quotes.
            - "curly_quotes": Extracts text within curly quotes.
        Returns:
            List[str]: A list of unique keywords found in the text.
    """
    pattern_map = {
        "allcaps": r"\b[A-Z]{2,}\b",
        "curly": r"\{.*?\}",
        "brackets": r"\[.*?\]",
        "parentheses": r"\(.*?\)",
        "barackets": r"<.*?>",
        "slash": r"/.*?/",
        "underscore": r"_.*?_",
        "semicolon": r";.*?;",
        "pipe": r"\|.*?\|",
        "percent": r"%.*?%",
        "dollar": r"\$.*?\$",
        "ampersand": r"&.*?&",
        "at": r"@.*?@",
        "caret": r"\^.*?\^",
        "exclamation": r"!.+?!",
        "tilde": r"~.*?~",
        "hash": r"#.*?#",
        "backtick": r"`.*?`",
        "plus": r"\+.*?\+",
        "minus": r"-.*?-",
        "dot": r"\..*?\.",
        "comma": r",.*?,",
        "question": r"\?.*?\?",
        "asterisk": r"\*.*?\*",
        "double_quotes": r"\".*?\"",
        "single_quotes": r"'.*?'",
        "curly_quotes": r"[“”](.*?)[“”]",
    }

    pattern = pattern_map.get(method)
    if not pattern:
        raise ValueError(f"Invalid keyword extraction method: {method}")
    
    return define_keywords(text, pattern)
