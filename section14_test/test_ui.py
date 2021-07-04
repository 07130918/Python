# selenium training
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('https://www.python.org/')
        self.assertIn('Python', self.driver.title)
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
