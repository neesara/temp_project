from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def driver_login(driver):

    driver.get("https://www.softwaretestingmaterial.com/")
    yield driver
    driver.quit()