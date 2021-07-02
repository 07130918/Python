# これはpytestで決まっている書き方
def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux')
