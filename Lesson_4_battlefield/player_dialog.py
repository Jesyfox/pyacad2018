__author__ = 'Bogdan.S'
from random import randint, choice
from units import Unit
from unit_packs import Squad, Side


def squad_builder():
    army = randint(5, 10)
    to_squad = []
    for a in range(army):
        unit, kw = choice([
            ('soldier', {}),
            ('vehicle', {'operator': 'soldier', 'u_count': randint(1, 3)}),
        ])
        unit_obj = Unit.new(unit, **kw)

        to_squad.append(unit_obj)

    return Squad(to_squad)


def side_builder(side):
    res = []
    squads = int(input(f'How many squads for side {side}: '))
    for squad in range(1, squads + 1):
        res.append(squad_builder())
    return Side(res)


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
        if sides > 1:
            break

    for side in range(1, sides + 1):
        res[f'{side}'] = side_builder(side)
    return res


if __name__ == '__main__':
    print(builder_dialog())
