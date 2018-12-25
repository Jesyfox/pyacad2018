__author__ = 'Bogdan.S'
from abc import ABC
from random import randint, sample, random
from unit_packs import Operators
from miscellaneous_junk import waiter, geometric_average


class Unit(ABC):
    UNIT = {}

    def take_damage(self, damage):
        pass

    def update(self):
        pass

    def attack(self):
        pass

    def exp_increase(self):
        pass

    @classmethod
    def register(cls, name):
        def dec(unit_cls):
            cls.UNIT[name] = unit_cls
            return unit_cls
        return dec

    @classmethod
    def new(cls, name):
        return cls.UNIT[name]()


class UnitBaseMixin:
    """
    represents either a soldier
    or a vehicle maned py predeterminated number of soldiers.

    have following properties:
        health %[0-100] - Represents the health of the unit
        recharge [100-2000] Represents the number of ms required to recharge the unit for an attack
    """
    def __init__(self, min_recharge=200):
        self.is_alive = True
        self.visual = 'X'
        self.health = 100
        self.recharge = randint(min_recharge, 2000)
        self.damage = 0
        self.attack_success = 0
        self.reload = waiter(self.recharge)

    def __repr__(self):
        """
        represents unit visualisation and health bar
        like: 24 = '. ' or 79 = ':.'
        """
        health_bar = ['. ', ': ', ':.', '::', '']
        scale_index = int(self.health * (len(health_bar)-1) // 100)
        return f'{self.visual}{health_bar[scale_index]}'

    def take_damage(self, damage):
        if damage:
            self.health -= damage
            self.update()

    def update(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def attack(self):
        if random() < self.attack_success and not next(self.reload):
            self.exp_increase()
            return self.damage
        else:
            return 0

    def exp_increase(self):
        pass


@Unit.register('soldier')
class Soldier(UnitBaseMixin, Unit):
    """
    Soldiers are units that have an additional property:
        experience [0-50] - Represents the soldier experience

    The experience property is incremented after each successful attack, and is sed to calculate
    the attack success probability and the amount of damage inflicted
    """

    def __init__(self):
        super().__init__()
        self.unit_type = 'soldier'
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
        self.visual = '-0'


@Unit.register('vehicle')
class Vehicle(UnitBaseMixin, Unit):
    """
    a battle vehicle has additional properties:
        operators [1-3] - the number of soldiers required to operate the vehicle

    A vehicle is considered active as long as it self has any health and there is and vehicle operator
    with and health. if the vehicle is destroyed, any remaining vehicle operator is considered as inactive(killed)
    """

    def __init__(self, drivers=[Soldier()]):
        super().__init__(min_recharge=1000,)
        self.unit_type = 'vehicle'
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
        if sum(self.operators.total_health()) < 0:
            self.health = 0
        self.damage = 0.1 + sum([exp/100 for exp in self.operators.experience()])
        self.attack_success = 0.5 * (1 + self.health/100) * geometric_average(self.operators.attack_success())
        self.visual = f'-=/{self.operators}\\'.replace(', ', '_')

    def exp_increase(self):
        self.operators.exp_increase()
        self.update()

    def add_drivers(self, num):
        if num > 3:
            num = 3
        elif num < 0:
            num = 1
        drivers = [Soldier() for i in range(num)]
        self.operators = Operators(drivers)
        self.update()


if __name__ == '__main__':
    # fight with soldier and vehicle test
    # from unit_packs import Squad
    # alpha = Squad([Vehicle([Soldier(), Soldier(), Soldier()])])
    # beta = Squad([Soldier()])
    # while alpha.is_Alive and beta.is_Alive:
    #     alpha.attack([beta])
    #     beta.attack([alpha])
    #     print(alpha, alpha.total_health(), beta, beta.total_health())
    a = Unit.new('vehicle')
    a.add_drivers(3)
    print(a)
