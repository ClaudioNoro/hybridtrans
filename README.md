# 🌍 HybridLibTest

**HybridLibTest** is a multilingual translation library for Python that combines the power of both **Google Translate** (online) and **Argos Translate** (offline). It automatically selects the best translation engine based on connectivity or developer preference.

---

## 🚀 Features

- **Hybrid Translation**: Choose between Google Translate, Argos Translate, or automatic detection.
- **Online Mode**: Uses `googletrans` to access Google Translate services.
- **Offline Mode**: Uses `argostranslate` and pre-installed language models.
- **Keyword Protection**: Prevent specific keywords from being translated.
- **Smart Segmentation**: Splits long texts for improved translation accuracy.
- (BETA) **Unit tested** and ready for integration in larger projects. 
- Easy to use via **CLI or as a Python package**.

---

## 📦 Installation

After building the wheel:

```bash
pip install dist/hybridlibtest-0.1.0-py3-none-any.whl
