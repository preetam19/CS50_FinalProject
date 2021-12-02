import bs4
from bs4 import BeautifulSoup
import requests
import sqlite3
import time


class Scrap():



    #rankdef
    def rank():
        url = requests.get("https://www.cryptocurrencychart.com/")
        soup = bs4.BeautifulSoup(url.text, "html.parser")
        ranks = []
        for i in range(0,25):
            rank = soup.find("table", {"class": "market-cap-list"}).find_all("td", {"class": "rank numeric"})[i].text
            ranks.append(rank)
        return ranks

    #Name
    def name():
        url = requests.get("https://www.cryptocurrencychart.com/")
        soup = bs4.BeautifulSoup(url.text, "html.parser")
        names = []
        for  i in range(0,25):
            name = soup.find("table",{"class":"market-cap-list"}).find_all("td", {"class":"name"})[i].text

            names.append(name)
        return names

    #Price
    def price():
        url = requests.get("https://www.cryptocurrencychart.com/")
        soup = bs4.BeautifulSoup(url.text, "html.parser")
        prices = []
        for i in range(0,25):
            price = soup.find("table",{"class":"market-cap-list"}).find_all("td", {"class":"numeric price"})[i].text
            prices.append(price)
        return prices




    #value last 24 hrs
    def table():
        url = requests.get("https://www.cryptocurrencychart.com/")
        soup = bs4.BeautifulSoup(url.text, "html.parser")
        tables =[]
        for i in range(0,25):
            table = soup.find("table",{"class":"market-cap-list"}).find_all("td", {"title":"Price change since yesterday"})[i].text
            tables.append(table)
        return tables


    #value last 7d
    def trade():
        url = requests.get("https://www.cryptocurrencychart.com/")
        soup = bs4.BeautifulSoup(url.text, "html.parser")
        trade = []
        for i in range(0,25):
            trades = soup.find("table",{"class":"market-cap-list"}).find_all("td", {"class":"numeric health"})[i].text
            trade.append(trades)

        return  trade

    #Market
    def market():
        url = requests.get("https://www.cryptocurrencychart.com/")
        soup = bs4.BeautifulSoup(url.text, "html.parser")
        markets = []
        for i in range(0,25):
            market =soup.find("table",{"class":"market-cap-list"}).find_all("td", {"class":"numeric marketCap"})[i].text

            markets.append(market)
        return markets
    # def image():
    #     url1 = requests.get("https://www.tradingview.com/markets/cryptocurrencies/prices-all/")
    #     soup1 = bs4.BeautifulSoup(url1.text, "html.parser")
    #     ima = soup1.find_all("img",
    #                             {"class": "tv-circle-logo tv-circle-logo--medium tv-screener-table__logo-container"})
    #     im= []
    #     for i in ima:
    #         im.append(i["src"])
    #     images = im[0:25]
    #     return images


# while True:
rank = Scrap.rank()
name = Scrap.name()
price = Scrap.price()
table = Scrap.table()
sev_day = Scrap.trade()
market = Scrap.market()
# images = Scrap.image()
ls = []
for i in range(25):
    ls.append((rank[i], name[i], price[i], table[i], sev_day[i], market[i]))
data = tuple(ls)
# print(data)
        # time.sleep(30)

d=[]
for i in range(25):
    d.append(name[i])
currency = tuple(d)


    # time.sleep(10)


