import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('https://www.python.org/')
        self.assertIn('Python', self.driver.title)
        self.driver.find_element_by_link_text('Downloads').click()

        # max wait time == 10seconds
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "widget-title")))
        self.assertEqual('Looking for a specific release?', element[1].text)

        self.driver.find_element_by_link_text('Documentation').click()

        # max wait time == 10seconds
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "call-to-action")))
        self.assertIn('Browse the docs', element[0].text)

        element = self.driver.find_element_by_name('q')
        element.clear()
        # input to search box
        element.send_keys('pycon')
        # RETURN is same meaning 'Enter'
        element.send_keys(Keys.RETURN)
        assert 'No results found' not in self.driver.page_source
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
