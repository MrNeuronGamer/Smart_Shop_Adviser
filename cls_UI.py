from cls_engine import Engine


class my_UI(object):
    G = Engine()

    def actions(self):
        offer = ['1 - Show current info', '2 - Show current recommendations', '3 - Delete log', '4 - Add new log',
                 '5 - Refresh data', '6 - Adjust log', '7 - Quit']
        print(offer, sep='\n')

    def run(self):
        self.G.read()

    def off(self):
        self.G.save()
        print("Have a nice day, Sir! :) ")

    def routine(self):

        self.actions()
        key = int(input("What would you like to perform?\n"))

        if key == 7:
            return False
        elif key == 1:
            self.G.current_info()
            return True
        elif key == 2:
            self.G.recommendations()
            return True
        elif key == 3:
            self.G.shw_plist()
            key = int(input("Which one is to be deleted? \n"))
            self.G.delStuff(key)
            return True
        elif key == 4:
            print(" Please, answer the following questions:\n")

            name = input("What is the name of the stuff : ")
            route = input("What is its web address : ")
            route = route.strip()
            vol = int(input("How much (int) of stuff : "))
            vol_per = input("What units are to be used (kg,g, l )  :  ")
            a_price = float(input("What is its Auchan price : "))
            self.G.add_new(name, route, vol, vol_per, a_price)
            return True
        elif key == 5:
            self.G.update()
            return True
        elif key == 6:
            self.G.shw_plist()  # Actually , I don't give a shit (a.k.a. to be implemented later)
            key = int(input("Which one? \n"))
            new_price = float(input("Please input new price for the selected stuff:\n "))
            self.G.adjust(key, new_price)
            return True
