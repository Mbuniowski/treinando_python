#vamos criar um loyout igual o modelo apresentados a cor fica a seu criterio, colocar um ,botão e uma
#label.Deve ser trocado o ícone para um de sua escolha.Tamanho da janela:500x400+50+200

from tkinter import *
def click1():
    etiqueta['text']= "Olá "+ entrada.get()
janela =  Tk()
janela.title("Empresa")
janela.iconbitmap('Arvore.ico.ico')
janela['bg']=('#FF69B4')
janela.geometry('500x400+50+200')
entrada=Entry(janela,width=80)
entrada.pack()
entrada.get()
etiqueta=Label(janela, text='Olá Michelle',bg= '#FF69B4',cursor='dot')
etiqueta.pack()
botao=Button(janela,bg='light blue',text=" Click ", padx='80' , pady= '20', command= click1)
botao.pack()
janela.mainloop()

#programa para clicar no botão click trocar o mnome michelle para ola