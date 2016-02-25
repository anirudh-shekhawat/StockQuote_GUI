#A python script for getting quotation for any stock across any index worlwide.
#Author:Anirudh S Shekhawat

from Tkinter import *
from googlefinance import getQuotes
from yahoo_finance import Share
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import json
import operator
from twilio.rest import TwilioRestClient

account_sid = "AC54f90f68ef524ec1d8dbc654a36f321b"  #Enter your Twilio account sid
auth_token  = "bdb3e1f9439208868c1588647faa759b"    #Enter your Twilio auth token
from_number = "+12027988108"   #Enter your Twilio number
to_number = "+917506399694"    #Enter the recepient's number 
client = TwilioRestClient(account_sid, auth_token)

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
        mes="Quote for "+index+" indexed on "+stock+" is "+parsed_json[0]['LastTradeWithCurrency']+" timestamp "+parsed_json[0]['LastTradeDateTimeLong']
        client.messages.create(
        to=to_number, 
        from_=from_number, 
        body=mes
        )
        yfinance=Share(index)
        historic_data=yfinance.get_historical('2015-11-01','2015-12-31')
        stock_high_values=map(operator.itemgetter('High'),historic_data)
        stock_trading_date=map(operator.itemgetter('Date'),historic_data)
        plt.plot(stock_high_values)
        plt.show()
        
        
        

root = Tk()
root.iconbitmap(default='transparent.ico')
root.title('Get Stock Quote')
app = App(root)

root.mainloop()
root.destroy()