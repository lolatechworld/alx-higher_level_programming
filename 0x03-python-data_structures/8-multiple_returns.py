#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    length = len(sentence) if sentence else 0
    first_char = sentence[:1] if sentence else None
    return length, first_char
