import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime

from Pages.bus_searchpage import BusSearch
from Utilities.current_date import CurrentDate
from Utilities.data_reader import DataReader
from Utilities.waits import Waits


class LandingPage:

    source=(By.XPATH,"//input[@placeholder='Leaving From']")
    destination=(By.XPATH,"//input[@placeholder='Going To']")
    search_box=(By.CSS_SELECTOR, ".btn-search")
    date_picker=(By.XPATH, "//input[@placeholder='Onward Journey Date']")
    drop_down=(By.XPATH,"//div[contains(@class,'container auto-complete-drop-down')]/ul[1]/li[1]/div[1]")
    def __init__(self,driver):
        self.driver=driver
    def enter_source(self,from_city_name):
        self.driver.find_element(*LandingPage.source).send_keys(from_city_name)
        if Waits(self.driver).text_to_be_present_in_element(LandingPage.drop_down):
            self.driver.find_element(*LandingPage.drop_down).click()
        else:
            print("Text not found")
        return self
    def enter_destination(self,to_city_name):
        self.driver.find_element(*LandingPage.destination).send_keys(to_city_name)
        if Waits(self.driver).text_to_be_present_in_element(LandingPage.drop_down):
            self.driver.find_element(*LandingPage.drop_down).click()
        else:
            print("Text not found")
        return self
    def select_datetime(self,date):
        self.driver.find_element(*LandingPage.date_picker).click()
        current_month = CurrentDate().current_month()
        df=DataReader().test_data()
        expected_date =date
        obj = datetime.strptime(expected_date, "%Y-%m-%d")
        expected_month = obj.month
        expected_date = obj.day
        if expected_month < current_month:
            assert False, "Cannot select past month"
        elif expected_month == current_month:
            self.driver.find_element(By.XPATH, f"//a[@data-date='{expected_date}']").click()

        else:
            while expected_month > current_month:
                self.driver.find_element(By.CSS_SELECTOR, ".calender-month-change").click()
                current_month += 1

            self.driver.find_element(By.XPATH, f"//a[@data-date='{expected_date}']").click()
        return self
    def click_search(self):
        self.driver.find_element(*LandingPage.search_box).click()
        return BusSearch(self.driver)
