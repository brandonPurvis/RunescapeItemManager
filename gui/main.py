# GUI main
import Tkinter as tk
from itemlistbox import ItemListBox
from itementry import ItemEntry

class App():

    def updateEntry(self):
        inEntry = self.itemEntry.getText()
        if inEntry:
            self.itemList.add(inEntry)

    def clearList(self):
        self.itemList.clearAll()
        
    
    def __init__(self, root):
        self.testlist = []
        
        self.master = tk.Frame(root)
        self.master.grid()

        self.itemEntry= ItemEntry(self.master)


        self.submitButton = tk.Button(self.master, text="Submit",
                                      command=self.updateEntry)
        self.submitButton.grid()


        self.clearButton = tk.Button(self.master, text="Clear",
                                     command = self.clearList)
        self.clearButton.grid()


        self.itemList = ItemListBox(self.master, self.testlist)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
