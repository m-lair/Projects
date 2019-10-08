import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():

    URL = 'https://www.corsair.com/us/en/Categories/Products/Memory/Vengeance-PRO-RGB-Black/p/CMW16GX4M2Z3200C16'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup =  BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="product-name").get_text()

    price = soup.find(class_="product-price").get_text()
    price = price.replace('$','')
    convprice = float(price)

    if convprice < 100.0:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sbulldogs3@gmail.com', 'cfexshadow')

    subject = 'The Price is Down'
    body = 'The price is down on the Corsair RAM you want. Check the amount here and that RBG goodness here: https://www.corsair.com/us/en/Categories/Products/Memory/Vengeance-PRO-RGB-Black/p/CMW16GX4M2Z3200C16'
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('sbulldogs3@gmail.com', 'mlair@heidelberg.edu', msg)

    server.quit



check_price()
    


