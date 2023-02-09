import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


service = Service(executable_path="/Users/bishamon/DEV/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Pass the pre-loader
time.sleep(10)

# Select language
lang_choice = driver.find_element(by='id', value='langSelect-EN')
lang_choice.click()

# Pass the pre-loader
time.sleep(10)

big_cookie = driver.find_element(by='id', value='bigCookie')

game_timeout = 1 * 60   # 1 minutes from now
timeout_start = time.time()

while time.time() < timeout_start + game_timeout:

    # Click on Cookie for 5 seconds
    round_timeout = 10
    round_start = time.time()
    while time.time() < round_start + round_timeout:
        big_cookie.click()

    print("Round ended. 5 Seconds passed.")

    try:
        for i in range(18, -1, -1):
            product = driver.find_element(by='id', value=f'product{i}')
            try:
                product.click()
            except:
                print(f"Product #{i}  is unavailable.")

    except:
        print("Try failed.")


cookies_ps = driver.find_element(by='id', value='cookiesPerSecond').text
print(f"\nFinal result after 1 minute: Cookies {cookies_ps}")
