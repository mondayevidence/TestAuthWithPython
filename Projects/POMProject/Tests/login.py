from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.dirname(__file__), "...", "..."))
from Projects.POMProject.Pages.loginPage import LoginPage
from Projects.POMProject.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):
    # we want to run it once

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/home/evidencemonday/IdeaProjects/Test/.idea/drivers/chromedriver")

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    HtmlTestRunner.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/evidencemonday/IdeaProjects/SeleniumTest/reports'))
