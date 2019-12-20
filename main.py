from player import Player
from rules import Rules
from menu import Menu


def main():
    player1 = Player("Jan", "Kowalski")
    player2 = Player("Patryk", "Nowak")
    player3 = Player("Jakub", "Zawadzki")
    rules = Rules()
    menu = Menu(rules)
    index = 0

    print(menu.header)
    print(menu.adding_player_description)
    """Nie miałem lepszego pomysłu na dodawanie graczy :("""
    list_of_object_players = [player1, player2, player3]
    while index < rules.max_players:
        menu.adding_players(list_of_object_players[index])
        index += 1
    print(menu.number_of_dices)
    number_of_dices = int(input("Set the number of dices from keyboard "))
    menu.set_number_of_dices(number_of_dices)
    print(menu.throwing_quantity_description)
    print(menu.list_of_results())
    print(menu.get_a_winner())


if __name__ == '__main__':
    main()
