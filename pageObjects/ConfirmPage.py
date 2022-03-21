from selenium.webdriver.common.by import By

from utilities.BaseElement import BaseElement


class ConfirmPage:
    checkoutbtn = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def checkoutbutton(self):
        return BaseElement(self.driver, locator=ConfirmPage.checkoutbtn)
