import test_cal


def test_add_num_and_double():
    cal = test_cal.Cal()
    assert cal.add_num_and_double(1, 1) == 4

# class name must start to Test
# func name must start to test_


class TestCal(object):
    def test_add_num_and_double(self):
        cal = test_cal.Cal()
        assert cal.add_num_and_double(1, 1) == 6
