from selenium.webdriver.common.by import By

from Utilities.waits import Waits


class PassengerDetailsPage:
    mobile_number=(By.XPATH,"//div[@id='passenger-details-mob-input']//input")
    email = (By.XPATH, "//div[@id='passenger-details-email']//input")
    name=(By.XPATH,"//div[@id='passenger-detail-name']//input")
    age=(By.XPATH,"//div[@id='passenger-detail-age']//input")
    male_button=(By.XPATH,"//div[@id='passenger-detail-gender']//button[1]")
    secure_booking=(By.XPATH,"//*[text()='Secure this booking only']")
    travel_insurance=(By.XPATH,"//input[@type='checkbox']")
    continue_to_pay=(By.XPATH,"//a[contains(text(),'Continue')]")
    def __init__(self,driver):
        self.driver=driver
    def enter_mobile_number(self,mobile_number):
        self.driver.find_element(*PassengerDetailsPage.mobile_number).send_keys(mobile_number)
        return self
    def enter_email(self,email):
        self.driver.find_element(*PassengerDetailsPage.email).send_keys(email)
        return self
    def enter_name(self,name):
        self.driver.find_element(*PassengerDetailsPage.name).send_keys(name)
        return self
    def enter_age(self,age):
        self.driver.find_element(*PassengerDetailsPage.age).send_keys(age)
        return self
    def click_male_button(self):
        self.driver.find_element(*PassengerDetailsPage.male_button).click()
        return self
    def click_secure_booking(self):
        self.driver.execute_script("window.scrollTo(0, 800)")
        Waits(self.driver).element_to_be_clickable(PassengerDetailsPage.secure_booking).click()
        return self
    def click_travel_insurance(self):
        self.driver.find_element(*PassengerDetailsPage.travel_insurance).click()
        return self
    def click_continue_to_pay(self):
        self.driver.find_element(*PassengerDetailsPage.continue_to_pay).click()
        return self
