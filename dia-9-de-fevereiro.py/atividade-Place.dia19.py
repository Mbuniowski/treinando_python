#PLACE#

#--Vamos construir uma janela no tamanho 800x500x100x100

from tkinter import *
janela =  Tk()


botao1=Button(janela, text="botao 1" )
botao1.place(x=400, y=300, anchor= NE)

botao2=Button(janela, text="botao 2" )
botao2.place(x=400, y=250, anchor = E)

botao3=Button(janela, text="botao 3" )
botao3.place(x=450, y=300, anchor= NW)
en=Entry(janela)
en.place(x=450,y =250,anchor=NW)
janela.geometry('500x400+50+20')
janela.mainloop()