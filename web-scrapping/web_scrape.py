import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=WA99PZ9QACX6FQ2EZ1V8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3 ")
html = BeautifulSoup(webpage.content, "html.parser") 

print(html.prettify())
print(html.title)

