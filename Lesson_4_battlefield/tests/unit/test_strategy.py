import unittest
from battlefield.unit.strategy import Strategy


class TestHealth:

    def __init__(self, health):
        self.health = health

    def total_health(self):
        return sum(self.health)

    def __eq__(self, other):
        return self.total_health()


class TestAttack:

    def __init__(self, attack):
        self.attack = attack

    def total_attack(self):
        return sum(self.attack)

    def __eq__(self, other):
        return self.total_attack()


class TestStrategy(unittest.TestCase):

    def test_weakest(self, ):
        testing_s = [TestHealth([1, 2, 30]),
                     TestHealth([1, 2, 20]),
                     TestHealth([1, 2, 10])]
        testing_strategy = Strategy.new('weakest')
        self.assertEqual(TestHealth([1, 2, 10]).total_health(),
                         testing_strategy.squad(testing_s).total_health())
        self.assertEqual(TestHealth([1, 2, 10]).total_health(),
                         testing_strategy.side(testing_s).total_health())

    def test_strongest(self):
        testing_s = [TestAttack([1, 2, 10]),
                     TestAttack([1, 2, 20]),
                     TestAttack([1, 2, 30])]
        testing_strategy = Strategy.new('strongest')
        self.assertEqual(TestAttack([1, 2, 30]).total_attack(),
                         testing_strategy.squad(testing_s).total_attack())
        self.assertEqual(TestAttack([1, 2, 30]).total_attack(),
                         testing_strategy.side(testing_s).total_attack())

    def test_random(self):
        """no need to be tested, its literally random"""
        pass
