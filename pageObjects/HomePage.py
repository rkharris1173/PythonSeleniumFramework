from selenium.webdriver.common.by import By

from utilities.BaseElement import BaseElement


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href$='shop']")
    name = (By.CSS_SELECTOR, "body > app-root > form-comp > div > form > div:nth-child(1) > input")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR, "body > app-root > form-comp > div > form > input")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shop_item(self):
        return BaseElement(self.driver, locator=HomePage.shop)

    def getName(self):
        return BaseElement(self.driver, locator=HomePage.name)

    def getEmail(self):
        return BaseElement(self.driver, locator=HomePage.email)

    def getCheckBox(self):
        return BaseElement(self.driver, locator=HomePage.check)

    def getGender(self):
        return BaseElement(self.driver, locator=HomePage.gender)

    def submitForm(self):
        return BaseElement(self.driver, locator=HomePage.submit)

    def getSuccessMessage(self):
        return BaseElement(self.driver, locator=HomePage.successMessage)
