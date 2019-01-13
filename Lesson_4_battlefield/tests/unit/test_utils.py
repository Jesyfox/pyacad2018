import unittest
from unittest.mock import patch
from battlefield.unit.utils import geometric_average, waiter


class TestUtils(unittest.TestCase):

    def test_geometric_average(self):
        self.assertEqual(geometric_average([1, 2, 3, 4, 5]),
                         2.605171084697352)

    @patch('battlefield.unit.utils.time')
    def test_waiter(self, mock_time):
        recharge = 2000
        mock_time.side_effect = [i+1 for i in range(1000)]
        waiting_var = waiter(recharge)
        for i in range(100):
            self.assertFalse(next(waiting_var))
            self.assertTrue(next(waiting_var))
