import inspect
import logging
from pathlib import Path

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    ROOT_PATH = str(Path(__file__).parent.parent)
    TEST_URL = "https://rahulshettyacademy.com/angularpractice"




    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(self.ROOT_PATH +'/logs/'+'logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, linktext):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, linktext))

    def select_from_dropdown_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

