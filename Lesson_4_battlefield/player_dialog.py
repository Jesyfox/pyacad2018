__author__ = 'Bogdan.S'
from random import randint, choice
import json_bridge as JB


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


def safe_dialog():
    safe_menu = {
        'yes': True,
        'no': False
    }


def player_choice(choices: dict):
    choice_dict = dict(enumerate(choices.keys(), 1))
    for i, item in choice_dict.items():
        print(i, '-', item)
    return choice_dict.get(int(input('Enter the choice: ')), 'wrong choice')


def menu_dialog():
    main_menu = {
        'new template': builder_dialog,
        'load template': JB.get_available_patterns
        }

    jump = player_choice(main_menu)
    return main_menu[jump]()


if __name__ == '__main__':
    print(menu_dialog())
