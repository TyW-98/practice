import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=WA99PZ9QACX6FQ2EZ1V8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3 ")
html = BeautifulSoup(webpage.content, "html.parser") 

print(html.prettify())
print(html.title)
print(html.find("a", class_="sc-bfec09a1-1 gfeYgX").string)
print(html.find("a", class_="sc-bfec09a1-2 sc-bfec09a1-3 gwnRuk lbPvhp title-cast-item__char").string)

actor = html.find_all("a", class_="sc-bfec09a1-1 gfeYgX")
profile = html.find_all(class_ = "sc-bfec09a1-1 gfeYgX",id="href")
character = html.find_all(class_="sc-bfec09a1-4 kqwseC")

print(html.find(class_ ="sc-bfec09a1-1 gfeYgX").get('href'))
print(actor[1].get('href'))

actor_name = []
actor_page = []
character_name = []

for person, character in zip(actor,character):
    print(person.prettify())
    actor_name.append(person.string)
    character_name.append(character.string)
    actor_page.append(profile[person].get('href'))
    
    
print(actor_page)
print(actor_name)
print(character_name)