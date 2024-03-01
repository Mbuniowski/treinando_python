from tkinter import *
janela =  Tk()
etiqueta=Label(janela, font=20,text='Olá Michelle',cursor='dot')
etiqueta.pack()
janela.geometry('500x400+50+20')
botao=Button(janela,bg='light blue',text=" Fechar ", padx='30' , pady= '20',command=janela.quit)
botao.pack()
janela.mainloop()