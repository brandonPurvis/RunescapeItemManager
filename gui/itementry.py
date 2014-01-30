# ItemEntry

import Tkinter as tk

class ItemEntry(tk.Frame):
    def __init__(self, root):
        self.lastCheck = ""
        self.textVar = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.textVar)
        self.entry.grid()

    def getText(self):
        return self.textVar.get()

    def setText(self, text):
        self.textVar.set(text)

    def check(self):
        if self.lastCheck != self.getText():
            self.lastCheck = self.getText()
            return False
        else:
            return True


if __name__ == "__main__":
    root = tk.Tk()
    app = ItemEntry(root)
    app.setText("Hello World")
    app.setText("The sky is blue")
    print(app.getText())
    root.mainloop()
