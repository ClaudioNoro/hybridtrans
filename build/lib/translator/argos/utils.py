import os
import argostranslate.package


def install_model(model_path: str) -> bool:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    try:
        argostranslate.package.install_from_path(model_path)
        print(f"Model installed from: {model_path}")
        return True
    except Exception as e:
        print(f"Error installing model: {e}")
        return False
