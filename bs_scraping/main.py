from bs4 import BeautifulSoup
import requests


root = "https://subslikescript.com"
website = f"{root}/movies_letter-A"
result = requests.get(website)
content = result.text    
soup = BeautifulSoup(content, "lxml")

pagination = soup.find("ul", class_="pagination")
pages = pagination.find_all('li',class_="page-item")
last_page = int(pages[-2].text)
print(type(last_page))


links = []
for page in range(1,last_page+1)[:2]:
    website = f"{website}?page={page}"
    result = requests.get(website)
    content = result.text    
    soup = BeautifulSoup(content, "lxml")

    
    box = soup.find("article", class_="main-article")
    anchors = box.find_all('a', href = True)

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
    try:
        result = requests.get(url+link)
        content = result.text
        soup = BeautifulSoup(content, "lxml")
        box = soup.find("article", class_="main-article")
        title = box.find('h1').get_text()
        transcript = box.find('div',class_="full-script").get_text(strip=True,separator=' ')

        with open(f"{title}.txt","w", encoding='utf-8') as file:
            file.write(transcript)
    except:
        print(f"Error with {title}")