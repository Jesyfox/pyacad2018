__author__ = 'Bogdan.S'
from .unit.units import Unit
from .unit.unit_packs import Squad, Side


class Battlefield:

    def __init__(self, sides):
        self.sides = sides
        self.is_running = True

    def __repr__(self):
        return str(self.sides)

    def update(self):
        to_delete = []
        for num, side in enumerate(self.sides):
            if not self.sides[num].is_alive:
                to_delete.append(num)

        for key in to_delete:
            self.sides.pop(key)

    def start(self):
        from time import time
        wait_seconds = 4
        timer = time()
        while self.is_running:
            self.update()

            for side, side_obj in enumerate(self.sides):
                enemy_sides_alive = [self.sides[i] for i, e_side in enumerate(self.sides)
                                     if i != side and self.sides[i].is_alive]
                if enemy_sides_alive:
                    side_obj.attack(enemy_sides_alive)
                    side_obj.update()
                else:
                    self.is_running = False

            if time() - timer >= wait_seconds:
                timer = time()
                print('=' * 10)
                print(self)

        self.update()
        print(f'Winner!\n{self.sides}')


def build_side(pattern: dict):
    return [
        Side([
            Squad([
                Unit.new(name, **kw)
                for name, kw in units
            ])
            for units in squads
        ], name=side_name)
        for side_name, squads in pattern.items()
    ]


if __name__ == '__main__':
    test = {
        'test_template_1': {
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
        },

    }
    template = build_side(test['test_template_1'])
    game = Battlefield(template)
    game.start()
