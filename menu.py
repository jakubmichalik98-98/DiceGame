from abc import ABCMeta, abstractmethod
from rules import Rules
from player import Player


class IMenu(metaclass=ABCMeta):
    @abstractmethod
    def header(self):
        pass

    @abstractmethod
    def adding_player_description(self):
        pass

    @abstractmethod
    def adding_players(self, player1):
        pass

    @abstractmethod
    def number_of_dices(self):
        pass

    @abstractmethod
    def set_number_of_dices(self, quantity_of_dices):
        pass

    @staticmethod
    def list_of_results():
        pass

    @abstractmethod
    def get_a_winner(self):
        pass


class Menu(IMenu):
    def __init__(self, first_version: Rules):
        self.first_version = first_version

    @property
    def header(self):
        return "Welcome to the game! Lets get ready to rumble!?"

    @property
    def adding_player_description(self):
        return f"Add player (you cannot add more than {self.first_version.max_players}):"

    def adding_players(self, player1: Player):
        self.first_version.add_player(player1)

    @property
    def number_of_dices(self):
        return f"Set the number of dices: "

    def set_number_of_dices(self, quantity_of_dices):
        self.first_version.set_quantity_of_dices(quantity_of_dices)

    @property
    def throwing_quantity_description(self):
        return f"All players have {self.first_version.max_throws} throws"

    @staticmethod
    def list_of_results():
        return "List of results is: \n"

    def get_a_winner(self):
        self.first_version.select_a_winner(self.first_version.player_list)
        return self.first_version.show_results(self.first_version.player_list)


