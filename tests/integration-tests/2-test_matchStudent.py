import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

### test functions in Match Students page
## PASSING TESTS
# check page title is correct
def test_matchStudentsPageTitle():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=chrome_options)
    chrome_driver.get('http://127.0.0.1:5221/match_student')

    time.sleep(3)
    if not "Match Student" in chrome_driver.title:
        raise Exception("Incorrect page name")

# test Company List column's drop down list
def test_companyListColumnDropDown():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=chrome_options)
    chrome_driver.get('http://127.0.0.1:5221/match_student')

    time.sleep(2)
    element = chrome_driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[3]/form/select")
    element.click()

# test Status column's drop down list
def test_statusColumnDropDown():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=chrome_options)
    chrome_driver.get('http://127.0.0.1:5221/match_student')

    time.sleep(2)
    element = chrome_driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[4]/form/select")
    element.click()


## FAILING TESTS
# test if there is no company selected before changing status
def test_noSelectedCompany():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=chrome_options)
    chrome_driver.get('http://127.0.0.1:5221/match_student')
    time.sleep(2)

    # open dropdown list for Status column
    element = chrome_driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[4]/form/select")
    
    # select "Pending Confirmation" status
    element = chrome_driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td[4]/form/select/option[2]")
    
