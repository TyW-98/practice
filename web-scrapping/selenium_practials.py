from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def page_scraper():
    property_dict = {"Property_Value": [], "Bedrooms": [], "Bathrooms": [],"Area": [],"Reception":[], "Property Address": [], "Property Description": [] }
    location = input("What area are you looking for - ")
    pages_to_scrape = int(input("How many pages to scrape: "))
    driver = webdriver.Chrome()
    driver.get("https://www.zoopla.co.uk/")
    time.sleep(5)
    
    try:
        driver.switch_to.frame("gdpr-consent-notice")
        accept_cookies_button = driver.find_element(by = By.XPATH, value = '//*[@id="save"]')
        accept_cookies_button.click()
        
    except:
        pass   
    
    search_bar = driver.find_element(by = By.XPATH, value = '//*[@class = "c-voGFy"]')
    search_bar.send_keys(location)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.current_url
    driver.find_elements(by = By.XPATH, value = '//button[@role="button"]')[1].click()
    time.sleep(5)
    
    for n in range(1,pages_to_scrape+1):
        
        if n != 1:
            print(f"Scrapping page {n}")
            driver.get(home_page)
            time.sleep(7.5)
            driver.find_elements(by = By.XPATH, value = '//*[@class = "eaoxhri5 css-xtzp5a-ButtonLink-Button-StyledPaginationLink eaqu47p1"]')[6].click()
           
        time.sleep(2) 
        home_page = driver.current_url
              
        all_listing = driver.find_elements(by= By.XPATH, value = '//div[@class= "c-PJLV c-PJLV-igALLAE-css"]')
        #print(all_listing[1].find_element(by = By.TAG_NAME, value = "a").get_attribute("href"))

        listing_link_list = []

        for listing in all_listing: 
            listing_link = listing.find_element(by = By.TAG_NAME, value = "a").get_attribute("href")
            listing_link_list.append(listing_link)

        for listing in listing_link_list:
            driver.get(listing)
            property_value = driver.find_element(by= By.XPATH, value = '//*[@class="c-PJLV c-PJLV-igTumRt-css"]')
            property_value = property_value.find_element(by = By.TAG_NAME, value = "p").text
            property_dict["Property_Value"].append(property_value)
            property_features = driver.find_elements(by = By.XPATH, value = '//*[@class= "c-PJLV c-PJLV-kQvhQW-centered-true c-PJLV-iPJLV-css"]')
            number_of_listed_features = len(property_features)
            
            if number_of_listed_features == 0 or number_of_listed_features == None or number_of_listed_features == 1 or number_of_listed_features == 2:
                number_of_bedrooms = "Not listed"
                number_of_bathrooms = "Not listed"
                reception_yn = "no"
            elif number_of_listed_features == 3:
                number_of_bedrooms = property_features[2].text
                number_of_bathrooms = "Not listed"
                reception_yn = "no"
            elif number_of_listed_features == 4:
                number_of_bedrooms = property_features[2].text
                number_of_bathrooms = property_features[3].text
                reception_yn = "no"
            elif number_of_listed_features == 5:
                number_of_bedrooms = property_features[2].text
                number_of_bathrooms = property_features[3].text
                reception_yn = property_features[4].text
                
                if reception_yn == None:
                    reception_yn = "no"
                
                reception_yn = "yes"
            
            property_dict["Bedrooms"].append(number_of_bedrooms)
            property_dict["Bathrooms"].append(number_of_bathrooms)
            property_dict["Reception"].append(reception_yn)
            
            if number_of_listed_features == 6:
                property_area = property_features[5].text    
            else:
                property_area = "Not Listed"
                
            property_dict["Area"].append(property_area)
            property_address = driver.find_element(by = By.XPATH, value = '//*[@data-testid= "address-label"]').text
            property_dict["Property Address"].append(property_address)
            property_description = driver.find_element(by = By.XPATH, value = '//*[@data-testid = "listing_features_bulletted"]').text.replace("\n",", ")
            property_dict["Property Description"].append(property_description)
            print(property_dict)
            time.sleep(5)
            
page_scraper()