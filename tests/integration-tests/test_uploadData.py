from selenium import webdriver
from selenium.webdriver.common.by import By
import time

### test functions in Upload Students page
## PASSING TESTS
def test_uploadDataPageTitle_uploadStudentsButton():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5221/upload_data')

    # check page title is correct
    if not "Upload Data" in chrome_driver.title:
        raise Exception("Incorrect page name")

    # test Upload Student Data button
    element = chrome_driver.find_element(By.XPATH, "/html/body/div[1]/form/input[1]")
    element.click()

# test Upload Company Data button
def test_uploadCompanyButton():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5221/upload_data')

    element = chrome_driver.find_element(By.XPATH, "/html/body/div[1]/form/input[2]")
    element.click()


## FAILING TESTS
# test Upload button with no file(s) chosen
def test_uploadButton():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5221/upload_data')

    element = chrome_driver.find_element(By.XPATH, "/html/body/div[1]/form/input[3]")
    element.click()