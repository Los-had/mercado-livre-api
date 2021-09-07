from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError
import requests
from datetime import datetime

def default_error_message():
    return {
        "Message": "The product you are trying to search is not available, or doesn't exist, or was not found. Try again."
    }

def http_error_message(error):
    return {
        "Message": f"A http_error(error: {error}) ocurred, try again."
    }

def connection_error_message():
    return {
        "Message": "A connection_error ocurred, try again."
    }

def find_all_products_data(product_name: str):
    if product_name == '':
        return default_error_message()

    try:
        product_name_to_use = product_name.replace(' ', '-')
        url = f'https://lista.mercadolivre.com.br/{product_name_to_use}'
        website = requests.get(url).text
        soup = BeautifulSoup(website, 'lxml')
        #print(soup.prettify())

        response = {
            "products": [],
            "searched_day": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
        }

        products_cards = soup.find_all('div', class_='andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default')
        product_id = 0

        for product_card in products_cards:
            title = product_card.find('h2', class_='ui-search-item__title').text
            product_link = product_card.find('a', class_='ui-search-item__group__element ui-search-link')
            price1 = product_card.find('span', class_='price-tag-fraction').text
            cents = product_card.find('span', class_='price-tag-cents')
            cents2 = str(cents)
            coin = product_card.find('span', class_='price-tag-symbol').text
            price = f'{price1}.{cents2[30:32]}'
            product = {
                "id": product_id,
                "name": title,
                "link": product_link['href'],
                "price": price,
                "coin": coin
            }
            response['products'].append(product)
            product_id += 1

        return response
    except ConnectionError:
        return connection_error_message()
    except HTTPError as err:
        return http_error_message(err)
    except:
        return default_error_message()

def find_product_data(product_name: str):
    if product_name == '':
        return default_error_message()

    try:
        product_name_to_use = product_name.replace(' ', '-')
        url = f'https://lista.mercadolivre.com.br/{product_name_to_use}'
        website = requests.get(url).text
        soup = BeautifulSoup(website, 'lxml')
        product_card = soup.find('div', class_='andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default')
        title = product_card.find('h2', class_='ui-search-item__title').text
        product_link = product_card.find('a', class_='ui-search-item__group__element ui-search-link')
        price1 = product_card.find('span', class_='price-tag-fraction').text
        cents = product_card.find('span', class_='price-tag-cents')
        cents2 = str(cents)
        coin = product_card.find('span', class_='price-tag-symbol').text
        price = f'{price1}.{cents2[30:32]}'
        product = {
            "name": title,
            "link": product_link['href'],
            "price": price,
            "coin": coin
        }
        response = {
            "product": [],
            "searched_day": datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
        }
        response['product'].append(product)

        return response
    except ConnectionError:
        return connection_error_message()
    except HTTPError as err:
        return http_error_message(err)
    except:
        return default_error_message()

if __name__ == "__main__":
    print(find_all_products_data('caneta'))
    print('\n\n\n\n')
    print(find_product_data('caneta'))