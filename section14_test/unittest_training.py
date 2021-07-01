import unittest

import test_cal

release_name = 'unit test'


class CalTest(unittest.TestCase):
    def setUp(self):
        """execute when test started
        """
        print('Set up test')
        self.cal = test_cal.Cal()

    def tearDown(self):
        """execute when test ended
        """
        print('Clean up')
        del self.cal

    # @unittest.skip('test_add_num_and_double was skipped!!!')
    @unittest.skipIf(release_name == 'unit test', 'skip!')
    def test_add_num_and_double(self):
        """
            must: start with test_
        """
        # self.assertEqual(self.cal.add_num_and_double(1, 1), 4)
        self.assertNotEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()
