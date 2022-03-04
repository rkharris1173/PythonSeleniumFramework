from selenium.webdriver.common.by import By


class DeliveryPage:
    deliverylocation = (By.ID, "country")
    terms_checkbox = (By.ID, "checkbox2")
    purchase_btn = (By.CLASS_NAME, "btn btn-success btn-lg")

    def __init__(self, driver):
        self.driver = driver

    def delivery_location_textbox(self):
        return self.driver.find_element(*DeliveryPage.deliverylocation)

    def terms_checkbox(self):
        return self.driver.find_element(*DeliveryPage.terms_checkbox)

    def purchase_button(self):
        return self.driver.find_element(*DeliveryPage.purchase_btn)