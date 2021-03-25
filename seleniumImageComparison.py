import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import cv2

class use_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\driverChrome.exe")

    def test_useCv2(self):
        driver = self.driver
        driver.get("https://www.google.com")
        # Take Screenshot
        driver.save_screenshot("img2.png")
        time.sleep(3)

    def test_ImageCompare(self):
        img1 = cv2.imread("img1.png")
        img2 = cv2.imread("img2.png")

        diff = cv2.absdiff(img1, img2)
        # difference = cv2.absdiff(img1, img2)
        gray_image = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        contours, = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) >= 20:
                position_x, position_y, width, high = cv2.boundingRect(c)
                cv2.rectangle(img1,(position_x, position_y),(position_x + width, position_y + high), (0, 0, 255), 2)
        
        while(1):
            cv2.imshow("Image1", img1)
            cv2.imshow("Image2", img2)
            cv2.imshow("Difference between screenshots", diff)
            keyboard = cv2.waitKey(5) & 0xFF
            if keyboard == 27:
                break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    unittest.main()