from bs4 import BeautifulSoup as BS
import requests

response = requests.get("https://news.ycombinator.com/")
website = BS(response.text, "html.parser")
art_title = []
storylink = website.select("table")

pre_title = storylink[0].find_all(class_="athing")
pre_score = storylink[0].find_all(class_="subtext")

for number in range(30):
    try:
        title = pre_title[number].find(class_="titleline").getText()
        score = pre_score[number].find(class_="score").getText()
    except AttributeError:
        title = pre_title[number].find(class_="titleline").getText()
        score = "0 points"
    score_int = str(score).split(" ")[0]
    art_title.append((int(score_int), title))

max_lambda = max(art_title, key=lambda x: x[0])
print(max_lambda)
