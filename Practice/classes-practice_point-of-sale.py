#item and sale and receipt

#Create a class for items in a store
class item:
    def __init__(self, name, price)
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

class cart:
    def __init__(self):
        self.items=[]

    def addItem(self, product):
        self.items.append(product)

    def getTotal(self):
        total=0
        for i in items:
            total += i.price
        return total

    def main():
        more = "y"
        c=cart()
        while more == "y":
            name = input("Item Name: ")
            price = float(input("Item price: "))
            prod=item(name, price)
            c.addItem(prod)
            more = input("Enter 'y' to continue")
        print(c.getTotal)

main()

