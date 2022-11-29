from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

def page_scraper():
    property_dict = {"Property_Value": [], "Bedrooms": [], "Bathrooms": [],"Area": [],"Reception":[], "Property Address": [], "Property Description": [] }
    driver = webdriver.Chrome()
    pages_to_scrape = 2
    time.sleep(5)
    
    try:
        driver.switch_to.frame("gdpr-consent-notice")
        accept_cookies_button = driver.find_element(by = By.XPATH, value = '//*[@id="save"]')
        accept_cookies_button.click()
        
    except:
        pass

    for n in range(1,pages_to_scrape+1):
        
        if n == 1:
            main_page = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
            driver.get(main_page)
        else:
            driver.get(main_page)
            time.sleep(5)
            next_page = driver.find_elements(by = By.XPATH, value = '//*[@class = "eaoxhri5 css-xtzp5a-ButtonLink-Button-StyledPaginationLink eaqu47p1"]')[6]
            next_page.click()
        
        time.sleep(5)    
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
            
            if number_of_listed_features == 2:
                number_of_bedrooms = "Not listed"
                number_of_bathrooms = "Not listed"
            else:
                number_of_bedrooms = property_features[2].text
                number_of_bathrooms = property_features[3].text
            
            property_dict["Bedrooms"].append(number_of_bedrooms)
            property_dict["Bathrooms"].append(number_of_bathrooms)
            
            if number_of_listed_features == 4:
                reception_yn = "no"
            else:
                reception_yn = property_features[4].text
                
                if reception_yn == None:
                    reception_yn = "no"
                
                reception_yn = "yes"
            
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