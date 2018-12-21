__author__ = 'Bogdan.S'
from random import randint, choice
from units import Soldier, Vehicle
from unit_packs import Squad


def squad_builder():
    army = randint(5, 10)
    to_squad = []
    for a in range(army):
        operators = [Soldier() for _ in range(randint(1, 3))]
        unit = choice([Soldier(), Vehicle(operators)])
        to_squad.append(unit)
    return Squad(to_squad)


def side_builder(side):
    res = {}
    squads = int(input(f'How many squads for side {side}: '))
    for squad in range(1, squads + 1):
        res[f'Squad {squad}'] = squad_builder()
    return res


def battle_builder():
    """
    start player dialog:
        the number of armies (2 <= n)
        the choice of attack strategy per army  (pick |random|weakest|strongest| army)
        the number of squads per army (2 <= n)
        the number of units per squad (5 <= n <= 10)

    its all returns the dict file
    """
    res = {}
    sides = int(input('How many sides will be fight?: '))
    for side in range(1, sides + 1):
        res[f'Side {side}'] = side_builder(side)
    return res


if __name__ == '__main__':
    print(battle_builder())
