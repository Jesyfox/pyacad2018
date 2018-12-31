import json
from random import randint
from units import Unit
from unit_packs import Squad, Side

FILE_NAME = 'sides_template.json'


def build_side_pattern_from_file(file=FILE_NAME, template='test_template'):
    with open(file) as f:
        pattern = json.load(f)

    return [
        Side([
            Squad([
                Unit.new(name, **kw)
                for name, kw in units
            ])
            for units in squads
        ], name=side_name)
        for side_name, squads in pattern[template].items()
    ]


if __name__ == '__main__':
    test = {
        'test_template': {
            'side_1': [
                [
                    ('soldier', {}),
                    ('vehicle', {'operator': 'soldier', 'u_count': 1}),
                    ('soldier', {}),
                    ('soldier', {})
                ],
                [
                    ('soldier', {}),
                    ('vehicle', {'operator': 'soldier', 'u_count': 2})
                ],
            ],
            'side_2': [
                [
                    ('soldier', {}),
                    ('vehicle', {'operator': 'soldier', 'u_count': 3})
                ]
            ]
        }
    }

    json.dump(test, open(FILE_NAME, 'w'), indent=4)
    print(build_side_pattern_from_file())
