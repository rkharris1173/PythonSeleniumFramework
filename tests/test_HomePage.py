import pytest
from pytest import mark
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    @mark.critical
    def test_formSubmission(self, getdata):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        # self.wait_for_element_to_be_clickable(homepage.getName())
        # homepage.getName().click()
        homepage.getName().input_text(getdata["firstname"])
        log.info('Entering name')
        homepage.getEmail().input_text(getdata['email'])
        log.info("entering email")
        homepage.getCheckBox().click()
        self.select_from_dropdown_by_text(homepage.gender, getdata['gender'])
        homepage.submitForm().click()

        alerttext = homepage.getSuccessMessage().get_text

        assert ("Success" in alerttext)
        assert (getdata["firstname"] in homepage.getName().get_attribute('value'))
        assert (getdata['email'] in homepage.getEmail().get_attribute('value'))


    # specific to this test only  feeding data to this test
    @pytest.fixture(params=HomePageData.test_Homepage_data)
    def getdata(self, request):
        return request.param
