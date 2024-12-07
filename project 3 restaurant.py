import requests
import bs4

url = "https://takhfifan.com/tehran/restaurants-cafes"

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text,'html.parser')
restaurant = soup.find_all("p",attrs={"class":"vendor-card-box__title-text"})
rating = soup.find_all('p',attrs={"class":"rate-badge__rate-value"})

restaurant_data = []
for i in restaurant:
    name = restaurant
    rating = rating
    restaurant_data.append({'name': name, 'rating': rating})