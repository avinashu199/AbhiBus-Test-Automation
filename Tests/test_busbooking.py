
import pytest
from Pages.landing_page import LandingPage
from Utilities.data_reader import DataReader

data=DataReader().test_data().values.tolist()
@pytest.mark.parametrize("url,source,destination,date,mobile,email,name,age",data)
def test_bus_booking(browser_launch,url,source,destination,date,mobile,email,name,age):
    driver=browser_launch
    driver.get(url)
    bus_searchpage=LandingPage(driver).enter_source(source).enter_destination(destination).select_datetime(date).click_search()
    seat_selectpage=bus_searchpage.page_load().select_bus()
    popup_page=seat_selectpage.select_seat().select_points().click_proceed()
    passenger_detailspage=popup_page.skip_popup()
    passenger_detailspage.enter_mobile_number(mobile).enter_email(email).enter_name(name).enter_age(age).click_male_button().click_secure_booking().click_travel_insurance().click_continue_to_pay()

