import pytest

import test_cal

# class name must start to Test
# func name must start to test_
is_release = True


def test_add_num_and_double():
    cal = test_cal.Cal()
    assert cal.add_num_and_double(1, 1) == 4


class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = test_cal.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def setup_method(self, method):
        """execute when test started
        """
        print(f'method={method.__name__}')
        # self.cal = test_cal.Cal()

    def teardown_method(self, method):
        """execute when test ended
        """
        print(f'method={method.__name__}')
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    # @pytest.mark.skip(reason='skip')
    @pytest.mark.skipif(is_release is True, reason='skip')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double(1, 1)
