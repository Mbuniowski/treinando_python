#BARRA DE ROLAGEM

from tkinter import*
janela = Tk()
def selecao():
    etq['text']=' Local é  ' + lista.get(ANCHOR)

et2= Label(janela,text='Qual estado você mora?')    
et2.pack()
frame = Frame(janela)
scrollbar=Scrollbar(frame,orient= VERTICAL)
lista=Listbox(frame, width=20, height=5,yscrollcommand=Scrollbar.set)
scrollbar.config(command=lista.yview)
scrollbar.pack(side= RIGHT, fill=Y)
frame.pack()
lista.pack()
minhalista=['São Paulo','Rio de Janeiro','Minas Gerais','Paraná','Mato Grosso','Amazonas']

for item in minhalista:
    lista.insert(END, item)

btn=Button(janela,text='Selecionado', command=selecao)  
btn.pack() 
etq=Label(janela,text='')
etq.pack()
janela.geometry('500x400+50+200')
janela.mainloop()
