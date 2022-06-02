from tkinter import *
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
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
        self.ent.place(x=176,y=220,height=35)
        # txt.insert(entg,'insert')
        self.img = ImageTk.PhotoImage(Image.open('Bitcoin.png'))
        self.img1 = ImageTk.PhotoImage(Image.open('Ethereum.png'))
        self.img2 = ImageTk.PhotoImage(Image.open('Tether.png'))
        self.lab1=Label(master, image=self.img, bg='#D3DED2', bd=0)
        self.lab1.place(x=193,y=330)
        self.lab2 = Label(master, image=self.img1, bg='#D3DED2', bd=0)
        self.lab2.place(x=46, y=370)
        self.lab1 = Label(master, image=self.img2, bg='#D3DED2', bd=0)
        self.lab1.place(x=340, y=370)
        self.lab=Label(master,text='CryptoParser',bg='#EE751C',font=('Impact',40),justify='center')
        self.lab.place(x=112,y=12)
        self.but=Button(master, text='Парсить!', bg='#2FA07B', fg='#E8DD2D',command=self.click)
        self.but.place(x=226,y=290)


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
                return f"Название - {name}\nИнициалы - {sym}\nЦена - {round(price,2)}$\nИзменения за последний час: {round(item['quotes'][0]['percentChange1h'],2)}%\nИзменения за 24 часа: {round(item['quotes'][0]['percentChange24h'],2)}%"
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
