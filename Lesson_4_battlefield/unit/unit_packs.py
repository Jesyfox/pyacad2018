__author__ = 'Bogdan S.'
from random import choice


class Operators:

    def __init__(self, units: list):
        self.units = units

    def __repr__(self):
        return str(self.units)

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
        self.is_Alive = True

    def attack(self, squads):
        strategy = choice(['random', 'weakest', 'strongest'])
        target = self.choose_target(strategy, squads)
        target.take_damage(self.fire())

    def take_damage(self, damage):
        choice(self.units).take_damage(damage)
        self.update()

    def choose_target(self, strategy: str, squads: list):
        if strategy is 'weakest':
            weakest = squads[0]
            for squad in squads:
                if weakest.total_attack() > squad.total_attack():
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

    def update(self):
        to_delete = []
        for i, unit in enumerate(self.units):
            if not unit.is_Alive:
                to_delete.append(i)
        for i in to_delete:
            self.units.pop(i)
        if not self.units:
            self.is_Alive = False

    def total_health(self):
        return [unit.health for unit in self.units]

    def total_attack(self):
        return sum([unit.damage for unit in self.units])

    def attack_success(self):
        return geometric_average([unit.attack_success for unit in self.units])

    def fire(self):
        return sum([unit.attack() for unit in self.units])

    def __repr__(self):
        return str(self.units)


def geometric_average(arr: list):
    power = 1 / len(arr)
    res = 1
    for i in arr:
        res *= i
    return res**power
