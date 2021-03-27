import unittest
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import time

class toggleTest(unittest.TestCase):

    def setUp(self):
        self.drive = webdriver.Chrome(executable_path=r"C:\driverChrome\driverChrome.exe")

    def test_using_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(5)
        toggle = driver.find_element_by_xpath('//*[@id="main"]/label[3]/div')
        toggle.click()
        time.sleep(5)
        toggle.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()