import random
from tkinter import *

class jogar_os_dados(object):


    def __init__(self,mestre):
        quadro = Frame(mestre)
        quadro.pack()

        self.label = Label(mestre, font=("times",200))
        botao=Button(mestre, text="Jogue os dados!", command=self.rolar)
        botao.place(x=200,y=0)

    def rolar(self):
        simbolos=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
        self.label.config(text=f"{random.choice(simbolos)}{random.choice(simbolos)}")
        self.label.pack()

if __name__ == '__main__':
    inicio = Tk()
    inicio.title("Jogue os Dados")
    inicio.geometry("500x300")
    jogar_os_dados(inicio)
    inicio.mainloop()













