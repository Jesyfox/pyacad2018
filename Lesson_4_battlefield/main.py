__author__ = 'Bogdan.S'
from battlefield import Battlefield
from player_dialog import builder_dialog


def main():

    print("""\tWelcome to "Battle Simulator 2019"
           Available Units:
          "-=/[-0, -0]\\" - a Vehicle with operators
          \t "-0" -  a Soldier""")

    game = Battlefield(builder_dialog())

    print('Your arrangement is: \n', game)

    game.start()


if __name__ == '__main__':
    main()
