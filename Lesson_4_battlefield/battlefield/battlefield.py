__author__ = 'Bogdan.S'
from .unit.units import Unit
from .unit.unit_packs import Squad, Side
from .logger_battlefield import logger


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

        if to_delete:
            logger.debug(f'{len(to_delete)} side out')

        for key in to_delete:
            self.sides.pop(key)

    def side_attack(self, side_obj, enemy_sides):
        if enemy_sides:
            side_obj.attack(enemy_sides)
            side_obj.update()
        else:
            logger.debug('# battle is over')
            self.is_running = False

    def filter_enemy_sides(self, my_side):
        return [self.sides[i] for i, e_side in enumerate(self.sides)
                if i != my_side and self.sides[i].is_alive]

    def start(self):
        from time import time
        wait_seconds = 4
        timer = time()
        logger.debug('# starting battle!')
        while self.is_running:
            self.update()

            for side, side_obj in enumerate(self.sides):
                enemy_sides_alive = self.filter_enemy_sides(side)
                self.side_attack(side_obj, enemy_sides_alive)

            if time() - timer >= wait_seconds:
                timer = time()
                print('=' * 30)
                print(self)

        self.update()
        print(f'Winner!\n{self.sides}')


def build_side(pattern: dict):
    logger.debug('# building side')
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
