from cls_Stuff import Stuff


class Engine(object):
    stuff_log = []

    def read(self):
        file = open("shops_data.dat", 'r')
        buf = file.readline().strip()
        while (buf):
            buf = buf.split(sep=' ')
            S = Stuff(buf[0], int(buf[1]), buf[2], float(buf[3]), buf[4])
            S.update()
            self.stuff_log.append(S)
            buf = file.readline().strip()

        file.close()

    def save(self):
        file = open("shops_data.dat", 'w')
        for i in self.stuff_log:
            file.write("{0.name} {0.vol} {0.home_route} {0.a_price} {0.vol_per}\n".format(i))
        file.close()

    def update(self):
        for i in self.stuff_log:
            i.update()

    def recommendations(self):
        for i in self.stuff_log:
            i.recommend()

    def current_info(self):
        for i in self.stuff_log:
            i.show()

    def shw_plist(self):
        for i in list(range(len(self.stuff_log))):
            print("{0}  : {1.name}  ".format(i, self.stuff_log[i]))

    def add_new(self, name, route, vol, vol_per, a_price):
        S = Stuff(name, vol, route, a_price, vol_per)
        S.update()
        self.stuff_log.append(S)

    def delStuff(self, index):
        self.stuff_log.pop(index)

    def adjust(self, index, price):
        self.stuff_log[index].adjust(price)
