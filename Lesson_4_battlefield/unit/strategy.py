__author__ = 'Bogdan S.'
from abc import ABC


class Strategy(ABC):
    STRATEGY = {}

    def side(self, e_side):
        pass

    def squad(self, e_squad):
        pass

    @classmethod
    def register(cls, name):
        def dec(strategy_cls):
            cls.STRATEGY[name] = strategy_cls
            return strategy_cls
        return dec

    @classmethod
    def new(cls, name):
        return cls.STRATEGY[name]()


class StrategyMixin(Strategy):

    def squad(self, e_squad):
        if e_squad is not list:
            raise TypeError('obj must me list')

    def side(self, e_side):
        if e_side is not list:
            raise TypeError('obj must me list')


@Strategy.register('weakest')
class Weakest(Strategy):

    def squad(self, e_squad):
        super().squad(e_squad)
        weakest = e_squad[0]
        for enemy_unit in e_squad:
            if weakest.total_health() > enemy_unit.total_health():
                weakest = enemy_unit

        return weakest

    def side(self, e_side):
        super().side(e_side)
        weakest = e_side[0]
        for enemy_squad in e_side:
            if weakest.total_health() > enemy_squad.total_health():
                weakest = enemy_squad

        return weakest


@Strategy.register('strongest')
class Strongest(Strategy):

    def squad(self, e_squad):
        super().squad(e_squad)
        strongest = e_squad[0]
        for enemy_unit in e_squad:
            if strongest.total_attack() < enemy_unit.total_attack():
                strongest = enemy_unit

        return strongest

    def side(self, e_side):
        super().side(e_side)
        strongest = e_side[0]
        for enemy_squad in e_side:
            if strongest.total_attack() < enemy_squad.total_attack():
                strongest = enemy_squad

        return strongest


@Strategy.register('random')
class Random(Strategy):

    def squad(self, e_squad):
        super().squad(e_squad)
        from random import choice

        return choice(e_squad)

    def side(self, e_side):
        return self.squad(e_side)
