import random

from fileManager import WordsLoader

WORDS = WordsLoader().load_words()


def get_random_word():
    return random.choice(WORDS)


def create_hidden_word(word):
    """
    Convierte 'python' en ['_', '_', '_', '_', '_', '_']
    """
    return ["_"] * len(word)


def is_word_completed(hidden_word):
    return "_" not in hidden_word
