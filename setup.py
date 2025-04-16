""" Setup script for the hybrid translation library using Google Translate and Argos Translate."""
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        try:
            subprocess.check_call([sys.executable, "postinstall.py"])
        except Exception as e:
            print(f"Post-install script failed: {e}")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='hybridlibtest',
    version='0.1.0',
    author='Claudio Filho',
    author_email='cg-filho@criticalsoftware.com',
    description='Hybrid translation library using Google Translate and Argos Translate',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["translator", "translator.*"]),
    install_requires=[
        "aiohappyeyeballs==2.6.1",
        "aiohttp==3.11.14",
        "aiosignal==1.3.2",
        "annotated-types==0.7.0",
        "anyio==3.7.1",
        "argostranslate==1.9.6",
        "astor==0.8.1",
        "astroid==3.3.9",
        "attrs==25.3.0",
        "autodocstrings==0.1.3",
        "autopep8==2.3.2",
        "black==25.1.0",
        "build==1.2.2.post1",
        "certifi==2025.1.31",
        "chardet==3.0.4",
        "charset-normalizer==3.4.1",
        "click==8.1.8",
        "colorama==0.4.6",
        "ctranslate2==4.5.0",
        "dill==0.3.9",
        "distro==1.9.0",
        "filelock==3.18.0",
        "flake8==7.1.2",
        "frozenlist==1.5.0",
        "fsspec==2025.3.0",
        "googletrans==4.0.0rc1",
        "h11==0.9.0",
        "h2==3.2.0",
        "hpack==3.0.0",
        "hstspreload==2025.1.1",
        "httpcore==0.9.1",
        "httpx==0.13.3",
        "hyperframe==5.2.0",
        "idna==2.10",
        "isort==6.0.1",
        "Jinja2==3.1.6",
        "jiter==0.9.0",
        "joblib==1.4.2",
        "markdown-it-py==3.0.0",
        "MarkupSafe==3.0.2",
        "mccabe==0.7.0",
        "mdurl==0.1.2",
        "mpmath==1.3.0",
        "multidict==6.2.0",
        "mypy-extensions==1.0.0",
        "networkx==3.4.2",
        "nltk==3.9.1",
        "numpy==2.2.4",
        "openai==0.28.1",
        "packaging==24.2",
        "pathspec==0.12.1",
        "platformdirs==4.3.7",
        "propcache==0.3.1",
        "protobuf==6.30.1",
        "pycodestyle==2.12.1",
        "pydantic==2.10.6",
        "pydantic_core==2.27.2",
        "pyflakes==3.2.0",
        "Pygments==2.19.1",
        "pylint==3.3.6",
        "pyproject_hooks==1.2.0",
        "PyYAML==6.0.2",
        "regex==2024.11.6",
        "requests==2.32.3",
        "rfc3986==1.5.0",
        "rich==13.9.4",
        "sacremoses==0.0.53",
        "sentencepiece==0.2.0",
        "shellingham==1.5.4",
        "six==1.17.0",
        "sniffio==1.3.1",
        "stanza==1.1.1",
        "sympy==1.13.1",
        "textblob==0.19.0",
        "tomlkit==0.13.2",
        "torch==2.6.0",
        "tqdm==4.67.1",
        "typer==0.15.2",
        "typing_extensions==4.12.2",
        "urllib3==2.3.0",
        "yarl==1.18.3"
    ],
    entry_points={
        "console_scripts": [
            "translate=translator.main:main",
            "install-argos-models=translator.utils.argos_installer:install_languages_from_config"  # install-argos-models is the command to run the installer
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    cmdclass={
        "install": PostInstallCommand,
    },
)
