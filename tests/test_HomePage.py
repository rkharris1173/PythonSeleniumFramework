import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getdata):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        self.wait_for_element_to_be_clickable(homepage.getName())
        homepage.getName().send_keys(getdata["firstname"])
        log.info('Entering name')
        homepage.getEmail().send_keys(getdata['email'])
        log.info("entering email")
        homepage.getCheckBox().click()
        self.select_from_dropdown_by_text(homepage.getGender(), getdata['gender'])
        homepage.submitForm().click()

        alerttext = homepage.getSuccessMessage().text

        assert ("Success" in alerttext)
        assert (getdata["firstname"] in homepage.getName().get_attribute('value'))
        assert (getdata["email"] in homepage.getEmail().get_attribute('value'))
        assert (getdata['gender'] in homepage.getGender().get_attribute('value'))
        assert (homepage.getCheckBox().is_selected())

    # specific to this test only  feeding data to this test
    @pytest.fixture(params=HomePageData.test_Homepage_data)
    def getdata(self, request):
        return request.param
