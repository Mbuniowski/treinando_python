from tkinter import *
#cria formulario
formulario= Tk()
formulario.title = "Desenvolvimento Aberto"
#Evento do botão 
def clique():
    texto.set(mostraValor + str(slider.get()))

#Declara variaveis
texto = StringVar()
mostraValor = "Valor escolhido: "

#Declaração componentes
titulo = Label(formulario,text = "Desenvolvimento Aberto - Scale")        
valor = Label(formulario,textvariable = texto)
slider = Scale(formulario,from_ = 1,to = 50, orient=HORIZONTAL)
botao = Button(formulario, text="ok",command= clique)

#Adiciona propriedades
texto.set(mostraValor)
slider.set(25)

#Exibe componentes no formulario
titulo.grid(row=0, sticky=W, padx=10, pady=20)
valor.grid(row=1, sticky=W, padx=10)
slider.grid(row=2, sticky=W, padx=10)
botao.grid(row=3, sticky=W, padx=10, pady=20)

#Loop do tcl
mainloop