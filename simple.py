#A python script for getting quotation for any stock across any index worlwide.
#Author:Anirudh S Shekhawat
from Tkinter import *
from googlefinance import getQuotes
from yahoo_finance import Share
import json

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.entry=Entry(frame,width=60)
        self.entry.pack(side=LEFT)
        self.entry.focus_set()
        
        self.Value_of_stock=StringVar()
        self.time_Stamp_of_stock=StringVar()
        self.display_value=Message(frame,textvariable=self.Value_of_stock,relief=RAISED,aspect=200)
        self.display_value.pack(side=RIGHT)

        self.display_timestamp=Message(frame,textvariable=self.time_Stamp_of_stock,relief=RAISED,aspect=200)
        self.display_timestamp.pack(side=RIGHT)

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
        decoded_json=json.dumps(getQuotes(final_quote))
        parsed_json = json.loads(decoded_json)
        self.Value_of_stock.set(parsed_json[0]['LastTradeWithCurrency'])
        self.time_Stamp_of_stock.set(parsed_json[0]['LastTradeDateTimeLong'])

root = Tk()
root.iconbitmap(default='transparent.ico')
root.title('Get Stock Quote')
app = App(root)

root.mainloop()
root.destroy()