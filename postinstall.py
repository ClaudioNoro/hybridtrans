# postinstall.py
import subprocess
import sys


def download_textblob_corpora():
    """Download the necessary corpora for TextBlob.
    This function uses subprocess to run the TextBlob download command
    in a separate process. It handles any exceptions that may occur
    during the download process.
    It is recommended to run this function after installing the package
    to ensure that all necessary corpora are available for use.
    This function is called in the post-installation script of the package.
    It is important to note that this function may require internet access
    to download the corpora, so ensure that the machine running this script
    has internet connectivity.
    """
    try:
        print("Downloading TextBlob corpora...")
        subprocess.check_call([sys.executable, "-m", "textblob.download_corpora"])
        print("TextBlob corpora downloaded.")
    except Exception as e:
        print(f"[ERROR] Failed to download TextBlob corpora: {e}")


if __name__ == "__main__":
    download_textblob_corpora()
