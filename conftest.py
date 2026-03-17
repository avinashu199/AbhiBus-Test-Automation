import pytest
from selenium import webdriver

from Utilities.data_reader import DataReader


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="browser selection")
@pytest.fixture(scope="class")
def browser_launch(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.set_window_size(1920,1080)
        yield driver
        driver.quit()
    else:
        driver = webdriver.Edge()
        driver.implicitly_wait(5)
        driver.set_window_size(1920, 1080)
        yield driver
        driver.quit()

