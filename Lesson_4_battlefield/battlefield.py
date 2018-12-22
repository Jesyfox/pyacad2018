__author__ = 'Bogdan.S'
from options import builder_dialog


class Battlefield(object):

    def __init__(self):
        self.sides = builder_dialog()
        self.turn = self.next_side()

    def __repr__(self):
        from pprint import pprint
        pprint(self.sides)
        return ''

    def next_side(self):
        """returns next side: next(*class_var*.turn)"""
        while True:
            self.update()
            for side in self.sides.keys():
                yield self.sides[side]

    def update(self):
        print(self)
        for key in self.sides.keys():
            self.sides[key] = [s for s in self.sides[key] if s.is_Alive]

    def start(self):
        # wait_seconds = 4
        # from time import time
        # while True:
        #     timer = time()
        #     try:
        #         while True:
        #             side = next(self.turn)
        #             oposide_side = next(self.turn)
        #
        #             for squad in side:
        #                 squad.attack(oposide_side)
        #
        #             for squad in oposide_side:
        #                 squad.attack(side)
        #
        #             if time() - timer >= wait_seconds:
        #                 print(self)
        #                 print('='*20)
        #                 break
        #     except IndexError:
        #         print(self)
        #         print('THE END')
        pass


if __name__ == '__main__':
    pass
