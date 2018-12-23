__author__ = 'Bogdan S.'
from abc import ABC


class Strategy(ABC):
    STRATEGY = {}

    def choose(self):
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

    def __init__(self, side):
        self.side_to_attack = side


@Strategy.register('weakest')
class Weakest(StrategyMixin, Strategy):
    pass


@Strategy.register('strongest')
class Strongest(StrategyMixin, Strategy):
    pass


@Strategy.register('random')
class Random(StrategyMixin, Strategy):
    pass
