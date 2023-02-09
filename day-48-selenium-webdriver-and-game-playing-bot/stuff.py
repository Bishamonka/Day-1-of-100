from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(executable_path="/Users/bishamon/DEV/chromedriver")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.python.org/")

events_dates = driver.find_elements(by="class name", value="event-widget li time")
events_names = driver.find_elements(by="class name", value="event-widget li a")

events_dates_list = []
events_names_list = []

for date in events_dates:
    events_dates_list.append(date.text)

for event in events_names:
    events_names_list.append(event.text)

# print(events_dates_list)
# print(events_names_list)

dict_items_list = []

for index in range(0, len(events_dates_list)):
    dict_item = dict(time=events_dates_list[index], name=events_names_list[index])
    dict_items_list.append(dict_item)
# print(dict_items_list)

events_dict = {item: dict_items_list[item] for item in range(len(dict_items_list))}
print(events_dict)

driver.close()
driver.quit()
