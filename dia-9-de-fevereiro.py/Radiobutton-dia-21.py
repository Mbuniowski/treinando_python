# Radiobutton e somente permite o usuario uma unica opção 
from tkinter import*
janela = Tk()
def sel():
    Selecionado = "Você selecionou a opção"+ str(var.get())
    etq['text']=Selecionado
janela.title('Caixa de seleção',)
janela.iconbitmap('casa.ico.ico',)

var= IntVar()
Rb1=Radiobutton(janela, text='Opção 1',variable=var,value=1)
Rb1.pack()


Rb2=Radiobutton(janela, text='Opção 2',variable=var,value=2)
Rb2.pack()

Rb3=Radiobutton(janela, text='Opção 3',variable=var,value=3)
Rb3.pack()

btn=Button(janela,text='Selecionar',bg='light blue',command=sel)
btn.pack()

etq = Label(janela, text= ' ')
etq.pack()

janela.geometry('500x400+50+200')
mainloop()