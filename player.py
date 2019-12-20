from abc import ABCMeta, abstractmethod
from typing import Set


class IPlayer(metaclass=ABCMeta):
    @abstractmethod
    def introduce(self):
        pass

    @abstractmethod
    def add_points(self, points):
        pass

    @abstractmethod
    def set_points(self, number_of_points):
        pass


class Player(IPlayer):
    def __init__(self, first_name: str = "Unknown first name", last_name: str = "Unknown last name"):
        self.first_name = first_name
        self.last_name = last_name
        self.points: int = 0
        self.quantity_of_throws: int

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def introduce(self) -> str:
        return f"Player {self.first_name} {self.last_name}"

    def add_points(self, points):
        self.points += points

    def set_points(self, number_of_points):
        """
        Metoda do oszukiwania, odkomentowanie jej w 'rules' sprawi, że można wpisać inną niż
        wyrzucona wartość punktów
        """
        possible_points: Set = {1, 2, 3, 4, 5, 6}
        if number_of_points in possible_points:
            self.points += number_of_points

