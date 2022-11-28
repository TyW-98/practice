from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
website = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
driver.get(website)
time.sleep(5)

try:
    driver.switch_to.frame("gdpr-consent-notice")
    accept_cookies_button = driver.find_element(by = By.XPATH, value = '//*[@id="save"]')
    accept_cookies_button.click()
    
except:
    pass

time.sleep(5)
listing_property = driver.find_element(by= By.XPATH, value = '//*[@id="listing_63347676"]')
a_tag = listing_property.find_element(by=By.TAG_NAME, value = "a")
property_link = a_tag.get_attribute("href")
print(property_link)
