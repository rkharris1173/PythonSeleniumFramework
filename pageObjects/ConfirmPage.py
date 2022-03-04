from selenium.webdriver.common.by import By


class ConfirmPage:
    checkoutbtn = (By.CLASS_NAME, "btn btn-success")

    def __init__(self, driver):
        self.driver = driver

    def checkoutbutton(self):
        return self.driver.find_element(*ConfirmPage.checkoutbtn)
