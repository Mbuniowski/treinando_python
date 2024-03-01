from tkinter import *
janela =  Tk()

def selecao():
    etq['text']=lista.get(ANCHOR)
    
lista = Listbox(janela)
lista.pack()
minhalista=['São Paulo','Rio de Janeiro','Minas Gerais']

for item in minhalista:
        lista.insert(END,item)

botao=Button(janela,text=" selecionado ", command=selecao )
botao.pack()
etq=Label(janela, text='  ')
etq.pack()






janela.geometry('500x400+50+200')
janela.mainloop()