import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style


def changeColor():
    r = requests.get("https://finance.yahoo.com/quote/FB?p=FB")
    soup = BeautifulSoup(r.text, "lxml")
    price = (
        soup.find("div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"})
        .find("span")
        .text
    )
    priceint = int(float(price))
    if priceint > 270:
        print(Fore.GREEN + "the current price: ", str(price))
    else:
        print(Fore.RED + "the current price: ", str(price))


while True:
    changeColor()
