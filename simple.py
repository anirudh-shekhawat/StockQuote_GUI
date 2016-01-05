from Tkinter import *
from googlefinance import getQuotes
import json

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.quote = Button(frame, text="Stock Quotation for RPOWER Listed in NSE", command=self.get_quote)
        self.quote.pack(side=LEFT)

    def get_quote(self):
        print json.dumps(getQuotes('BSE:RPOWER'),indent=2)

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below