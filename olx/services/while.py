import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup


MAIN_URL = 'https://www.olx.uz'
BASE_URL = 'https://www.olx.uz/d/oz/elektronika/kompyutery/periferiynye-ustroystva/?page={}'

input_count = int(input("Enter number: "))
def get_products_from_olx(input_count):
    HaveNextPage = True
    page = 1
    product_count = 0
    while(HaveNextPage):
        response = requests.get(BASE_URL.format(page))
        soup = BeautifulSoup(response.text, 'lxml')
        products = {}
        results = soup.find_all('div', {'data-cy' : 'l-card'})
        for element in results:
            element_title = element.find('h6', 'css-v3vynn-Text').text
            element_url = element.find('a', class_='css-1bbgabe').get("href")
            element_price = element.find('p', {'data-testid': 'ad-price', 'class': 'css-wpfvmn-Text'}).text
            element_region = element.find('p', {'data-testid': 'location-date', 'class': 'css-p6wsjo-Text'}).text
            created_date, created_time = element_region.split()[-2], element_region.split()[-1]
            element_created_date = f"{created_date} {created_time}"
            products[product_count] = [element_title, MAIN_URL + element_url, element_price, element_region, element_created_date]
            product_count += 1
            print(f"{product_count}. \nTitle: {element_title}\nLink: {MAIN_URL + element_url}\nPrice: {element_price}\nRegion: {element_region}\nCreated_at: {element_created_date}\n\n")
            url_tag = soup.find('a', class_='css-1mi714g')
            if url_tag is None or input_count <= product_count:
                HaveNextPage = False
                print("No any products found.")
                break
        print(f"Page  {page}")


        page += 1

    print("Awesome, You're the best!")
    print(f"Total products: {product_count}")

get_products_from_olx(3)

# def get_products(count):
#     page_number = 1
#     response = requests.get(BASE_URL.format(page_number))
#     soup = BeautifulSoup(response.text, 'lxml')
#     products = {}
#     results = soup.find_all('div', {'data-cy' : 'l-card'})
#     product_count = 0
#     for element in results:
#         element_title = element.find('h6', 'css-v3vynn-Text').text
#         element_url = element.find('a', class_='css-1bbgabe').get("href")
#         element_price = element.find('p', {'data-testid': 'ad-price', 'class': 'css-wpfvmn-Text'}).text
#         element_region = element.find('p', {'data-testid': 'location-date', 'class': 'css-p6wsjo-Text'}).text
#         created_date, created_time = element_region.split()[-2], element_region.split()[-1]
#         element_created_date = f"{created_date} {created_time}"
#         products[product_count] = [element_title, MAIN_URL + element_url, element_price, element_region, element_created_date]
#         # Product.objects.create(created_date=created_date, title=element_title)
#         print(f"{product_count}. \nTitle: {element_title}\nLink: {MAIN_URL + element_url}\nPrice: {element_price}\nRegion: {element_region}\nCreated_at: {element_created_date}\n\n")
#         if not element:
#             page_number += 1
#             continue
#         if product_count == count:
#             print("Awesome. You're the best!")
#             break
        
#         else:
#             product_count += 1

#     print(f"Total products:  {product_count}")
        # url_tag = soup.find('a', class_='css-1mi714g').get("href")
        # if url_tag:
        #     page_number += 1
        # else:
        #     break




        # if not element:
        #     page_count = 2
        #     url_tag = soup.find('a', class_='css-1mi714g').get("href")
        #     url = MAIN_URL.format(page_count)
        #     response = requests.get()
        #     continue
            # page_count = 2
            # url_tag = soup.find('a', class_='css-1mi714g').get("href")
            # url = MAIN_URL + url_tag.get("href") + "?page={page_count}"

        

    


    #           Writing into excel and csv file


    # products_df = pd.DataFrame.from_dict(products, orient='index', columns=['Product title', 'URL', 'PRICE', 'REGION', 'CREATED_DATE' ])
    # products_df.head()
    # # writing into csv
    # products_df.to_csv('olxuz_products.csv')
    # # writing into excel
    # with pd.ExcelWriter("C:\\Users\\abduh\\OneDrive\\Desktop\\Django with bs4(olx.uz)\\olx_products.xlsx") as excel_file:
    #     products_df.to_excel(excel_file, sheet_name='df_1')
    #     excel_file.save()

# if __name__ == "__main__":
#     get_products(1500)

