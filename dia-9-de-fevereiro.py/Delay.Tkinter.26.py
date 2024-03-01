from tkinter import *
janela=Tk()
janela.title("Delay Tkinter")
#método def
def delay():
    etq['text']='Aguarde...'
    janela.after(2000, mensagem)
    # o metodo after rcebe um tempo em millissegundos e uma função que sera executa apos o tempo definido 
def mensagem():
    etq['text']='Botão acionado'

#criação botão
btn=Button(janela,bg="pink",text="Selecionado",padx="40",pady="10",command=delay)
btn.pack()

#criação Label(espaço em branco)
etq1 = Label(janela,text= " ")
etq1.pack()

etq = Label(janela,text= "Botão acionado")
etq.pack()



janela.geometry('500x400+50+200')
janela.mainloop()