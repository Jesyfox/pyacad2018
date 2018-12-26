import json
from random import randint
from units import Unit
from unit_packs import Squad, Side

FILE_NAME = 'sides_template.json'


def construct_sides(file=FILE_NAME):
    with open(file) as f:
        pattern = json.load(f)

    return [
        Side([
            Squad([
                Unit.new(name, **kw)
                for name, kw in units.items()
            ])
            for squad_name, units in squads.items()
        ])
        for side_name, squads in pattern.items()
    ]


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
