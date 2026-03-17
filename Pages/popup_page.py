from selenium.webdriver.common.by import By

from Pages.passengerdetails_page import PassengerDetailsPage
from Utilities.waits import Waits


class PopupPage:
    skip=(By.XPATH,"//a[text()='Skip']")
    def __init__(self,driver):
        self.driver = driver
    def skip_popup(self):
        Waits(self.driver).element_to_be_clickable(PopupPage.skip).click()
        return PassengerDetailsPage(self.driver)
