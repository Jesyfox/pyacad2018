__author__ = 'Bogdan.S'
from random import randint, choice


def squad_builder():
    army = randint(5, 10)
    res = []
    for a in range(army):
        unit, kw = choice([
            ('soldier', {}),
            ('vehicle', {'operator': 'soldier', 'u_count': randint(1, 3)}),
        ])
        unit_obj = (unit, kw)

        res.append(unit_obj)

    return res


def side_builder(side, name):
    res = []
    squads = int(input(f'How many squads for side {side}: '))
    for squad in range(1, squads + 1):
        res.append(squad_builder())

    return res


def builder_dialog():
    """
    start player dialog:
        the number of armies (2 <= n)
        the number of squads per army (2 <= n)
        the number of units per squad (5 <= n <= 10)

    its all returns the dict file
    """
    res = {}
    while True:
        sides = int(input('How many sides will be fight?(2 - n): '))
        if sides >= 2:
            break

    for side in range(1, sides + 1):
        name = f'side {side}'
        res[name] = side_builder(side, name)
    return res


if __name__ == '__main__':
    print(builder_dialog())
