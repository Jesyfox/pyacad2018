import json
from random import randint, choice
from units import Unit
from unit_packs import Squad, Side

FILE_NAME = 'sides_template.json'


def construct_sides(file=FILE_NAME):
    pattern = json.load(open(file))
    sides = []

    for side in pattern.keys():
        squad_list = []
        for squad in pattern[side].keys():
            unit_list = []
            for unit in pattern[side][squad]:
                name, kw = unit
                if kw:
                    min_oper, max_oper = kw['u_count']
                    kw['u_count'] = randint(min_oper, max_oper)
                unit_list.append(Unit.new(name, **kw))
            squad_list.append(Squad(unit_list))
        sides.append(Side(squad_list))

    return sides


if __name__ == '__main__':
    test = {
        'side_1': {
            'squad_1': (
                ('soldier', {}),
                ('vehicle', {'operator': 'soldier', 'u_count': (1, 3)})
            ),
            'squad_2': (
                ('soldier', {}),
                ('vehicle', {'operator': 'soldier', 'u_count': (1, 3)})
            ),
        },
        'side_2': {
            'squad_1': (
                ('soldier', {}),
                ('vehicle', {'operator': 'soldier', 'u_count': (1, 3)})
            )
        }
    }

    json.dump(test, open(FILE_NAME, 'w'), indent=4)
    print(construct_sides())
