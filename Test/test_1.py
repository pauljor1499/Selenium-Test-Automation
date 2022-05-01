import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def login_page():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser = driver
    url = 'http://localhost:8080/'
    browser.get(url)


def test_valid_login(login_page):
    driver.find_element(By.XPATH, "//span[contains(.,'Log In')]").click()
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin")
    driver.find_element(By.XPATH, "//i[@id='togglePassword']").click()
    driver.find_element(By.XPATH, "//button[contains(.,'LOG IN')]").click()
    assert driver.find_element(By.XPATH, "//h1[contains(.,'Welcome to your Dashboard!')]").text
    driver.quit()
