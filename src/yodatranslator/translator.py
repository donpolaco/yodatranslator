"""Simple Yoda-Translator module by donpolaco

It's a simple module for translating English into Yoda-language.
Training project illustrates how to use setup.cfg and CLI scripts.
"""

import requests


def translate(original_text: str) -> str:
    """Translate English to Yoda language.

    Translated sentence is returned and printed.

    Args:
        original_text (str): English text to translate into Yoda language

    Returns:
        str: text translated in Yoda-language

    Raises:
        RuntimeError: if translation is impossible due to any connection problem or bad response.

    """
    try:
        req = requests.post("https://api.funtranslations.com/translate/yoda.json", json={'text': original_text})
        translated_text = req.json()["contents"]["translated"]
        return translated_text
    except Exception:
        err_msg = f"Sorry cannot translate your sentence. Tray again later!\n{req.text}"
        raise RuntimeError(err_msg)
