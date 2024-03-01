from tkinter import *
def click1():
    etiqueta['text']= ' botão 1'
janela =  Tk()
janela.title("Empresa")
janela.iconbitmap('Icon.ico')
janela['background']=('RoyalBlue')
etiqueta=Label(janela, text='Olá Mundo',bg='RoyalBlue',cursor='dot')
etiqueta.pack()
botao=Button(janela,text="Botão 1", padx='50' , pady= '30', command=click1)
botao.pack()
janela.geometry('500x400+50+20')
janela.mainloop()