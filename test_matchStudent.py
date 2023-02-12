from selenium import webdriver
from selenium.webdriver.common.by import By
import time

### test functions in Match Students page
## PASSING TESTS
def test_matchStudentsPageTitle_companyListColumnDropDown():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5221/upload_data')
    element = chrome_driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[2]/a")
    element.click()

    # check page title is correct
    if not "Match Student" in chrome_driver.title:
        raise Exception("Incorrect page name")

# test Company List column's drop down list
def test_matchStudentsPageTitle_companyListColumnDropDown():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5221/upload_data')
    element = chrome_driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[2]/a")
    element.click()

    element = chrome_driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[3]/form/select")
    element.click()

# test Status column's drop down list
def test_matchStudentsPageTitle_statusListColumnDropDown():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5221/upload_data')
    element = chrome_driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[2]/a")
    element.click()

    element = chrome_driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[4]/form/select")
    element.click()


## FAILING TESTS
# test if there are no data in Match Students page
def test_noStudentData():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5221/upload_data')
    element = chrome_driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[2]/a")
    element.click()

    element = chrome_driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]")
    if element is None:
        raise Exception("No student data in database")
    
