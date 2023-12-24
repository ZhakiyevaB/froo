
import re
import requests
from bs4 import BeautifulSoup

url = 'https://consumer-api.wolt.com/v1/pages/venue-list/category-burgers?lon=76.954158&lat=43.245132'
response = requests.get(url)
data = response.json()

for section in data.get('sections', []):

    for item in section.get('items', []):

        restaurant_name = item.get('title', '')
        estimate_box = item.get('venue', {}).get('estimate_box', {}).get('title', 'Ресторан закрыт')
        
        print(f'Название ресторана: {restaurant_name}')
        print(f'Время доставки: {estimate_box}\n')
        print("---")