import random

WORDS = [
    "python",
    "computadora",
    "programacion",
    "algoritmo",
    "variable",
    "funcion"
]

def get_random_word():
    return random.choice(WORDS)