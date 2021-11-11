#! /urs/bin/env python
"""Simple Yoda-Translator by donpolaco

It's a simple CLI script for translating English into Yoda-language.
Training project illustrates how to use setup.cfg and CLI scripts.
"""

import argparse

from .translator import translate


def arg_parser() -> dict:
    """Parse CLI arguments.

    Returns:
        dict: parsed arguments in dictionary
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("words", nargs="+", type=str, help="Sentence that will be translated")
    return parser.parse_args().__dict__


def main():
    """Main function for running from CLI.

    """
    print("Simple Yoda-Translator by donpolaco\n")
    words = arg_parser()["words"]
    original_text = " ".join(words)
    try:
        translated_text = translate(original_text)
    except RuntimeError as error:
        print(error)
        return 1
    else:
        print(f"YOU SAID: {original_text}\n\nYODA WOULD SAY: {translated_text}\n")
        return 0


if __name__ == '__main__':
    main()
