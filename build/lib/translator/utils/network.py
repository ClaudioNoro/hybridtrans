import requests


def is_connected(timeout=3) -> bool:
    """Checks internet connection.
    Args:
        timeout (int): Timeout in seconds for the connection check.
            Default is 3 seconds.
    Returns: bool:
        - True if connected,
        - False otherwise.
    Raises:
        - requests.RequestException: If the request fails.
    Example:
        >>> is_connected()
            True
        >>> is_connected(timeout=9999)
            False
    """
    try:
        requests.get("https://www.google.com", timeout=timeout) #hardcoded, virar variavel global
        return True
    except requests.RequestException:
        return False
