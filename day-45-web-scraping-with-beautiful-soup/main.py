from bs4 import BeautifulSoup as BS
import requests
import random

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
top_100_movies_page = response.text
web_page = BS(top_100_movies_page, "html.parser")

movie_num = []
movie_name = []

articles_div = web_page.find_all(name="section")
for article in articles_div:
    movie_article = article.find(name="h3").getText()
    movie_num.append(movie_article.split()[0][:-1])
    movie_name.append(movie_article.split(" ", 1)[1])

top_100_movies_to_watch = dict(zip(movie_num, movie_name))
random_movie = random.choice(list(top_100_movies_to_watch.items()))

movie_position = random_movie[0]
movie_name = random_movie[1]

print("\n100 MOVIES OF ALL TIME\n")
print(f"Position: {movie_position}/100\nMovie name: {movie_name}")
