def show_hidden_word(hidden_word):
    print(" ".join(hidden_word))


def show_attempts(attempts):
    print(f"Intentos restantes: {attempts}")


def show_used_letters(letters):
    print("Letras usadas:", ", ".join(sorted(letters)))


def show_victory(word):
    print(f"\n¡Ganaste! La palabra era '{word}'")


def show_defeat(word):
    print(f"\nPerdiste. La palabra era '{word}'")