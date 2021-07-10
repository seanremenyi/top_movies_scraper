import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

all_movies = soup.find(name="h3", class_="jsx-4245974604")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open(movies.txt, mode="w") as file:
    for movie in movies:
        file.write(f'{movie}\n')


