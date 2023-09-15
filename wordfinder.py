"""Word Finder: finds random words from a dictionary."""


import random


class WordFinder:
    """Find random words from a dictionary.
    """
    def __init__(self, file_path: str) -> None:
        with open(file_path) as words_file:
            self.words = [word.strip() for word in words_file]
    def random(self) -> str:
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Find random words from a dictionary. Aware of handling comments and non-words
    >>> word_finder = SpecialWordFinder('./words.txt')
    ...
    >>> exist = word_finder.random() in word_finder.words
    >>> exist
    True
    """
    def __init__(self, file_path: str) -> None:
        with open(file_path) as words_file:
            self.words = [word.strip() for word in words_file if not word.startswith("#") or word == '']

