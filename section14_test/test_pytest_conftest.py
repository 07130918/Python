# 実行コマンド
# pytest test_pytest_conftest.py --os-name = mac - s

# import pytest
import os

import test_cal


class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = test_cal.Cal()
        cls.test_file_name = 'test.txt'

    def test_add_num_and_double(self, request):
        """ 外から受け取る場合引数名は必ずrequest
        """
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        print(test_file_path)
        assert os.path.exists(test_file_path) is True
