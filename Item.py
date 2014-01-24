# Item
import Api

class Item:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name
        self.price = 0
        self.alchemy = 0

    def setAlchemy(self, value):
        self.alchemy = value
        
    def getProfit(self):
        return self.alchemy - self.price
    
    def update(self, api):
        self.price = api.getItemPrice(self.id)
        
    def __str__(self):
        return "{} {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    pass
