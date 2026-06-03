from words import create_hidden_word, get_random_word, is_word_completed
from utils import (
    reveal_letters
)
from userInterface import (
    show_hidden_word,
    show_attempts,
    show_used_letters,
    show_victory,
    show_defeat
)


MAX_ATTEMPTS = 6


def play_game():

    word = get_random_word()

    hidden_word = create_hidden_word(word)

    attempts = MAX_ATTEMPTS

    used_letters = set()

    while attempts > 0:

        print("\n----------------")

        show_hidden_word(hidden_word)
        show_attempts(attempts)
        show_used_letters(used_letters)

        letter = input("Ingresa una letra: ").lower()

        if len(letter) != 1:
            print("Debes ingresar una sola letra.")
            continue

        if letter in used_letters:
            print("Ya utilizaste esa letra.")
            continue

        used_letters.add(letter)

        if letter in word:
            reveal_letters(word, hidden_word, letter)

            if is_word_completed(hidden_word):
                show_victory(word)
                return

        else:
            attempts -= 1
            print("Letra incorrecta.")

    show_defeat(word)
