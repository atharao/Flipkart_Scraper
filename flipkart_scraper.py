import argparse
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from prettytable import PrettyTable
import csv

def scrape_flipkart_products(page_url):
    uClient = urlopen(page_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, 'html.parser')

    containers = page_soup.findAll('div', {'class': '_13oc-S'})

    filename = "products.csv"

    headers = ["Product Name", "Price", "Offer", "Specs"]

    with open(filename, 'a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)

        product_table = PrettyTable(headers)

        for container in containers:
            product_name_container = container.find('div', {'class': '_4rR01T'})
            product_name = product_name_container.text.strip() if product_name_container else 'N/A'

            price_container = container.find('div', {'class': '_30jeq3 _1_WHN1'})
            price = price_container.text.strip() if price_container else 'N/A'

            spec_container = container.find('li', {'class': 'rgWa7D'})
            specs = spec_container.text.strip() if spec_container else 'N/A'

            Offer_container = container.find('div', {'class': '_3Ay6Sb'})
            Offer = Offer_container.text.strip() if Offer_container else 'N/A'

            csv_writer.writerow([product_name.replace(',', '|'), price.replace(',', ''), Offer.replace(',', ' '), specs.replace(',', '|')])

            
            product_table.add_row([product_name, price, Offer, specs])

        
        print(product_table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Flipkart mobile products and display in a table.")
    parser.add_argument('page_number', type=int, help="Page number of the Flipkart page to scrape.")
    args = parser.parse_args()

    base_url = 'https://www.flipkart.com/search?q=phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=phone%7CMobiles&requestId=53cf1081-ec8b-4ece-ad30-d2926b2026c9&as-searchtext=ph&page={}'
    page_number = args.page_number
    url_to_scrape = base_url.format(page_number)

    scrape_flipkart_products(url_to_scrape)
