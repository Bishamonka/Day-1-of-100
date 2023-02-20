import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


USERNAME = os.getenv('link_username')
PASSWORD = os.getenv('link_password')
JOB_TITLE = 'python developer'


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


service = Service(executable_path="/Users/bishamon/DEV/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com/login")

time.sleep(1)

email_input = driver.find_element(by='id', value='username')
email_input.send_keys(USERNAME)
password_input = driver.find_element(by='id', value='password')
password_input.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.CSS_SELECTOR, value='.btn__primary--large')
sign_in_button.click()

time.sleep(1)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3472341955&f_AL=true&geoId=102264497&keywords=python%20developer&location=Ukraine&refresh=true")
jobs_list = driver.find_elements(By.XPATH, value='//*[@id="main"]/div/section[1]/div/ul/li')

time.sleep(1)

for job in jobs_list:
    # print(job)
    # print(job.tag_name)
    a_elements = job.find_elements(By.TAG_NAME, value='a')
    print(a_elements[1].text)
    job_card = driver.find_element(By.XPATH, value='//*[@id="main"]/div/section[2]')
    easy_apply_button = job_card.find_element(By.CSS_SELECTOR, value='.jobs-apply-button')
    easy_apply_button.click()
    print("---")




# ———————————————— # ———————————————— # ———————————————— # ———————————————— # ———————————————— #
#
# At this moment LinkedIn stopped lettimg me in. Right when I got on the right path. :( I should return to it someday.
#
# ———————————————— # ———————————————— # ———————————————— # ———————————————— # ———————————————— #

# Solution code:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = YOUR_LOGIN_EMAIL
ACCOUNT_PASSWORD = YOUR_LOGIN_PASSWORD
PHONE = YOUR_PHONE_NUMBER

chrome_driver_path = YOUR_CHROME_DRIVER_PATH
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()