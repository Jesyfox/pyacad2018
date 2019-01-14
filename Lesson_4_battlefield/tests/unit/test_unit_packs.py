import unittest
from battlefield.unit import unit_packs
from battlefield.unit.units import Unit


class TestUnitPacks(unittest.TestCase):

    def test_squad(self):
        testing_squad = unit_packs.Squad([Unit.new('soldier'),
                                          Unit.new('soldier'),
                                          Unit.new('soldier')])
        self.assertEqual(testing_squad.total_health(), 300)
        testing_squad.take_damage(1000)
        self.assertEqual(len(testing_squad.units), 2)
        testing_squad.take_damage(1000)
        testing_squad.take_damage(1000)
        self.assertFalse(testing_squad.is_alive)

    def test_side(self):
        testing_side = unit_packs.Side([unit_packs.Squad([Unit.new('soldier'),
                                                         Unit.new('soldier'),
                                                         Unit.new('soldier')]),
                                       unit_packs.Squad([Unit.new('soldier'),
                                                         Unit.new('soldier'),
                                                         Unit.new('soldier')]),
                                       unit_packs.Squad([Unit.new('soldier'),
                                                         Unit.new('soldier'),
                                                         Unit.new('soldier')])],
                                       name='testing_side')
        self.assertEqual(testing_side.total_health(), 900)
        testing_side.squads[0].take_damage(1000)
        testing_side.squads[0].take_damage(1000)
        testing_side.squads[0].take_damage(1000)
        testing_side.update()
        self.assertEqual(len(testing_side.squads), 2)


