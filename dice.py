from abc import ABCMeta, abstractmethod
from random import shuffle
from typing import List


class Idice(metaclass=ABCMeta):
    @abstractmethod
    def throw_dice(self):
        pass


class Dice(Idice):
    def __init__(self):
        self.final_value: int = 0
        self.quantity_of_dices: int = 2

    def throw_dice(self) -> int:
        """
        Mój pomysł na zmiane rozkładu prawdopodobieństwa na kostce
        :return: wartość wyrzucona co jest zarazem liczbą punktów za dany rzut
        """
        throw_dice_list: List = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
        shuffle(throw_dice_list)
        self.final_value = throw_dice_list[0]
        print(self.final_value)
        return self.final_value
