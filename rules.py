from abc import ABCMeta, abstractmethod
from typing import List
from dice import Dice
from player import Player


class IRules(metaclass=ABCMeta):
    @abstractmethod
    def quantity_of_throws_per_player(self, max_throws):
        pass

    @abstractmethod
    def set_quantity_of_players(self, max_players):
        pass

    @abstractmethod
    def add_player(self, player):
        pass

    @abstractmethod
    def set_quantity_of_dices(self, quantity_of_dices):
        pass

    @abstractmethod
    def select_a_winner(self, player_list):
        pass

    @abstractmethod
    def show_results(self, player_list):
        pass


class TooManyPlayersError(Exception):
    """Raises when there is too many players in the game"""


class Rules(IRules):
    def __init__(self):
        self.player_list: List = []
        self.throw: int = 1
        self.max_players: int = 3
        self.max_throws: int = 20
        self.dice_throw: Dice = Dice()
        self.winner_list: List = []
        self.winner: Player
        self.draw_pointer: bool = False

    def quantity_of_throws_per_player(self, max_throws: int):
        """Nieużywane przeze mnie ustawianie max_throws w mainie, mógłbym dodać
           tą opcje ale nie wiedziałem czy nie lepiej po prostu zmieniać powyżej
           w zależności od podpunktu zadania"""
        self.max_throws = max_throws

    def set_quantity_of_players(self, max_players: int):
        """Podobnie jak powyżej"""
        self.max_players = max_players

    def add_player(self, player: Player):
        """Warunek w mainie sprawia, że wyjątek się nigdy nie wywoła ale jest
           to dodatkowe zabezpieczenie"""
        self.player_list.append(player)
        if len(self.player_list) > self.max_players:
            raise TooManyPlayersError("Too many players")

    def set_quantity_of_dices(self, quantity_of_dices):
        self.dice_throw.quantity_of_dices = quantity_of_dices

    def select_a_winner(self, player_list):
        """Ponieważ np gracz mający 119 punktów i rzcuający '6' zdobywa łącznie 125 punktów
           czyli przekracza liczbę 120 i jest zwycięzcą"""
        winner_set = {120, 121, 122, 123, 124, 125}
        for player in player_list:
            while self.throw < (self.max_throws * self.dice_throw.quantity_of_dices) + 1:
                print(f"{player.introduce} throw:")
                #cheated_points = int(input("Enter how many points you throw "))
                player.add_points(self.dice_throw.throw_dice())
                #player.set_points(cheated_points)
                player.quantity_of_throws = self.throw
                if player.points in winner_set:
                    self.winner_list.append(player)
                    break
                self.throw += 1
            self.throw = 1

        if self.winner_list:
            """Sortowanie listy obiektów: Player według klucza 'quantity_of_dices'"""
            self.winner_list.sort(key=lambda player: player.quantity_of_throws)
            self.winner = self.winner_list[0]
            self.winner.points = 120
            """Remis gdy wiecej niz jedna osoba ma najmniejsza ilosc rzutów
               (w tym samym rzucie co najmniej dwóch graczy zdobyło 120 punktów)"""
            if self.winner_list[0].quantity_of_throws == self.winner_list[1].quantity_of_throws:
                self.draw_pointer = True

        else:
            """Sortowanie listy obiektów: Player według klucza 'points'"""
            self.player_list.sort(key=lambda player: player.points, reverse=True)
            self.winner = self.player_list[0]
            """Remis gdy co najmniej dwie osoby mają najwieksza ilosc punktów"""
            if self.player_list[0].points == self.player_list[1].points:
                self.draw_pointer = True

    def show_results(self, player_list):
        if self.draw_pointer is True:
            return "Its a draw!"
        else:
            return f"The winner is {self.winner.introduce} with the {self.winner.points} number of points. "
