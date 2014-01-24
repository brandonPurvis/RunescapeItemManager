#Item List

class ItemList:
    def __init__(self):
        self.itemList = []

    def add(item):
        if item not in self.itemList:
            self.itemList.append(item)

    def remove(item):
        self.itemList.remove(item)

    def update():
        for item in itemList:
            item.update()

    def getProfitable():
        item_profit = []
        for item in self.itemList:
            profit = item.getProfit()
            item_profit.append((item, profit))
        return sorted(item_profit,key=lambda x:x[1],reverse=True)

if __name__ == "__main__":
    pass
