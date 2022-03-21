from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, locator, value="value"):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.value = value
        self.find()

    def __iter__(self):
        for x in self.web_element:
            yield x

    def __getitem__(self, item):
        return self.web_element[item]

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator=self.locator))
        self.web_element = element
        return self.web_element

    def click(self):
        element = WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable(self.locator)))
        element.click()
        return None

    def input_text(self, text):
        if len(self.web_element) == 1:
            self.web_element[0].send_keys(text)
        return text

    @property
    def get_text(self):
        if len(self.web_element) == 1:
            return self.web_element[0].text
        return self.web_element

    def get_attribute(self, value):
        if len(self.web_element) == 1:
            return self.web_element[0].get_attribute(value)
        return self.web_element
