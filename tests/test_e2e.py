import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        homepage = HomePage(self.driver)
        homepage.shop_item().click()
        checkoutpage = CheckoutPage(self.driver)
        cards = checkoutpage.get_card_title().text()
        i=-1
        for card in cards:
            i = i + 1
            cardtext = card.text
            print (cardtext)
            if cardtext == 'Blackberry':
                checkoutpage.get_card_footer()[i].click()

        self.verifyLinkPresence("India")

