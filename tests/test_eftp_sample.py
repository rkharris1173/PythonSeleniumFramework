from utilities.BaseClass import BaseClass
from pageObjects.EFTPS_sample import EFTPSSample


class TestEFTPS(BaseClass):

    def test_payment(self):
        eftps = EFTPSSample(self.driver)
        eftps.login_link.click()
        self.wait_for_element_to_be_clickable(EFTPSSample.loginbtn)
        eftps.enter_ein_first2.input_text("16")
        eftps.enter_ein_last.input_text("0000141")
        eftps.enter_pin.input_text("6646")
        eftps.enter_password.input_text("BwEftps$5Ind")
        eftps.login_btn.click()

