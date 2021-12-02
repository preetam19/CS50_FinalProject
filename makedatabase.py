import sqlite3
from scrap import Scrap
import bs4
from bs4 import BeautifulSoup
import requests
import sqlite3
from time import gmtime, strftime


    # for z in range(0,11):
    #     ls.append((i[z],j[z],k[z],l[z],m[z],n[z]))
con = sqlite3.connect("redd.db")
db = con.cursor()

print("Database Connected")
# creating the table
db.execute("CREATE TABLE 'red' ('username'  VARCHAR (255),'email' VARCHAR(255), 'password' VARCHAR(200))")
db.execute("CREATE TABLE 'market' ('rank','name', 'price', '24h' ,'7d' ,'market')")
db.execute("CREATE TABLE 'sell' ('Name' VARCHAR(255), 'Amount of Crypto'  INTEGER, 'Price' INTEGER, 'Day', 'Hour', 'status')")
db.execute("CREATE TABLE 'buy' ('Name' VARCHAR(255), 'Amount of Crypto'  INTEGER , 'Price' INTEGER, 'Day', 'Hour','status')")


## To delete tables from database
# db.execute("DROP TABLE 'red'")
# db.execute("DROP TABLE 'sell'")
# db.execute("DROP TABLE 'buy'")
# db.execute("DROP TABLE 'market'")

# gives name of tables that exists
# db.execute("SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;")

# print("Tables Created")
# db.execute(" INSERT INTO red VALUES (13, 'preetam', 'preetham1912@gmail.com')")
# db.execute("INSERT INTO users VALUES (?, ? ,? )", (user_name,user_email,user_id))
# db.execute("SELECT * FROM red WHERE email = ?",("qewq",))
#
db.execute("SELECT  * FROM 'red'  ")
# db.execute("SELECT  * FROM 'market'  ")
# db.execute("SELECT  * FROM 'buy'  ")
#
# db.execute("SELECT  * FROM 'sell'  ")


# db.execute("SELECT  * FROM 'buy' ORDER BY Price,name ")

# db.execute("SELECT  * FROM users  WHERE name=? ",("preetam",))
#
# some = db.fetchall()
#
# xd = []
# for something in some:
#     xd.append(something)
con.commit()

print(db.fetchall())


# con.commit()
# con.close()


