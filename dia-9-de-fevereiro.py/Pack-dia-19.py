'''
from tkinter import *
janela =  Tk()

etiqueta1=Label(janela, text='Etiqueta 1:',bg='RoyalBlue')
etiqueta1.pack(fill= X)
etiqueta2=Label(janela, text='Etiqueta 2:',bg='pink')
etiqueta2.pack(side=LEFT, fill= BOTH)
etiqueta=Label(janela, text='Etiqueta 3 :',bg='yellow')
etiqueta.pack(expand=1 ,fill= BOTH)




janela.geometry('500x500+100+100')
janela.mainloop()

'''

from tkinter import *
janela =  Tk()

etiqueta1=Label(janela, text='A:',)
etiqueta1.pack(side=LEFT,)
etiqueta2=Label(janela, text='B:',)
etiqueta2.pack(side=BOTTOM)
etiqueta3=Label(janela, text='C:',)
etiqueta3.pack(side =RIGHT ,)
etiqueta=Label(janela, text='D:',)
etiqueta.pack(side= TOP)

janela.geometry('500x500+100+100')
janela.mainloop()
