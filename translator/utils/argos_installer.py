import os
from argostranslate import package, translate
from translator.config import SUPPORTED_LANGUAGES


def install_argos_model(model_path: str) -> bool:
    """
    Installs an Argos Translate model from a .argosmodel file.

    Args:
        model_path (str): Path to the .argosmodel file.

    Returns:
        bool: True if installed successfully, False otherwise.
    """
    if not os.path.isfile(model_path):
        print(f"[ERROR] File not found: {model_path}")
        return False
    try:
        package.install_from_path(model_path)
        print(f"[INFO] Model installed successfully: {model_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to install model: {e}")
        return False


def uninstall_argos_model(model_name: str) -> bool:
    """
    Uninstalls an Argos Translate model by name.

    Args:
        model_name (str): Name of the model to uninstall.

    Returns:
        bool: True if uninstalled successfully, False otherwise.
    """
    try:
        package.uninstall(model_name)
        print(f"[INFO] Model uninstalled successfully: {model_name}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to uninstall model: {e}")
        return False


def get_installed_argos_models() -> list:
    """
    Returns a list of installed Argos Translate models.

    Returns:
        list: List of installed model names.
    """
    return package.get_installed_packages()


def get_available_argos_models() -> list:
    """
    Returns a list of available Argos Translate models.

    Returns:
        list: List of available model names.
    """
    return package.get_available_packages()


def update_argos_package_index() -> None:
    """Updates the Argos Translate package index."""
    package.update_package_index()


def install_language_models(
    supported_languages: dict,
) -> None:  # wtf is pylance yapping about
    """Installs Argos Translate language models for the specified language codes.
    Args:
        supported_languages (dict): A dictionary mapping language codes to language names.
    """
    # Update the package index to get the latest models
    update_argos_package_index()
    # Get the list of available models
    available_packages = get_available_argos_models()

    for from_code in supported_languages:
        for to_code in supported_languages:
            if from_code != to_code:
                # Find the package for the specified languages
                package_to_install = next(
                    (
                        pkg
                        for pkg in available_packages
                        if pkg.from_code == from_code and pkg.to_code == to_code
                    ),
                    None,
                )
                if package_to_install:
                    # Download and install the package
                    install_argos_model(package_to_install.download())
                    print(
                        f"Installed translation model from {supported_languages[from_code]} to {supported_languages[to_code]}"
                    )


def install_languages_from_config() -> None:
    """
    Install Argos Translate language models based on the supported languages
    defined in the configuration file.
    """
    print("Updating Argos Translate package index...")
    package.update_package_index()

    available_packages = package.get_available_packages()
    installed_codes = [lang.code for lang in translate.get_installed_languages()]  # type: ignore
    total_installed = 0

    for pkg in available_packages:
        from_code = pkg.from_code
        to_code = pkg.to_code

        if from_code in SUPPORTED_LANGUAGES and to_code in SUPPORTED_LANGUAGES:
            if from_code not in installed_codes or to_code not in installed_codes:
                print(f"Installing model: {from_code} → {to_code}")
                package.install_from_path(pkg.download())
                total_installed += 1

    if total_installed == 0:
        print("All required Argos models are already installed.")
    else:
        print(f"Installed {total_installed} model(s).")
