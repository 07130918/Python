import unittest
from unittest.mock import MagicMock

import mock_training


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = mock_training.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        print(s.calculation_salary())
        self.assertEqual(s.calculation_salary(), 101)


if __name__ == '__main__':
    unittest.main()
