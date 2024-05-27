#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.")
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace all instances of '?', '!', and '.' with a unique character ('|') to split the string
        modified_str = self.value.replace('?', '|').replace('!', '|').replace('.', '|')
        # Split the modified string based on '|' and filter out empty strings
        sentences = [sentence for sentence in modified_str.split('|') if sentence.strip()]
        return len(sentences)