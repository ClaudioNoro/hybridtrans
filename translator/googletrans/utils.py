import os
# legacy, no longer used and should be removed in the future


def read_file(file_path) -> str:
    """Reads the content of a text file.
    Args:
        file_path (str): Path to the text file.
    Returns:
        str: Content of the file.
    Raises:
            FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def process_keywords(keywords):
    """Processes a list of keywords (e.g., removes duplicates, trims whitespace).
    Args:
        keywords (list): List of keywords.
    Returns:
            list: Processed list of keywords."""
    return list(set(keyword.strip() for keyword in keywords))


def log_translation(input_text, translated_text,
                    log_file="translation_log.txt"):
    """Logs the original and translated text to a file."""
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(
            f"Original: {input_text}\nTranslated: {translated_text}\n\n")
