from tkinter import *
janela=Tk()

#esquerda
def esquerda(event):
    x=-10
    y=0
    tela.move(circulo,x,y)
#direita
def direita(event):
    x=+10
    y=0
    tela.move(circulo,x,y)
#subir
def subir(event):
    x=0
    y=-10
    tela.move(circulo,x,y)  
#descer
def descer(event):
    x=0
    y=+10
    tela.move(circulo,x,y)     
   

janela.geometry('500x400+50+200')
# criação de dimensões do circulo
x=300
y=300
#canva
tela =Canvas(janela,height=600,width=600,bg='white')
tela.pack()
#criação de circulo
circulo=tela.create_oval(x,y, x+10,y+10,fill='blue')

#criação de eventos
janela.bind('<Left>',esquerda)
janela.bind('<Right>',direita)
janela.bind('<Up>',subir)
janela.bind('<Down>',descer)





janela.mainloop()