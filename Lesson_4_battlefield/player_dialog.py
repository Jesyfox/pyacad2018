__author__ = 'Bogdan.S'
from random import randint, choice
import json_bridge as jb


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


def side_builder(side):
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
    from battlefield import build_side

    res = {}
    while True:
        sides = int(input('How many sides will be fight?(2 - n): '))
        if sides >= 2:
            break

    for side in range(1, sides + 1):
        name = f'side {side}'
        res[name] = side_builder(side)

    print(f'your arrangement: {build_side(res)}')

    safe_pattern_dialog(res)
    return res


def safe_pattern_dialog(pattern):
    player_wish_to = {
        'yes': True,
        'no': False
    }
    safe = player_choice(player_wish_to, 'Do you with to safe it?')
    if player_wish_to[safe]:
        template_name = input('Enter the template name: ')
        template = {template_name: pattern}
        jb.safe_pattern(template)


def load_pattern_dialog():
    list_of_patterns = jb.get_available_patterns()

    choice = player_choice(list_of_patterns, 'Available patterns: ')

    return list_of_patterns[choice]


def delete_pattern_dialog():
    list_of_patterns = jb.get_available_patterns()

    template = player_choice(list_of_patterns, 'Available patterns: ')
    jb.delete_pattern(template)

    return None


def player_choice(choices: dict, message=''):
    choice_dict = dict(enumerate(choices.keys(), 1))

    print(message)

    for i, item in choice_dict.items():
        print(i, '-', item)
    while True:
        res = choice_dict.get(int(input('Enter the choice: ')))
        if res:
            break

    return res


def menu_dialog():
    main_menu = {
        'new template': builder_dialog,
        'load template': load_pattern_dialog,
        'delete template': delete_pattern_dialog
        }

    jump = player_choice(main_menu, 'Welcome to Battle Simulator 2019')
    while True:
        res = main_menu[jump]()
        if res:
            break

    return res


if __name__ == '__main__':
    print(menu_dialog())
