from datetime import datetime, date
import json
import requests
from requests import HTTPError, ConnectionError
import sqlite3
from sqlite3 import Error

actual_month = datetime.now().strftime('%m')
actual_day = datetime.now().strftime('%d')
actual_year = datetime.now().strftime('%Y')
actual_date = date(int(actual_year), int(actual_month), int( actual_day))

try:
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        p_link TEXT NOT NULL,
        email TEXT NOT NULL,
        send_date TEXT NOT NULL
    )
    ''')
    conn.commit()
except Error:
    print('An error ocurred')

def save_to_db(product_name: str, product_id: int, email: str, email_provider: str):
    try:
        full_email = f'{email}@{email_provider}.com'
        product_link1 = f'https://mercado-livre-api-loshad.herokuapp.com/api/find-all/{product_name}'
        api = requests.get(product_link1)
        response = json.loads(api.text)
        product_link = response['products'][int(product_id)]['link']
        product_price = response['products'][int(product_id)]['price']
        name = response['products'][int(product_id)]['name']
        cursor.execute(f'''
        INSERT INTO users (name, price, p_link, email, send_date)
        VALUES ('{name}', {product_price}, '{product_link}', '{full_email}', '{actual_date}')
        ''')
        conn.commit()

        return {
            "Message": "Saved on mercado-livre-api db"
        }

    except Error as e:
        return {
            "Message": f"A db_error(error: {e}) occurred, try again."
        }
    except HTTPError as e:
        return {
            "Message": f"A http_error(error: {e}) occurred, try again."
        }
    except ConnectionError:
        return {
            "Message": "A connection_error ocurred, try again."
        }
#print(actual_date)

if __name__ == '__main__':
    print(save_to_db('chocolate', 0, 'bernardesmiguel709', 'gmail'))
    print(save_to_db('lápis', 0, 'bernardesmiguel709', 'gmail'))
    print(save_to_db('caneta', 0, 'bernardesmiguel709', 'gmail'))
