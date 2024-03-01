from tkinter import *
janela = Tk()
def selecao():
    nome=entrada1.get()
    if var1.get() ==1:
     x="Python"
    else:
     x=" "
    if var2.get() ==1:
     y="Java"

    else:
     y=" "
    if var3.get()==1:
     z="C#" 
    else:
     z=" "     
    if var.get()==1:
     w="Masculino"

    if var.get()==2:
     w="Feminino"
    etq['text']= nome + " " + w + ' ' + lista.get(ANCHOR) + "  " +  x  +  y  +  z


etq=Label(janela, text='Qual o seu nome?')
etq.pack()

entrada1=Entry(janela,width=50)
entrada1.pack()

etq=Label(janela,text='Qual o sexo?')
etq.pack()

var=IntVar()
var.set(1)
rb1=Radiobutton(janela,text=' Masculino',variable=var, value=1)
rb1.pack()

rb2=Radiobutton(janela, text= 'Feminino',variable=var, value=2)
rb2.pack()

et4=Label(janela)
et4.pack()
etq2=Label(janela,text='Qual unidade do curso?')
etq2.pack()

#lISTEBOX
frame=Frame(janela)
Scrollbar=Scrollbar(frame,orient=VERTICAL)
lista=Listbox(frame,width=50,height=5,yscrollcommand=Scrollbar.set)
Scrollbar.config(command=lista.yview)
Scrollbar.pack(side=RIGHT,fill=Y)
frame.pack()
lista.pack()
minhalista=['São Paulo','Rio de Janeiro','Minas Gerais','Paraná','Mato Grosso','Ceará','Amazonas']

for item in minhalista:
        lista.insert(END,item)

etq5=Label(janela)
etq5.pack()
etq3=Label(janela,text='Qual o curso?')
etq3.pack()

Frame2=Frame(janela)
Frame2.pack()
var1=IntVar()
CB1= Checkbutton(Frame2,text = "Python" , variable = var1)
CB1.pack(anchor = 'w')

var2=IntVar()
CB2= Checkbutton(Frame2,text = "JAVA" , variable = var2)
CB2.pack(anchor = 'w')

var3=IntVar()
CB3= Checkbutton(Frame2,text = "C#" , variable = var3)
CB3.pack(anchor = 'w')

et6=Label(janela)
et6.pack()
bt1=Button(janela, text='Selecionado',command=selecao )
bt1.pack()

etq=Label(janela,text= "   ")
etq.pack()


           
janela.geometry('500x500+50+200')
janela.mainloop()
