from tkinter import *


class MyWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('CryptoPars')
        self.master.iconphoto(True, PhotoImage(file=('Bitcoin-icon.png')))
        self.master.geometry('512x512')
        self.master["bg"] = '#D3DED2'
        self.txt = Text(self.master, font=('Courier New', 10), width=32, height=12)
        self.txt.place(x=64,y=256)
        self.ent=Text(self.master, font=('Courier New', 10), height=2)
        self.ent.place(y=64)




if __name__ == '__main__':
    root = Tk()
    win = MyWindow(root)
    root.mainloop()
