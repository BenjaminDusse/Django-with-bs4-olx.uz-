import requests
from bs4 import BeautifulSoup
from main import BASE_URL


req = requests.get(BASE_URL)
soup = BeautifulSoup(req.text, 'lxml')

results = soup.find_all('div', {'data-cy' : 'l-card'})
count = 0
for element in results:
    product_image = soup.find('img', class_='css-8wsg1m')
    print(product_image)
