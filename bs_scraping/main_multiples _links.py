from turtle import title
from bs4 import BeautifulSoup
import requests


""" result = requests.get("https://www.google.com/")
content = result.text

soup = BeautifulSoup(content, "lxml") """

website = "https://subslikescript.com/movies"
result = requests.get(website)

content = result.text    

soup = BeautifulSoup(content, "lxml")


box = soup.find("article", class_="main-article")

anchors = box.find_all('a', href = True)

links = []
for link in anchors:
    movie = link.get_text()
    movie_link = link['href']
    print(movie)
    print(movie_link)
    print("\n")
    links.append(movie_link)

print(links)

url = "https://subslikescript.com/"

for link in links:
    result = requests.get(url+link)
    content = result.text
    soup = BeautifulSoup(content, "lxml")
    box = soup.find("article", class_="main-article")
    title = box.find('h1').get_text()
    transcript = box.find('div',class_="full-script").get_text(strip=True,separator=' ')

    with open(f"{title}.txt","w", encoding='utf-8') as file:
        file.write(transcript)