
from tkinter import *
janela =  Tk()

frame1 = LabelFrame(janela, padx=20,pady=20, bg='pink',text='')
frame1.grid(row=0, column=0)
etiqueta=Label(frame1,text="Etiqueta 1")
etiqueta.pack()
bt1=Button(frame1, text='Botão 1')
bt1.pack()

frame2 = LabelFrame(janela, padx=20,pady=20, bg='blue',text='')
frame2.grid(row=0,column=1)
etiqueta2=Label(frame2,text="Etiqueta 2")
etiqueta2.pack()
bt2=Button(frame2, text='Botão 2')
bt2.pack()

janela.geometry('500x400+50+200')
janela.mainloop()