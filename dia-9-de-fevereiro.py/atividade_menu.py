from tkinter import *
janela=Tk()

#criação da função arquivo novo
def novo():
    texto1['text']="Novo 1"
    texto2['text']="Novo 2"
#criação da função deletar
def del1():
    texto1['text']=" "   
def del2():
    texto2['text']=" "    
#criação da função edit
def edit1():
    texto1['text']='Editado'
def edit2():
    texto2['text']='Editado'

barraMenu=Menu(janela)
janela.configure(menu=barraMenu)

#menu
menuArquivo=Menu(barraMenu,tearoff=0)
menuExcluir=Menu(barraMenu,tearoff=0)
menuEdit=Menu(barraMenu,tearoff=0)

#cascata
barraMenu.add_cascade(label="Arquivo",menu=menuArquivo)
menuArquivo.add_command(label="Novo",command=novo)
menuArquivo.add_separator()
menuArquivo.add_command(label="Fechar",command=janela.quit)

#excluir
barraMenu.add_cascade(label="Excluir",menu=menuExcluir)
menuExcluir.add_command(label="Excluir 1",command=del1)
menuExcluir.add_separator()
menuExcluir.add_command(label="Excluir 2",command=del2)
#Edit
barraMenu.add_cascade(label="Editar",menu=menuEdit)
menuEdit.add_command(label="Editar 1",command=edit1)
menuEdit.add_separator()
menuEdit.add_command(label="Editar 2",command=edit2)


texto1=Label(janela,text='texto1')
texto1.pack()
texto2=Label(janela,text='texto2')
texto2.pack()



janela.geometry('500x400+50+200')
janela.mainloop()