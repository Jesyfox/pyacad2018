__author__ = 'Bogdan.S'
from random import randint


class Unit(object):
    """
    represents either a soldier
    or a vehicle maned py predeterminated number of soldiers.

    have following properties:
        health %[0-100] - Represents the health of the unit
        recharge [100-2000] Represents the number of ms required to recharge the unit for an attack
    """
    def __init__(self, min_recharge=200):
        self.is_Alive = True
        self.health = 100
        self.recharge = randint(min_recharge, 2000)

    def damaged(self, damage):
        self.health -= damage


class Soldier(Unit):
    """
    Soldiers are units that have an additional property:
        experience [0-50] - Represents the soldier experience

    The experience property is incremented after each successful attack, and is sed to calculate
    the attack success probability and the amount of damage inflicted
    """

    def __init__(self):
        super().__init__()
        self.experience = 0
        self.damage = 0
        self.attack_success = 0
        self.exp_increase(exp=0)

    def exp_increase(self, exp=1):
        self.experience += exp
        self.damage = 0.05 + self.experience / 100
        self.attack_success = 0.5 * (1 + self.health/100) * randint(50 + self.experience, 100) / 100


class Squad:
    def __init__(self, solders):
        self.solders = solders


class Vehicle(Unit):
    """
    a battle vehicle has additional properties:
        operators [1-3] - the number of soldiers required to operate the vehicle
    """

    def __init__(self, drivers: list):
        super().__init__(min_recharge=1000)
        self.operators = Operators(drivers)


class Operators:
    def __init__(self, drivers: list):
        self.drivers = drivers

    def attack_success(self):
        return [drvr.experience for drvr in self.drivers]

    def health(self):
        return [drvr.health for drvr in self.drivers]


def geometric_average(arr:list):
    pass


if __name__ == '__main__':
    johny = Vehicle()
    print(johny.recharge)
