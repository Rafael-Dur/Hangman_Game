
import unicodedata
import os

class WordsLoader:
    """Carga y limpia palabras desde el archivo wordsList.txt."""

    def __init__(self, filepath=None):
        if filepath is None:
            filepath = os.path.join(os.path.dirname(__file__), "wordsList.txt")
        self.filepath = filepath

    def load_words(self):
        """Lee el archivo y devuelve una lista de palabras limpias."""
        with open(self.filepath, encoding="utf-8") as file:
            content = file.read()

        words = []
        for raw_word in content.split(","):
            cleaned = self._clean_word(raw_word)
            if cleaned:
                words.append(cleaned)

        return words

    @staticmethod
    def _clean_word(word):
        """Convierte la palabra a minúsculas y elimina acentos y caracteres no a-z."""
        normalized = unicodedata.normalize("NFKD", word.strip().lower())
        return "".join(
            char for char in normalized
            if "a" <= char <= "z"
        )