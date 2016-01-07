#A python script for getting quotation for any stock across any index worlwide.
#Author:Anirudh S Shekhawat
from Tkinter import *
from googlefinance import getQuotes
import json

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.entry=Entry(frame,width=60)
        self.entry.pack(side=LEFT)
        self.entry.focus_set()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=RIGHT)

        self.quote = Button(frame, text="Get quote for the specified stock and index",fg="blue", command=self.get_quote)
        self.quote.pack(side=LEFT)

    def get_quote(self):
        text=self.entry.get()
        s=text.split()
        stock=s[0]
        index=s[1]
        final_quote=stock+":"+index
        print json.dumps(getQuotes(final_quote),indent=2)

root = Tk()

app = App(root)

root.mainloop()
root.destroy()