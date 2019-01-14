import unittest
import os

from battlefield import json_bridge as jb


class TestJson(unittest.TestCase):
    def test_safe_pattern(self):
        TEST_FILE_NAME = 'tests/test_temp.json'
        # json transforms tuples to lists, but its n p
        test = {
            'test_template_1': {
                'side_1': [
                    [
                        ['soldier', {}],
                        ['soldier', {}],
                        ['soldier', {}]
                    ],
                ],
            },

        }

        jb.safe_pattern(test, file=TEST_FILE_NAME)
        self.assertTrue(os.path.exists(TEST_FILE_NAME))

        db_names_test = jb.get_available_patterns(file=TEST_FILE_NAME)
        self.assertEqual(db_names_test, test)

        db_sides_test = jb.get_side_pattern('test_template_1', file=TEST_FILE_NAME)
        self.assertEqual(db_sides_test, test['test_template_1'])

        jb.delete_pattern('test_template_1', file=TEST_FILE_NAME)
        self.assertFalse(jb.get_available_patterns(TEST_FILE_NAME))

        os.remove(TEST_FILE_NAME)
