import requests
import bs4


url="https://takhfifan.com/tehran/restaurants-cafes"

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text,"html.parser")

rate = soup.find_all("p",attrs={"class":"rate-badge__rate-value"})


rates = []
name = soup.find_all("p",attrs={"class":"vendor-card-box__title-text"})
names = []
for i,x in zip(rate,name):
    thescore=i.text.strip()
    rates.append(float(thescore))
    thename=x.text.strip()
    names.append(thename)

max_rate = max(rates)
max_index = rates.index(max_rate)
max_name = names[max_index]
print("Max Restaurant Name :", max_name ,"--->","Rate :", max_rate )