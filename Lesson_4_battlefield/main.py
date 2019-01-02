__author__ = 'Bogdan.S'
from battlefield import Battlefield, build_side
from player_dialog import builder_dialog


def main():
    battle_arrangement = build_side(builder_dialog())
    game = Battlefield(battle_arrangement)

    print('Your arrangement is: \n', game)

    game.start()


if __name__ == '__main__':
    main()
