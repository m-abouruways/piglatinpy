from cmath import phase

from src.error import PigLatinError


class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase
    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase
    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        vowels = "aeiou"

        if self.phrase[0] in vowels:

            if self.phrase.endswith("y"):
                return self.phrase + "nay"

            if self.phrase[-1] in vowels:
                return self.phrase + "yay"

            return self.phrase + "ay"

        index = 0

        while index < len(self.phrase) and self.phrase[index] not in vowels:
            index += 1

        return self.phrase[index:] + self.phrase[:index] + "ay"