#Calculadora de somarfrom tkinter import *


def click1():
    x=entrada1.get()
    y=entrada2.get()
    if x.isnumeric() and y.isnumeric():
        z=int(x)+int(y)
        etiqueta['text']=z
    else:
        etiqueta['text']="Entre dados válidos"   

janela =  Tk()
janela.title("Calculadora")
janela.iconbitmap('Icon.ico')
janela['background']=('RoyalBlue')
etiqueta1=Label(janela, text='Primeiro número:',bg='RoyalBlue')
etiqueta1.pack()
entrada1=Entry(janela,width=20)
entrada1.pack()
etiqueta2=Label(janela, text='Segundo número:',bg='RoyalBlue')
etiqueta2.pack()
entrada2=Entry(janela,width=20)
entrada2.pack()
etiqueta=Label(janela, text='  ',bg='RoyalBlue')
etiqueta.pack()
botao=Button(janela,text="Somar", padx='10' , pady= '5',command=click1 )
botao.pack()
janela.geometry('500x400+50+20')
janela.mainloop()