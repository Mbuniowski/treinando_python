from tkinter import *
janela=Tk()
#definição do evento
def pintar(event):
    x1,y1=(event.x-3),(event. y-3)
    x2,y2=(event.x+3),(event.y+3)
    tela.create_oval(x1,y1,x2,y2,fill='black')
def limpar():
    tela.delete('all')

tela =Canvas(janela,height=600,width=1200,bg='white')
tela.pack()

#criação de um evento
tela.bind('<B1-Motion>',pintar)
# o B1-Motion define o botão esquerdo do mouse

#criação do botão limpar
bt=Button(janela,text='limpar',command=limpar)
bt.pack()

janela.mainloop()