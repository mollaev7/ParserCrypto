from tkinter import *
import requests
from tkinter import messagebox

class MyWindow:
    def __init__(self,master):
        self.master = master
        self.master.resizable(height=False,width=False)
        self.master.title('CryptoPars')
        self.master.iconphoto(True, PhotoImage(file=('Bitcoin-icon.png')))
        self.master.geometry('512x512')
        self.master["bg"] = '#D3DED2'
        # txt = Text(master, font=('Courier New', 10), bg='#9C9C9C',width=32, height=12)
        # txt.place(x=64,y=256)
        self.cry=StringVar()

        self.ent=Entry(master, font=('Courier New', 10), bg='#9C9C9C',textvariable=self.cry)
        self.ent.place(x=64,y=128,height=35)
        # txt.insert(entg,'insert')
        self.lab=Label(master,text='CryptoParser',bg='#EE751C',font=('Impact',40),justify='center')
        self.lab.place(x=112,y=12)
        self.but=Button(master, text='Парсить!', bg='#2FA07B', fg='#E8DD2D',command=self.click)
        self.but.place(x=64, y=170)

    def get_info(self):
        request = requests.get(url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000').json()
        for item in request['data']['cryptoCurrencyList']:
            if item.get('name').lower() == self.cry.get().lower():
                name = item['name']
                sym = item['symbol']
                price = item['quotes'][0]['price']
                    # print(f'Название - {name}'
                    #       f'Инициалы - {sym}'
                    #       f'Цена - {price}'
                    #       )
                total = f'Название - {name}\nИнициалы - {sym}\nЦена - {round(price, 2)}'
                return f'Название - {name}\nИнициалы - {sym}\nЦена - {round(price,2)}$'
                # self.lab=Label(self.master, text='total')
                # self.lab.place(x=0,y=0)
            else:
                pass
    def click(self):
        messagebox.showinfo('Курс валюты', self.get_info())


if __name__ == '__main__':
    root=Tk()
    win=MyWindow(root)
    root.mainloop()
