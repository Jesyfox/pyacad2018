__author__ = 'Bogdan.S'
from random import randint, sample, random
from time import time
from unit_packs import *


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
        self.damage = 0
        self.attack_success = 0
        self.reload = waiter(self.recharge)

    def take_damage(self, damage):
        if damage:
            self.health -= damage
            self.update()

    def update(self):
        if self.health <= 0:
            self.health = 0
            self.is_Alive = False

    def attack(self):
        if random() < self.attack_success and not next(self.reload):
            self.exp_increase()
            return self.damage
        else:
            return 0

    def exp_increase(self):
        pass


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
        self.update()

    def exp_increase(self, exp=1):
        if self.experience < 50:
            self.experience += exp
        self.update()

    def update(self):
        super().update()
        self.damage = 0.05 + self.experience / 100
        self.attack_success = 0.5 * (1 + self.health/100) * randint(50 + self.experience, 100) / 100


class Vehicle(Unit):
    """
    a battle vehicle has additional properties:
        operators [1-3] - the number of soldiers required to operate the vehicle

    A vehicle is considered active as long as it self has any health and there is and vehicle operator
    with and health. if the vehicle is destroyed, any remaining vehicle operator is considered as inactive(killed)
    """

    def __init__(self, drivers: list):
        super().__init__(min_recharge=1000)
        self.operators = Operators(drivers)
        self.update()  # initial call

    def take_damage(self, damage):
        if damage:
            to_vehicle = 0.6
            to_random_drvr = 0.2
            to_other_operators = 0.1
            rand_driver = False

            self.health -= damage*to_vehicle

            for driver in sample(self.operators.units, len(self.operators.units)):
                if not rand_driver:
                    driver.health -= damage*to_random_drvr
                    rand_driver = True
                else:
                    driver.health -= damage*to_other_operators
            self.update()

    def update(self):
        super().update()
        if sum(self.operators.health()) < 0:
            self.health = 0
        self.damage = 0.1 + sum([exp/100 for exp in self.operators.experience()])
        self.attack_success = 0.5 * (1 + self.health/100) * geometric_average(self.operators.attack_success())

    def exp_increase(self):
        self.operators.exp_increase()
        self.update()


def waiter(recharge):
    while True:
        timer = time()
        while True:
            if (time() - timer) < (recharge/1000):
                yield True
            else:
                yield False
                break


if __name__ == '__main__':
    from unit_packs import Squad
    alpha = Squad([Vehicle([Soldier(), Soldier(), Soldier()])])
    beta = Squad([Soldier()])
    while alpha.is_Alive and beta.is_Alive:
        alpha.attack([beta])
        beta.attack([alpha])
        print(alpha.total_health(), beta.total_health())
