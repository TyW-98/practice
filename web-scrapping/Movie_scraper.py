import requests
import pandas as pd
from bs4 import BeautifulSoup

def movie_scraper():
    movie_url = input("Paste the movie's IMDB link here: ")
    movie_url = requests.get(movie_url)
    html = BeautifulSoup(movie_url.content, "html.parser") 

    print(html.prettify())
    print(html.title)
    print(html.find("a", class_="sc-bfec09a1-1 gfeYgX").string)
    print(html.find("a", class_="sc-bfec09a1-2 sc-bfec09a1-3 gwnRuk lbPvhp title-cast-item__char").string)

    actor = html.find_all("a", class_="sc-bfec09a1-1 gfeYgX")
    character = html.find_all(class_="sc-bfec09a1-4 kqwseC")

    print(html.find(class_ ="sc-bfec09a1-1 gfeYgX").get('href'))
    print(actor[1].get('href'))

    actor_names = []
    actor_pages = []
    character_names = []
    movie_list = []
    movie_year = []

    actor_df = pd.DataFrame()

    for person, character in zip(actor,character):
        Individual_movie_list = []
        Individual_movie_year_list = []
        print(person.prettify())
        actor_name = person.string
        actor_names.append(actor_name)
        character_names.append(character.string)
        actor_page = person.get("href")
        actor_page = "https://imdb.com"+actor_page
        profile_page = requests.get(actor_page)
        profile_page = BeautifulSoup(profile_page.content,"html.parser")
        all_movies = profile_page.find_all("div",class_ = "filmo-row odd")
        all_years = profile_page.find_all("span",class_ = "year_column")
        for movies,years in zip(all_movies,all_years):
            Individual_movie = movies.b.string
            Individual_movie_list.append(Individual_movie)
            movie_list.append(Individual_movie)
            Individual_movie_year = years.string.replace("\n\xa0","").replace("\n","")
            Individual_movie_year_list.append(Individual_movie_year)
            movie_year.append(Individual_movie_year)
            Individual_movie_dict = {"titles": Individual_movie_list,"year": Individual_movie_year_list}
            movie_dict = {"titles":movie_list,"year":movie_year}
        print(movie_list)
        print(movie_year)
        print(movie_dict)
        actor_pages.append(actor_page)
        individual_details = {"name":actor_name,"profile_page":actor_page,"movies":[Individual_movie_dict]}
        actor_df = actor_df.append(individual_details, ignore_index = True)
        print(actor_df)
        
    details = {"name":actor_names,"profile_page":actor_pages,"movies":[movie_dict]}

    return actor_df

movie_scraper()