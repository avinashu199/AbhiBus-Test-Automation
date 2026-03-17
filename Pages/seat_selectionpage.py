from selenium.webdriver.common.by import By

from Pages.popup_page import PopupPage


class SeatSelectionPage:
    seats=(By.CSS_SELECTOR,".seat.sleeper")
    points=(By.XPATH,"//div[@id='place-container']/div[1]")
    proceed=(By.XPATH,"//button[text()='Proceed']")
    def __init__(self, driver):
        self.driver = driver
    def select_seat(self):
        elements=self.driver.find_elements(*SeatSelectionPage.seats)
        for element in elements:
            if not element.is_selected():
                element.click()
                break
            else:
                print("select other seat or bus")
        return self
    def select_points(self):
        self.driver.find_element(*SeatSelectionPage.points).click()
        self.driver.find_element(*SeatSelectionPage.points).click()
        return self
    def click_proceed(self):
        self.driver.find_element(*SeatSelectionPage.proceed).click()
        return PopupPage(self.driver)


