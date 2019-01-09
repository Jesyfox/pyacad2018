import unittest
from unittest.mock import patch
from unit.units import Unit


class TestStringMethods(unittest.TestCase):

    def test_is_alive(self):
        unit = Unit.new('soldier')
        self.assertTrue(unit.is_alive)

    def test_is_dead(self):
        unit = Unit.new('soldier')
        unit.take_damage()
        self.assertFalse(unit.is_alive)
