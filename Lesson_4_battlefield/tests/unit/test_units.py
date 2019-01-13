import unittest
from battlefield.unit.units import Unit

available_units = [
    ('soldier', {}),
    ('vehicle', {'operator': 'soldier', 'u_count': 3})
]


class TestSoldier(unittest.TestCase):

    def test_is_alive(self):
        unit = Unit.new('soldier')
        self.assertTrue(unit.is_alive)

    def test_is_dead(self):
        unit = Unit.new('soldier')
        unit.take_damage(unit.health)
        self.assertFalse(unit.is_alive)

    def test_damage_zero_exp(self):
        unit = Unit.new('soldier')
        self.assertLess(0, unit.damage)

    def test_damage_max_exp(self):
        unit = Unit.new('soldier')
        for i in range(50):
            unit.exp_increase()
        self.assertLess(0, unit.damage)

    def test_damage_low_health(self):
        unit = Unit.new('soldier')
        unit.take_damage((unit.health-1))
        self.assertLess(0, unit.damage)

    def test_attack_success_zero_exp(self):
        unit = Unit.new('soldier')
        self.assertLess(0, unit.attack_success)

    def test_attack_success_max_exp(self):
        unit = Unit.new('soldier')
        for i in range(50):
            unit.exp_increase()
        self.assertLess(0, unit.attack_success)

    def test_attack_success_low_health(self):
        unit = Unit.new('soldier')
        unit.take_damage(unit.health - 1)
        self.assertLess(0, unit.attack_success)

    def test_max_experience(self):
        unit = Unit.new('soldier')
        for i in range(1000):
            unit.exp_increase()
        self.assertLessEqual(unit.experience, 50)


class TestVehicle(unittest.TestCase):

    def test_is_alive(self):
        unit = Unit.new('vehicle', operator='soldier', u_count=1)
        self.assertTrue(unit.is_alive)

    def test_is_dead(self):
        unit = Unit.new('vehicle', operator='soldier', u_count=1)
        unit.take_damage(unit.health*1.7)
        self.assertFalse(unit.is_alive)

    def test_damage_zero_exp(self):
        unit = Unit.new('vehicle', operator='soldier', u_count=1)
        self.assertLess(0, unit.damage)

    def test_damage_max_exp(self):
        unit = Unit.new('vehicle', operator='soldier', u_count=1)
        for i in range(1000):
            unit.exp_increase()
        self.assertLess(0, unit.damage)

    def test_damage_low_health(self):
        unit = Unit.new('vehicle', operator='soldier', u_count=1)
        unit.take_damage((unit.health-1)*1.7)
        self.assertLess(0, unit.damage)

    def test_attack_success_zero_exp(self):
        unit = Unit.new('vehicle', operator='soldier', u_count=1)
        self.assertLess(0, unit.attack_success)

    def test_attack_success_max_exp(self):
        unit = Unit.new('vehicle', operator='soldier', u_count=1)
        for i in range(50):
            unit.exp_increase()
        self.assertLess(0, unit.attack_success)

    def test_attack_success_low_health(self):
        unit = Unit.new('vehicle', operator='soldier', u_count=1)
        unit.take_damage(unit.health - 1)
        self.assertLess(0, unit.attack_success)
