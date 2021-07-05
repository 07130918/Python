import os
import pytest


# original fixture
@pytest.fixture
def csv_file(tmpdir):
    # return 'csv file!!!'
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('before test')
        print(f'tmpdir: {tmpdir}')
        yield c
        print('after test')


def pytest_addoption(parser):
    """これはpytestで決まっている書き方
    """
    parser.addoption('--os-name', default='linux')
