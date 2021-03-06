from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardtitle = (By.CSS_SELECTOR, ".card-title a")
    cardfooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def get_card_title(self):
        return self.driver.find_elements(*CheckoutPage.cardtitle)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckoutPage.cardfooter)

    def checkoutitems(self):
        return self.driver.find_element(*CheckoutPage.checkout)
