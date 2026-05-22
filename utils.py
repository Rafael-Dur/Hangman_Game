def create_hidden_word(word):
    """
    Convierte 'python' en ['_', '_', '_', '_', '_', '_']
    """
    return ["_"] * len(word)


def reveal_letters(word, hidden_word, letter):
    """
    Descubre las letras acertadas.
    """
    for index, char in enumerate(word):
        if char == letter:
            hidden_word[index] = letter

    return hidden_word


def is_word_completed(hidden_word):
    return "_" not in hidden_word