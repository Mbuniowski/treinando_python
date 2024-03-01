#Scale permite o usuario selecione um valor númerico,movendoum botão Slider ao longo de uma 
#escala.Você pode controlar os valores minimos e máximos, bem como a resolução.
from tkinter import *
jn=Tk()
x = Scale(jn, from_=00,to = 100)
x.pack()
#criação do def
def avaliacao():
    Etq= Label(jn,text=f'Avaliação foi {x.get()}').pack()

#botão
bt=Button(jn,text="avaliar", command=avaliacao)
bt.pack()


jn.geometry('500x400+50+200')
mainloop()