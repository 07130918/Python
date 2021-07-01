import unittest

import unittest_cal


class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        """
            must: start with test_
        """
        cal = unittest_cal.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 4)
        self.assertNotEqual(cal.add_num_and_double(1, 1), 4)


if __name__ == '__main__':
    unittest.main()
