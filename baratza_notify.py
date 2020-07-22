import requests
from bs4 import BeautifulSoup
import time
from subprocess import call

while True:
    try:
        page = requests.get("https://www.baratza.com/shop/refurb")
        soup = BeautifulSoup(page.text, 'html.parser')
        product_items = soup.find_all(class_='product-item-link')

        for item in product_items:
            product = item.contents[0].strip()
            if "encore" in product.lower():
                call("beep")

        time.sleep(5)

    except requests.exceptions.ConnectionError:
        time.sleep(30)
