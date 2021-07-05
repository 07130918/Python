import unittest
from unittest import mock
from unittest.mock import MagicMock

import mock_training


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = mock_training.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        # bounas_price confirmation
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = mock_training.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    @mock.patch('mock_training.ThirdPartyBonusRestApi.bonus_price', return_value=1)
    def test_calculation_salary_patch(self, mock_bonus):
        """ when you use docollator
            decollator引数にreturn_valueがない場合はコメントのようなコードを書く
        """
        # mock_bonus.return_value = 1

        s = mock_training.Salary(year=2017)
        # salary_price = s.calculation_salary()

        self.assertEqual(s.calculation_salary(), 101)
        # self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    def test_calculation_salary_patch_with(self):
        """ when you use with statement
        """
        with mock.patch(
                'mock_training.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = mock_training.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    def setUp(self):
        self.patcher = mock.patch(
            'mock_training.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary_patch_with_patcher(self):
        """ when you use patcher
        """
        self.mock_bonus.return_value = 1

        s = mock_training.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)

    def test_calculation_salary_patch_side_effect(self):
        """ when you use side effect
        """
        # def f(year):
        #     return year * 2
        # self.mock_bonus.side_effect = f
        # self.mock_bonus.side_effect = ConnectionRefusedError
        self.mock_bonus.side_effect = [1, 2, ValueError('Bankrupt!!!')]

        s = mock_training.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 101)

        s = mock_training.Salary(year=2018)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 102)

        s = mock_training.Salary(year=2019)
        with self.assertRaises(ValueError):
            s.calculation_salary()

    @mock.patch('mock_training.ThirdPartyBonusRestApi', spec=True)
    @mock.patch('mock_training.Salary.get_from_boss')
    def test_calculation_salary_class(self, mock_boss, MockRest):
        """ when you use docollator and spec
            classごとmock作成
        """
        mock_boss.return_value = 10
        # ↓2行は同じ意味
        mock_rest = MockRest.return_value
        # mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1

        s = mock_training.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 111)
        mock_rest.bonus_price.assert_called()


if __name__ == '__main__':
    unittest.main()
