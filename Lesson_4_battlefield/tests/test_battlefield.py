import unittest
from unittest.mock import patch
from battlefield import battlefield as b
from battlefield.unit.unit_packs import Side, Squad
from battlefield.unit.units import Unit


class TestBattlefield(unittest.TestCase):
    def test_build_side(self):
        pattern = {
                'side_1': [[
                        ('soldier', {}),
                        ('soldier', {}),
                        ('soldier', {})
                    ]]
                }
        testing_build = b.build_side(pattern)
        self.assertIsInstance(testing_build[0], Side)
        self.assertEqual(testing_build[0].name, 'side_1')
        self.assertIsInstance(testing_build[0].squads[0], Squad)
        for i in range(3):
            self.assertIsInstance(testing_build[0].squads[0].units[i], Unit)

    @patch('battlefield.unit.unit_packs.Side')
    def test_battlefield(self, mock_side):
        test_sides = [Side([Squad([Unit.new('soldier'), Unit.new('soldier'), Unit.new('soldier')])], name='side_1'),
                      Side([Squad([Unit.new('soldier'), Unit.new('soldier'), Unit.new('soldier')])], name='side_2'),
                      Side([Squad([Unit.new('soldier'), Unit.new('soldier'), Unit.new('soldier')])], name='side_3')]
        testing_battlefield = b.Battlefield(test_sides)

        enemy_sides_test = [s.name for s in testing_battlefield.filter_enemy_sides(playing_side_index=1)]
        self.assertEqual(enemy_sides_test, ['side_1', 'side_3'])

        testing_battlefield.side_attack(mock_side, enemy_sides=None)
        self.assertFalse(testing_battlefield.is_running)
