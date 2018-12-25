__author__ = 'Bogdan.S'
from player_dialog import builder_dialog


class Battlefield(object):

    def __init__(self):
        self.sides = builder_dialog()

    def __repr__(self):
        from pprint import pprint
        pprint(self.sides)
        return ''

    def update(self):
        to_delete = []
        for key in self.sides.keys():
            if not self.sides[key].is_alive:
                to_delete.append(key)

        for key in to_delete:
            self.sides.pop(key)

    def start(self):
        from time import time
        wait_seconds = 4
        timer = time()
        cycle_counter = 0
        while len(self.sides.keys()) > 1:
            self.update()

            for side, side_obj in self.sides.items():
                turning_side_index = list(self.sides.keys()).index(side)
                enemy_sides = list(self.sides.keys()).pop(turning_side_index)
                side_obj.attack([self.sides[i] for i in enemy_sides if self.sides[i].is_alive])
                side_obj.update()

            cycle_counter += 1

            if time() - timer >= wait_seconds:
                timer = time()
                print('=' * 10, f'cycle{cycle_counter}', '=' * 10)
                print(self)

        print(f'side {self.sides} Win!')


if __name__ == '__main__':
    pass
