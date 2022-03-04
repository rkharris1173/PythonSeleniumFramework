from selenium.webdriver.common.by import By


class DeliveryPage:
    deliverylocation = (By.ID, "country")
    terms_chkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_btn = (By.CSS_SELECTOR, "[type='submit']")


    def __init__(self, driver):
        self.driver = driver

    def delivery_location_textbox(self):
        return self.driver.find_element(*DeliveryPage.deliverylocation)

    def terms_checkbox(self):
        return self.driver.find_element(*DeliveryPage.terms_chkbox)

    def purchase_button(self):
        return self.driver.find_element(*DeliveryPage.purchase_btn)