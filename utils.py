def reveal_letters(word, hidden_word, letter):
    """
    Descubre las letras acertadas.
    """
    for index, char in enumerate(word):
        if char == letter:
            hidden_word[index] = letter

    return hidden_word
