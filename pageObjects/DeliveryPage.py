from selenium.webdriver.common.by import By

from utilities.BaseElement import BaseElement


class DeliveryPage:
    deliverylocation = (By.ID, "country")
    terms_chkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_btn = (By.CSS_SELECTOR, "[type='submit']")


    def __init__(self, driver):
        self.driver = driver

    def delivery_location_textbox(self):
        return BaseElement(self.driver, locator=DeliveryPage.deliverylocation)

    def terms_checkbox(self):
        return BaseElement(self.driver, locator=DeliveryPage.terms_chkbox)

    def purchase_button(self):
        return BaseElement(self.driver, locator=DeliveryPage.purchase_btn)