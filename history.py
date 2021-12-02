import sqlite3



def buy():
    con = sqlite3.connect("redd.db")
    db = con.cursor()
    db.execute("""SELECT * FROM 'buy' ORDER BY Day,Hour""")
    items = db.fetchall()
    # for item in items:
    #     xd.append(item)
    return items

def sell():
    con = sqlite3.connect("redd.db")
    db = con.cursor()
    db.execute("""SELECT * FROM 'sell' ORDER BY Day,Hour""")
    items = db.fetchall()
    # for item in items:
    #     xd.append(item)
    return items

some = buy()
so = sell()
# lol = []
# for somes in some:
#     lol.append(somes)
# for xd in so:
#     lol.append(xd)

# def sorting(l):
#     s = l.sort()
#     for i in range(len(s)+1):
#         if s[i][3] == s[i+1][3]:
#             q = sorted(key= s[4])
#             return q
#         else:
#             return s



loll = sorted(lol, key = lambda x: (x[3],x[2]))








