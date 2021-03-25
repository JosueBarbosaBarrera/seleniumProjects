import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class toggleTest(self):

    def setUp(self):
        self.drive = webdriver.Chrome(executable_path=r"C:\driverChrome\driverChrome.exe")

    def test_using_toggle(self):
        driver = self.driver
        driver.get("")