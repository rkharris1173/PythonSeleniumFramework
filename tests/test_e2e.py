import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.DeliveryPage import DeliveryPage
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        homepage = HomePage(self.driver)
        checkoutpage = CheckoutPage(self.driver)
        confirmpage = ConfirmPage(self.driver)
        deliverypage = DeliveryPage(self.driver)

        homepage.shop_item().click()
        cards = checkoutpage.get_card_title()
        i = -1
        for card in cards:
            i = i + 1
            cardtext = card.text
            print(cardtext)
            if cardtext == 'Blackberry':
                checkoutpage.get_card_footer()[i].click()
        checkoutpage.checkoutitems().click()

        confirmpage.checkoutbutton().click()
        deliverypage.delivery_location_textbox().input_text("Ind")
        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()

        deliverypage.terms_checkbox().click()
        deliverypage.purchase_button().click()

        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is " + textMatch)

        assert ("Success! Thank you!" in textMatch)

