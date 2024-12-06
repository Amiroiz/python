import requests
import bs4

url = "https://tv.filmnet.ir/"


response = requests.get(url)

soup = bs4.BeautifulSoup(response.text,'html.parser')
title = soup.find_all("h4",attrs={"class":"css-stgv2v eg0dt7k0"})

for i in title:
    print(i.text)