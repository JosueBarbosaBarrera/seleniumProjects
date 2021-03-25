import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class testExplicit(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\driverChrome.exe")
    
    def test_usingExplicitWait(self):
        driver = self.driver
        driver.get("https://www.google.com")
        try:
            element1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()