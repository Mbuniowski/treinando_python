#Combo Box
from tkinter import *
from tkinter import ttk
jn=Tk()

#criação do def
def clicado(event):
    Etq1=Label(jn,text=caixaSel.get()).pack()

#criação da comboBox
caixaSel=ttk.Combobox(jn, value=[" ","Casado","Solteiro","Divorciado","Viuvo" ])
caixaSel.current(0)# é responsavel para saber qual o valor que eu quero que apareça

#criação do evento
caixaSel.bind("<<ComboboxSelected>>",clicado)
caixaSel.pack()




jn.geometry('500x400+50+200')
jn.mainloop()