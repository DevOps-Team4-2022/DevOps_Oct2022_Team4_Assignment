from selenium import webdriver
from selenium.webdriver.common.by import By
import time

## test navigation bar\
# Upload Data page to Match Students page
def test_uploadDataToMatchStudentPage():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5221/upload_data')

    element = chrome_driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[2]/a")
    element.click()

# # Upload Data page to Match Students page to Prepare Emails page
# def test_matchStuedntsToPrepareEmailsPage():
#     chrome_driver = webdriver.Chrome()
#     chrome_driver.get('http://127.0.0.1:5221/upload_data')

#     element = chrome_driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[2]/a")
#     element.click()
#     element = chrome_driver.find_element(By.XPATH, "...") # replace "..." with button XPATH
#     element.click()

# # Upload Data page to Prepare Emails page to Settings page
# def test_prepareEmailsToSettingsPage():
#     chrome_driver = webdriver.Chrome()
#     chrome_driver.get('http://127.0.0.1:5221/upload_data')

#     element = chrome_driver.find_element(By.XPATH, "...") # replace "..." with button XPATH
#     element.click()
#     element = chrome_driver.find_element(By.XPATH, "...") # replace "..." with button XPATH
#     element.click()

