import requests


class Stuff(object):

    def __init__(self, name='', vol=0, home_route='', a_price=0.0, vol_per=''):
        self.name = name
        self.vol = vol
        self.home_route = home_route
        self.a_price = a_price
        self.vol_per = vol_per
        self.h_price = 0.0

    def update(self):
        r = requests.get(self.home_route)
        r = r.text[r.text.find("ProductPrice"):]
        r = r[r.find(':'):r.find(',')]
        r = r[r.find("'") + 1:]
        r = r[:r.find("'")]
        r = r.replace(',', '.')
        r = str(r)
        r = r.strip()
        r = r.split(sep='.')
        a = int(r[0])
        b = int(r[1])
        r = a + b / 100.0
        self.h_price = r

    def adjust(self, price):  # arr  --> [a_price, vol, name]
        self.a_price = price

    def show(self):
        print(
            "{0.name}  has following prices: auchan -- {0.a_price}, perekrestok -- {0.h_price}   for {0.vol} {0.vol_per}".format(
                self))

    def recommend(self):
        A = self.a_price * 0.99
        H = self.h_price * 0.95
        if A < H:
            recline = "Auchan"
        else:
            recline = "Perekrestok"

        print("About {0.name} : recommend having deal with the {1}".format(self, recline))
