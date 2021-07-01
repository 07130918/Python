import unittest

import unittest_cal


class CalTest(unittest.TestCase):
    def setUp(self):
        """execute when test started
        """
        print('Set up test')
        self.cal = unittest_cal.Cal()

    def tearDown(self):
        """execute when test ended
        """
        print('Clean up')
        del self.cal

    def test_add_num_and_double(self):
        """
            must: start with test_
        """
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)
        # self.assertNotEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()
