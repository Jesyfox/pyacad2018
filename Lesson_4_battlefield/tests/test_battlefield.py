import unittest
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
        equal_build = [Side(
                      [Squad([Unit.new('soldier'),
                              Unit.new('soldier'),
                              Unit.new('soldier')])],
                       name='side_1')]
        self.assertEqual(type(testing_build[0]), type(equal_build[0]))
        self.assertEqual(testing_build[0].name, equal_build[0].name)
        self.assertEqual(type(testing_build[0].squads[0]),
                         type(equal_build[0].squads[0]))
        for i in range(3):
            self.assertEqual(type(testing_build[0].squads[0].units[i]),
                             type(equal_build[0].squads[0].units[i]))

