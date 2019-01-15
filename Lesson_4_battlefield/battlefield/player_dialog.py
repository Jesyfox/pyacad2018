__author__ = 'Bogdan.S'
from random import randint, choice
from . import json_bridge as jb
from .battlefield import build_side
from .logger_battlefield import logger


def squad_builder():
    logger.debug('# building squad')
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
    logger.debug('# building side')
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
        res[name] = side_builder(side)

    print(f'your arrangement: {build_side(res)}')
    safe_pattern_dialog(res)
    return res


def safe_pattern_dialog(pattern):
    player_wish_to = {
        'yes': True,
        'no': False
    }
    safe = player_choice(player_wish_to, 'Do you with to safe it?',
                         back_possible=False)
    if player_wish_to[safe]:
        logger.debug('# saving pattern')
        template_name = dialog_input('Enter the template name: ')
        template = {template_name: pattern}
        jb.safe_pattern(template)


def available_patterns_dialog():
    list_of_patterns = jb.get_available_patterns()
    for pattern in list_of_patterns:
        side_pattern = jb.get_side_pattern(pattern)
        print(f'\n"{pattern}" ->', build_side(side_pattern))

    chosen = player_choice(list_of_patterns, 'Available patterns: ')
    if not chosen:
        return None
    else:
        return chosen


def load_pattern_dialog():
    logger.debug('# loading pattern')
    list_of_patterns = jb.get_available_patterns()
    chosen_pattern = available_patterns_dialog()
    if chosen_pattern:
        return list_of_patterns[chosen_pattern]


def delete_pattern_dialog():
    logger.debug('# deleting pattern')
    chosen_pattern = available_patterns_dialog()
    jb.delete_pattern(chosen_pattern)

    return None


def player_choice(choices: dict, message='', back_possible=True):
    choice_dict = dict(enumerate(choices.keys(), 1))
    if back_possible:
        choice_dict.update({0: None})

    print(message)

    for i, item in choice_dict.items():
        print(i, '-', item)
    res = choice_dict.get(int(dialog_input('Enter the choice: ')))

    return res


def dialog_input(message):
    not_available_inputs = ['', ]
    while True:
        res = input(message)
        if res in not_available_inputs:
            continue
        else:
            return res


def menu_dialog():
    main_menu = {
        'new template': builder_dialog,
        'load template': load_pattern_dialog,
        'delete template': delete_pattern_dialog
        }
    while True:
        jump = player_choice(main_menu, '\nWelcome to Battle Simulator 2019')
        if not jump:
            raise KeyboardInterrupt
        logger.debug(f'# player choose is {jump}')

        res = main_menu[jump]()
        if res:
            break
    return res


if __name__ == '__main__':
    print(menu_dialog())
