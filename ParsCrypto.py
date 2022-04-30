from tkinter import *


class MyWindow:
    def __init__(self, master):
        self.master = master
        self.master.resizable(height=False,width=False)
        self.master.title('CryptoPars')
        self.master.iconphoto(True, PhotoImage(file=('Bitcoin-icon.png')))
        self.master.geometry('512x512')
        self.master["bg"] = '#D3DED2'
        self.txt = Text(self.master, font=('Courier New', 10), bg='#9C9C9C',width=32, height=12)
        self.txt.place(x=64,y=256)
        self.ent=Entry(self.master, font=('Courier New', 10), bg='#9C9C9C', justify='center')
        self.ent.place(x=64,y=128,height=35)
        self.lab=Label(self.master,text='CryptoParser',bg='#EE751C',font=('Impact',40),justify='center')
        self.lab.place(x=112,y=12)
    def info(self):
        requests = requests.get(url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000').json()
        for item in requests['data']['cryptoCurrencyList']:
            if item.get('name') == self:
                name = item['name']
                sym = item['symbol']
                totalSupply = item['totalSupply']
                price = item['quotes']['price']
                print(f'Название - {name}'
                      f'Инициалы - {sym}'
                      f'Цена - {price}'
                      )





if __name__ == '__main__':
    root = Tk()
    win = MyWindow(root)
    root.mainloop()
