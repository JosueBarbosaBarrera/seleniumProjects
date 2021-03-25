import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Automated Search on google.com

class runUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\driverChrome.exe")

    def test_site(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        self.assertIn("Google", driver.title)
        element1 = driver.find_element_by_name("q")
        element1.send_keys("selenium")
        element1.send_keys(Keys.RETURN)
        time.sleep(5)
        # driver.close()
        assert "Not found element: " not in driver.page_source 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()