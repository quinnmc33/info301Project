import requests
import requests_html
from bs4 import BeautifulSoup


URL = "https://www.newworld.co.nz/shop/category/featured?s=popularity&sd=0&ps=50&pg=1"
page = requests.get(URL)

print("Page :")
print(page)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="1-main u-flex-justify-center")
products = soup.find_all('section', class_="fs-product-grid js-product-grid")

# products = 


for product in products:
    prod = product.find_all('div', class_="js-product-card-footer fs-product-card__footer-container")
    print("Just Products:")
    print(prod)

    
