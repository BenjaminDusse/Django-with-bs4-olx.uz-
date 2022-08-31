import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup


OLX_UZ = 'https://www.olx.uz'
MAIN_URL = 'https://www.olx.uz/d/oz'
BASE_URL = 'https://www.olx.uz/d/oz/elektronika/kompyutery/periferiynye-ustroystva/'

def get_products(count):
    req = requests.get(BASE_URL)

    soup = BeautifulSoup(req.text, 'lxml')


    # print(results.find('a', class_='css-1bbgabe').get('href'))

    products = {}
    results = soup.find_all('div', {'data-cy' : 'l-card'})
    product_count = 0
    for element in results:
        element_title = element.find('h6', 'css-v3vynn-Text').text
        element_url = element.find('a', class_='css-1bbgabe').get("href")
        element_price = element.find('p', {'data-testid': 'ad-price', 'class': 'css-wpfvmn-Text'}).text
        element_region = element.find('p', {'data-testid': 'location-date', 'class': 'css-p6wsjo-Text'}).text
        created_date, created_time = element_region.split()[-2], element_region.split()[-1]
        element_created_date = f"{created_date} {created_time}"
        products[product_count] = [element_title, OLX_UZ + element_url, element_price, element_region, element_created_date]
        # Product.objects.create(created_date=created_date, title=element_title)
        if product_count == count:
            print("Awesome. You're the best!")
            break
        product_count += 1
        if not element:
            url_tag = soup.find('a', class_='css-1mi714g')
            if url_tag.get('href'):
                url = OLX_UZ + url_tag.get("href")
                print(url)        
            else:
                print("No any urls found!")

        print(f"{product_count}. Title: {element_title}\nLink: {OLX_UZ + element_url}\nPrice: {element_price}\nRegion: {element_region}\nCreated_at: {element_created_date}\n\n")

    print(f"Total products {product_count}")
    products_df = pd.DataFrame.from_dict(products, orient='index', columns=['Product title', 'URL', 'PRICE', 'REGION', 'CREATED_DATE' ])
    products_df.head()
    # writing into csv
    products_df.to_csv('olxuz_products.csv')
    # writing into excel
    with pd.ExcelWriter("C:\\Users\\abduh\\OneDrive\\Desktop\\Django with bs4(olx.uz)\\olx_products.xlsx") as excel_file:
        products_df.to_excel(excel_file, sheet_name='df_1')
        excel_file.save()

if __name__ == "__main__":
    get_products(2)

