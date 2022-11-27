import requests
import pandas as pd 
from bs4 import BeautifulSoup
import time

def property_scraper():
    first_page = input("Paste the zoopla.co.uk link here: ")
    pages_to_scrape = int(input("Number of pages to scrape: "))
    

    all_prices = []
    property_agent_list = []
    property_df = pd.DataFrame()

    for n in range(1,pages_to_scrape+1):
        if n == 1:
            website = requests.get(first_page)
            html = BeautifulSoup(website.content,"html.parser")
            sub_page = html.find_all(class_="eaoxhri5 css-xtzp5a-ButtonLink-Button-StyledPaginationLink eaqu47p1")[2].get("href")
        else:
            time.sleep(60)
            page_url = "https://zoopla.co.uk"+sub_page[:-1]+str(n)
            website = requests.get(page_url)
            html = BeautifulSoup(website.content,"html.parser")
            print(f"Scrapping page number {n}")
        #print("https://zoopla.co.uk/"+ html.find(class_="c-hhFiFN").get("href"))
        all_listings = html.find_all(class_="c-PJLV c-PJLV-ihinyfY-css")

        for indvi_listing in all_listings:
            
            listing_link = "https://zoopla.co.uk"+indvi_listing.findChild().get("href")
            listing_page = requests.get(listing_link)
            listing_page = BeautifulSoup(listing_page.content, "html.parser")
            property_value = listing_page.find("p",class_ = "c-dPyNJo").string
            property_agent = listing_page.find("p", class_= "css-1q5qety efkkbo93").string
            property_name = listing_page.find(class_ ="c-fdQfiB").string
            property_location = property_name.split(", ")
            property_postcode = property_name[-3:]
            all_prices.append(property_value)
            if property_agent not in property_agent_list:
                property_agent_list.append(property_agent)
            else:
                property_agent_list.append(" \" ")
                
            listing_dict ={"Property name":property_location[0],"Listing Page":listing_link,"Property Value":property_value,"Property Postcode": property_postcode,"Property Agent":property_agent}
            property_df = property_df.append(listing_dict, ignore_index = True)
            
        print(property_df)
            
            
        property_dict = {"Prices":all_prices,"Property Agents": property_agent_list}
        
    property_df.sort_values(by = "Property Value",ascending=False, inplace= True)
    
    print(property_df)
    
    return property_df

property_scraper()