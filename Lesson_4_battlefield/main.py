__author__ = 'Bogdan.S'
from battlefield import Battlefield


def main():

    print("""\tWelcome to "Battle Simulator 2019"
           Available Units:
          "-=/[-0, -0]\\" - a Vehicle with operators
          \t "-0" -  a Soldier""")

    game = Battlefield()

    print('Your arrangement is: \n', game)

    game.start()


if __name__ == '__main__':
    main()
