from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from utilities.locator import Locator
from utilities.BaseElement import BaseElement


class EFTPSSample(BaseClass):
    loginlink = Locator(By.LINK_TEXT, "LOGIN")

    einfirst2 = (By.CSS_SELECTOR,
                  "#LoginForm > div > table:nth-child(1) > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td.autoTab > input:nth-child(1)")
    einlast = (By.CSS_SELECTOR,
                "#LoginForm > div > table:nth-child(1) > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td.autoTab > input:nth-child(2)")
    loginbtn = (By.CLASS_NAME, "css_button")

    pinfield = (By.CSS_SELECTOR,
                "#LoginForm > div > table:nth-child(1) > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(4) > td:nth-child(2) > input")

    passwordfield = (By.CSS_SELECTOR,
                     "#LoginForm > div > table:nth-child(1) > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type=password]")

    def __init__(self, driver):
        self.driver = driver

    @property
    def login_link(self):
        self.wait_for_element_to_be_clickable(locator=EFTPSSample.loginlink)
        return BaseElement(self.driver, locator=EFTPSSample.loginlink)

    @property
    def enter_ein_first2(self):
        return BaseElement(self.driver, locator=EFTPSSample.einfirst2)

    @property
    def enter_ein_last(self):
        return BaseElement(self.driver, locator=EFTPSSample.einlast)

    @property
    def login_btn(self):
        return BaseElement(self.driver, locator=EFTPSSample.loginbtn)

    @property
    def enter_pin(self):
        return BaseElement(self.driver, locator=EFTPSSample.pinfield)

    @property
    def enter_password(self):
        return BaseElement(self.driver, locator=EFTPSSample.passwordfield)