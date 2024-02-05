#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """
    text_indentation
    """
    flag = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if flag and text[i].isspace():
            continue
        elif text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print("\n")
            flag = True
        else:
            print(text[i], end="")
            flag = False