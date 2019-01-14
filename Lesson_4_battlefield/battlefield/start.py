__author__ = 'Bogdan.S'
from .battlefield import Battlefield, build_side
from .player_dialog import menu_dialog


def main():
    try:
        battle_arrangement = build_side(menu_dialog())
        game = Battlefield(battle_arrangement)

        print('Battle is starting!')
        game.start()
    except KeyboardInterrupt:
        print('\nGood bye!')
