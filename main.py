# Main
import Api
import Item
import Tkinter as tk
import thread
import time
from gui import ItemListBox, ItemEntry


class App():
    
    def __init__(self, root):
        self.root = root
        self.api = Api.Api()
        self.master = tk.Frame(root)
        self.master.grid()
        self._build_widgit()
        
        thread.start_new(self.updateFound,())
        self.root.mainloop()

    def _build_widgit(self):
        self.infoFrame = tk.Frame(self.master)
        self.foundFrame = tk.Frame(self.master)
        self.trackedFrame = tk.Frame(self.master)
        self.itemEntryFrame = tk.Frame(self.master)
        self.listButtonFrame = tk.Frame(self.master)

        self.infoFrame.grid(       row = 0, column = 1)
        self.itemEntryFrame.grid(  row = 1, column = 1)
        self.foundFrame.grid(      row = 2, column = 1)
        self.listButtonFrame.grid( row = 2, column = 2)
        self.trackedFrame.grid(    row = 2, column = 3)
        
        # Found Box
        self.foundList = ItemListBox(self.foundFrame, [])
        self.foundFrame.grid()
        
        # Tracked Box
        self.trackedList = ItemListBox(self.trackedFrame, [])
        self.trackedFrame.grid()

        # Item Entry
        self.itemEntry = ItemEntry(self.itemEntryFrame)
        self.itemEntryFrame.grid(row = 1)

        # Add Button
        self.addButton = tk.Button(self.listButtonFrame, text = " >>> ")
        self.addButton.grid(row = 1)
        
        # Remove Button
        self.removeButton = tk.Button(self.listButtonFrame, text = " <<< ")
        self.removeButton.grid(row = 2)
        
        # Info Screen

    
    def updateFound(self):
        while True:
            print "Checking!"
            if (self.itemEntry.check()):
                new_alpha = self.itemEntry.getText()
                self.foundList.clearAll()
                if new_alpha == "":
                    pass
                else:
                    for c_id in xrange(1,23):
                        for page_num in xrange(1,10):
                            try:
                                items = self.api.getCatalog(c_id,new_alpha,page_num)
                                for item in self.api.getCatalog(c_id,new_alpha,page_num):
                                    self.foundList.add(item)
                            except ValueError:
                                pass
            time.sleep(1)

    def addToTracked(self):
        pass

    def removeFromTracked(self):
        pass

    def updateInfo(self):
        pass

    def saveTracked(self):
        pass
      
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
