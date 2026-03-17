from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Waits:
    def __init__(self,driver):
        self.driver=driver
    def text_to_be_present_in_element(self,locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.text_to_be_present_in_element(locator,"points"))

    def visibility_of_element_located(self,locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.visibility_of_element_located(locator))
    def element_to_be_clickable(self,locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator))
    #def url_changes(self,locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.url_changes(locator))
    def url_contains(self,time=10):
        return WebDriverWait(self.driver,time).until(EC.url_contains("ixigo"))