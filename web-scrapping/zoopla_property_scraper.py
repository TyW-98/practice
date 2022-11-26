import requests
import pandas as pd 
from bs4 import BeautifulSoup

website = requests.get("https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list")
html = BeautifulSoup(website.content,"html.parser")
#print("https://zoopla.co.uk/"+ html.find(class_="c-hhFiFN").get("href"))
all_listings = html.find_all(class_="c-PJLV c-PJLV-ihinyfY-css")

all_prices = []
property_agent_list = []
property_df = pd.DataFrame()

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
    print(property_agent_list)
    print(listing_link)
    print(property_df)
    print(property_name)
    print(property_postcode)
    
    
property_dict = {"Prices":all_prices,"Property Agents": property_agent_list}