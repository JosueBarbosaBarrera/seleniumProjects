import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Search on google.com by XPath

class runUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\driverChrome.exe")

    def test_search_by_xpath(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        time.sleep(3)
        # Search by relative XPath
        search_by_xpath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        search_by_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()