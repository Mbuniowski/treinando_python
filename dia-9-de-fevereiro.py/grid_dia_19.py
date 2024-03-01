from tkinter import *
janela =  Tk()

lb1=Label(janela, text= 'Login')
lb1.grid(column=0, row=0)
lb2=Label(janela, text = 'Senha')
lb2.grid(column=0, row=1)

En1=Entry(janela)
En1.grid(column=1,row=0, padx=(50,50),pady=(50,50))
En2=Entry(janela)
En2.grid(column=1,row=1,padx=(50,50),pady=(10,10))

botao1=Button(janela, text="Avançar" )
botao1.grid(column=0, row=2, columnspan= 2)


janela.geometry('500x400+50+20')
janela.mainloop()