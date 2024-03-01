from tkinter import *
def click1():
    etiqueta['text']= 'Olá'
def click2():
    etiqueta['text']= 'Michelle'
janela =  Tk()
janela.title("Empresa")
janela.iconbitmap('Icon.ico')
janela['background']=('RoyalBlue')
etiqueta=Label(janela, text='Olá Mundo',bg='RoyalBlue',cursor='dot')
etiqueta.pack()
botao=Button(janela,text="Botão 1", padx='50' , pady= '30', command=click1)
botao.pack()
botao1=Button(janela,text=" Click ", padx='50' , pady= '30', command=click2)
botao1.pack()
janela.geometry('500x400+50+20')
janela.mainloop()