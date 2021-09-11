import smtplib
import time
import sqlite3
from datetime import datetime, timedelta, date
from sqlite3 import Error

password = open('password.txt').read()
actual_date1 = datetime.now().strftime('%Y-%m-%d')
actual_date = datetime.strptime(actual_date1, '%Y-%m-%d').date()

try:
    conn = sqlite3.connect('users.db', check_same_thread=False)
    c = conn.cursor()
except Error as e:
    print(f'Error!(error: {e}) we could not connect to the database, try again.')

def send_error_email(email, error):
    email_to = 'RandomPersonAPI.comments@gmail.com'
    email_for = email
    smtp = 'smtp.gmail.com'
    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email_to, password)
    msg = f'''
    We couldn't send the product email, because of an error(error: {error})
    '''
    server.sendmail(email_to, email_for, msg)
    server.quit()

def send_email(email, link, name):
    email_to = 'RandomPersonAPI.comments@gmail.com'
    email_for = email
    smtp = 'smtp.gmail.com'
    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email_to, password)
    msg = f'''
    Check the price of {name}! In this link:
    {link}
    '''
    server.sendmail(email_to, email_for, msg)
    server.quit()

c.execute("""
SELECT * FROM users;
""")

while True:
    for row in c.fetchall():
        print(f'{row}\n\n\n')
        str_to_date = date = datetime.strptime(row[5], '%Y-%m-%d').date()
        if actual_date == str_to_date:
            try:
                send_email(row[4], row[3], row[1].encode('utf-8'))
                new_date = str_to_date + timedelta(days = 7)
                print(new_date)
                c.execute("""
                UPDATE users SET send_date = ?
                WHERE id = ?
                """, (new_date, row[0]))
                conn.commit()
            except UnicodeError as e:
                send_error_email(row[4], e)

        print(f'\n\n\n{row}')

    time.sleep(7200)        