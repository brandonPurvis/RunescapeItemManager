import Tkinter as tk

class ItemListBox(tk.Frame):

    def __init__(self, master, item_list):
        self.item_list = item_list
        self.main = tk.Frame(master)
        self.main.grid()
        self._build_widget()
        self.cur_end = 0
        self._build_widget()
        self.update()

    def _build_widget(self):
        self.scrollbar  = tk.Scrollbar(self.main)
        self.scrollbar.grid(row = 0, column = 1, sticky = tk.N + tk.S)

        self.list_box = tk.Listbox(self.main, yscrollcommand = self.scrollbar.set)
        self.list_box.grid(row = 0, column= 0)
        
    def update(self):
        self.list_box.delete(0,tk.END)
        for index, item in enumerate(self.item_list):
            self.list_box.insert(index, item)

    def add(self, item):
        self.item_list.append(item)
        self.update()

    def remove(self, item):
        self.item_list.remove(item)
        self.update()

    def get(self):
        indexes = map(int,self.list_box.curselection())
        return [self.item_list[i] for i in indexes]

    def clearAll(self):
        self.item_list = []
        self.update()
    
if __name__ == "__main__":
    root = tk.Tk()
    ilist = ["one", "two", "three"]
    app = ItemListBox(root, ilist)
    app.add("eighty")
    app.remove("two")
    root.mainloop()
