import unittest
from unittest.mock import patch, call
import InsideOffice.Lesson_8_test.x as x


class TestStringMethods(unittest.TestCase):
    @patch('builtins.print')
    @patch('x.random')
    def test_x(self, mock_random, pr):
        mock_random.randint.return_value = 10
        x.foo()
        self.assertListEqual(
            pr.mock_calls, [call('x')]
        )
