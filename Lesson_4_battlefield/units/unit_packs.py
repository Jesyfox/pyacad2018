__author__ = 'Bogdan S.'
from random import choice


class Operators:

    def __init__(self, units: list):
        self.units = units

    def exp_increase(self):
        for unit in self.units:
            unit.exp_increase()

    def experience(self):
        return [unit.experience for unit in self.units]

    def health(self):
        return [unit.health for unit in self.units]

    def attack_success(self):
        return [unit.attack_success for unit in self.units]


class Squad:
    def __init__(self, units):
        self.units = units

    def attack(self, squads):
        strategy = choice(['random', 'weakest', 'strongest'])
        target = self.choose_target(strategy, squads)
        if target.attack_success() < self.attack_success():
            target.take_damage(self.total_attack())

    def take_damage(self, damage):
        choice(self.units).take_damage(damage)

    def choose_target(self, strategy: str, squads: list):
        if strategy is 'weakest':
            weakest = squads[0]
            for squad in squads:
                if sum(weakest.total_health()) > sum(squad.total_health()):
                    weakest = squad
            res = weakest
        elif strategy is 'strongest':
            strongest = squads[0]
            for squad in squads:
                if strongest.total_attack() < squad.total_attack():
                    strongest = squad
            res = strongest
        else:
            res = choice(squads)
        return res

    def is_alive(self):
        pass

    def total_health(self):
        return [unit.health for unit in self.units]

    def total_attack(self):
        return sum([unit.damage for unit in self.units])

    def attack_success(self):
        return geometric_average([unit.attack_success for unit in self.units])


def geometric_average(arr: list):
    power = 1 / len(arr)
    res = 1
    for i in arr:
        res *= i
    return res**power
