import requests
import bs4

url = "https://karnameh.com/car-price"


response = requests.get(url)

soup = bs4.BeautifulSoup(response.text,'html.parser')
title = soup.find_all("p",attrs={"class":"MuiTypography-root MuiTypography-body1 muirtl-iy5bpq"})
price = soup.find_all('p',attrs={"class":"MuiTypography-root MuiTypography-body1 muirtl-22intj"})

print(title[0].text ,'====', price[0].text)
print(title[1].text ,'====', price[1].text)
print(title[2].text ,'====', price[2].text)
print(title[3].text ,'====', price[3].text)
print(title[4].text ,'====', price[4].text)
print(title[5].text ,'====', price[5].text)
print(title[6].text ,'====', price[6].text)
print(title[7].text ,'====', price[7].text)
print(title[8].text ,'====', price[8].text)
print(title[9].text ,'====', price[9].text)
print(title[10].text ,'====', price[10].text)