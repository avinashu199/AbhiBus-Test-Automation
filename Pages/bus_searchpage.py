from selenium.webdriver.common.by import By

from Pages.seat_selectionpage import SeatSelectionPage
from Utilities.waits import Waits


class BusSearch:
    availability=(By.CSS_SELECTOR,".buses-availability")
    sleeper=(By.CSS_SELECTOR,"#seat-filter-bus-type a:nth-child(2)")
    save_elements=(By.XPATH,"//div[contains(@class,'fare-info')]//div[contains(@class,'chip')]")
   # seat_selection = (
       # By.XPATH,
     #   ".//ancestor::div[contains(@class,'service-card')]//following-sibling::div[contains(@class,'seat-info')]//button"
    #)

    def __init__(self, driver):
        self.driver = driver
    def page_load(self):
        Waits(self.driver).visibility_of_element_located(BusSearch.availability)
        return self
    '''
    def select_type(self):
        self.driver.find_element(*BusSearch.sleeper).click()
        return self
        '''
    def select_bus(self):
        discount_list=[]
        element_list=self.driver.find_elements(*BusSearch.save_elements)
        for element in element_list:
            discount=element.text
            discount_list.append(discount)
        final_list= sorted(discount_list, key=lambda x: int(x.split('₹')[1]))
        max_discount=final_list[-1]
        for element in element_list:
            if max_discount == element.text:
                # Navigate from the discount chip to its ancestor and then to the seat button
                seat_button = element.find_element(
                    By.XPATH,
                    ".//ancestor::div[contains(@class,'fare-info')]//following-sibling::div[contains(@class,'seat-info')]//button"
                )
                seat_button.click()
                break

        return SeatSelectionPage(self.driver)

