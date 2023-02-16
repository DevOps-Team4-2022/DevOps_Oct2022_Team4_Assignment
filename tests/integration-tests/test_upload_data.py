import time
import sys, os, inspect
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)

# Set the filename
studentdata_filename = "excel_files_to_upload/student_data.xlsx"
companydata_filename = "excel_files_to_upload/company_data.xlsx"

# Get the absolute path of the file
studentdata_file_path = os.path.join(parentdir, studentdata_filename)
companydata_file_path = os.path.join(parentdir, companydata_filename)

# in upload data page, upload a student csv file
def test_upload_student_data():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=chrome_options)
    chrome_driver.get('http://127.0.0.1:5221/upload_data')

    chrome_driver.find_element(By.NAME, "internship_student_data").send_keys(studentdata_file_path)
    time.sleep(1)

    chrome_driver.find_element(By.XPATH, "/html/body/div/form/input[3]").click()


def test_upload_company_data():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()),
                                     options=chrome_options)
    chrome_driver.get('http://127.0.0.1:5221/upload_data')

    chrome_driver.find_element(By.NAME, "internship_company_data").send_keys(companydata_file_path)
    time.sleep(1)

    chrome_driver.find_element(By.XPATH, "/html/body/div/form/input[3]").click()
