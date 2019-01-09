__author__ = 'Bogdan S.'
from abc import ABC
from random import choice
from .strategy import Strategy
from .miscellaneous_junk import geometric_average


class UnitPacks(ABC):

    def update(self): pass

    def total_health(self): pass

    def total_attack(self): pass


class Operators(UnitPacks):

    def __init__(self, units: list):
        self.units = units

    def __repr__(self):
        return str(self.units)

    def exp_increase(self):
        for unit in self.units:
            unit.exp_increase()

    def experience(self):
        return [unit.experience for unit in self.units]

    def total_health(self):
        return [unit.health for unit in self.units]

    def attack_success(self):
        return [unit.attack_success for unit in self.units]

    def total_attack(self):
        # operators didnt attack
        pass


class Squad(UnitPacks):
    def __init__(self, units):
        self.units = units
        self.is_alive = True

    def __repr__(self):
        return '\n\t' + str(self.units)

    def attack(self, squads):
        strategy = choice(['random', 'weakest', 'strongest'])
        target = Strategy.new(strategy).squad(squads)
        target.take_damage(self.fire())

    def take_damage(self, damage):
        if self.units:
            choice(self.units).take_damage(damage)
        self.update()

    def update(self):
        to_delete = []
        for i, unit in enumerate(self.units):
            if not unit.is_alive:
                to_delete.append(i)

        for i in to_delete:
            self.units.pop(i)

        if not self.units:
            self.is_alive = False

    def total_health(self):
        return sum([unit.health for unit in self.units])

    def total_attack(self):
        return sum([unit.damage for unit in self.units])

    def attack_success(self):
        return geometric_average([unit.attack_success for unit in self.units])

    def fire(self):
        return sum([unit.attack() for unit in self.units])


class Side(UnitPacks):

    def __init__(self, squads: list, name: str):
        self.squads = squads
        self.name = name
        self.is_alive = True

    def __repr__(self):
        return '\n' + self.name + str(self.squads) + '\n'

    def attack(self, sides):
        """choose the side and attack"""
        strategy = choice(['random', 'weakest', 'strongest'])
        target = Strategy.new(strategy).side(sides)
        for squad in self.squads:
            squad.attack(target.squads)

    def update(self):
        to_delete = []
        for i, squad in enumerate(self.squads):
            if not squad.is_alive:
                to_delete.append(i)

        for i in to_delete:
            self.squads.pop(i)

        if not self.squads:
            self.is_alive = False

    def total_health(self):
        return sum([squad.total_health() for squad in self.squads])

    def total_attack(self):
        return sum([squad.total_attack() for squad in self.squads])
