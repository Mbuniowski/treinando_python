from tkinter import*
janela = Tk()
def funcao():
    if var1.get()==1:
        etq1['text']= 'Opção 1 selecionada'
    else:
        etq1['text']= '' 
    if var2.get()== 1:
        etq2['text'] = 'Opção 2 selecionada'  
    else:
        etq2['text']=''   

janela.title('Caixa de seleção',)
janela.iconbitmap('casa.ico.ico',)

var1 = IntVar()
Checkbutton(janela, text="opção 1 ",variable=var1).grid(row=0, padx=220)
var2 = IntVar()
Checkbutton(janela,text="opção 2 ",variable=var2).grid(row=1, padx=220)

btn=Button(janela,text='Selecionar',bg='light blue',command=funcao)
btn.grid()

etq1 = Label(janela, text= ' ')
etq1.grid()
etq2= Label(janela, text= ' ')
etq2.grid()

janela.geometry('500x400+50+200')
mainloop()