from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

property_dict = {"Property_Value": [], "Bedrooms": [], "Bathrooms": [],"Area": [],"Reception":[], "Property Address": [], "Property Description": [] }
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
listing_property = driver.find_element(by= By.XPATH, value = '//*[@id="listing_63347676"]') # Get elements of a single listing
a_tag = listing_property.find_element(by=By.TAG_NAME, value = "a") # Get "a" tag within listing property to get "href" attribute
property_link = a_tag.get_attribute("href")
print(property_link)

driver.get(property_link)
property_value = driver.find_element(by= By.XPATH, value = '//*[@class="c-PJLV c-PJLV-igTumRt-css"]')
property_value = property_value.find_element(by = By.TAG_NAME, value = "p").text
property_dict["Property_Value"].append(property_value)
property_features = driver.find_elements(by = By.XPATH, value = '//*[@class= "c-PJLV c-PJLV-kQvhQW-centered-true c-PJLV-iPJLV-css"]')
number_of_bedrooms = property_features[2].text
property_dict["Bedrooms"].append(number_of_bedrooms)
number_of_bathrooms = property_features[3].text
property_dict["Bathrooms"].append(number_of_bathrooms)
reception_yn = property_features[4].text
if reception_yn == None:
    reception_yn = "no"
else:
    reception_yn = "yes"
property_dict["Reception"].append(reception_yn)
property_area = property_features[5].text
property_dict["Area"].append(property_area)
property_address = driver.find_element(by = By.XPATH, value = '//*[@data-testid= "address-label"]').text
property_dict["Property Address"].append(property_address)
property_description = driver.find_element(by = By.XPATH, value = '//*[@data-testid = "listing_features_bulletted"]').text.replace("\n",", ")
property_dict["Property Description"].append(property_description)
print(property_dict)
time.sleep(5)

