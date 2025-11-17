class Vending:
    def __init__(self, name, list):
        self.name = name
        self.list = list

    def getList(self):
        return self.list

class Beverage:
    def __init__(self, beverage, cost):
        self.beverageName = beverage
        self.cost = cost

    def getName(self):
        return self.beverageName
    def getCost(self):
        return self.cost

beverage1 = Beverage("Pepsi", 2.00)
beverage2 = Beverage("Coca Cola", 2.00)
beverage3 = Beverage("Sprite", 2.00)
beverage4 = Beverage("Dr. Pepper", 2.00)
beverage5 = Beverage("Fanta", 2.00)
beverage6 = Beverage("Water", 1.50)
bevList = [beverage1, beverage2, beverage3, beverage4, beverage5, beverage6]
machine1 = Vending("Halo's Vending Machine", bevList)

print("Welcome to Halo's Vending Machine. Here are your options:")
for bev in machine1.getList():
    print(str(bev.getName()) + ": " + str(bev.getCost()))

while True:
    option = str(input("(Case Sensitive) Select an option.\n"))
    if option in [beverage1.getName(), beverage2.getName(), beverage3.getName(), beverage4.getName(), beverage5.getName()]:
        pay = str(input("Please insert $2.00:\n"))
        if float(pay) < 2.0:
            print("Please try again")
        if float(pay) > 2.0:
            print("You input more than needed. Please try again")
        if float(pay) == 2.0:
            print("You have received:")
            if option == beverage1.getName():
                print(beverage1.getName())
            if option == beverage2.getName():
                print(beverage2.getName())
            if option == beverage3.getName():
                print(beverage3.getName())
            if option == beverage4.getName():
                print(beverage4.getName())
            if option == beverage5.getName():
                print(beverage5.getName())
    elif option == beverage6.getName():
        pay = str(input("Please insert $1.50:\n"))
        if float(pay) < 1.5:
            print("Please try again")
        if float(pay) > 1.5:
            print("You input more than needed. Please try again")
        if float(pay) == 1.5:
            print("You have received:")
            print(beverage6.getName())



