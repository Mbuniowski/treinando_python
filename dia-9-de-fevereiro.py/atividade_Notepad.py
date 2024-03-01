#criação da janela
import tkinter 
#criação da variavel da janela
window=tkinter.Tk()
#criação da função def
def Novo():
    text_area.delete(1.0,"end")

def Abrir():
    file=open('notepad.txt', 'r')
    container= file.read()
    text_area.insert(1.0,container)

def Salvar():
    container=text_area.get(1.0,"end")
    file=open("notepad.txt","w")
    file.write(container)
    file.close()
 
 #def update  
def Update():
     font=spin_font.get()   
     size=spin_size.get() 
     text_area.config(font="{} {}".format(font,size))

#criação do titulo
window.title("Notepad")

#definição do tamanho da janela
window.wm_minsize(width=1200,height=800)

#barra de ferramentas
frame=tkinter.Frame(window, height=30)#Inicio da frame
frame.pack(fill="x")#final da frame

#tipo de fonte
fonte_text=tkinter.Label(frame,text="Fonte: ")
fonte_text.pack(side="left")

#Spinbox
spin_font=tkinter.Spinbox(frame,values=("Arial","Verdana","Vladimir Script","Bradley Hand ITC",
                                        "Algerian","8514oem","Jokerman","Jokerman"))
spin_font.pack(side="left")

#tamanho da fonte
font_size=tkinter.Label(frame,text="Fonte Size:")
#Spinbox2
font_size.pack(side="left")
spin_size =tkinter.Spinbox(frame,from_=0, to=60)
spin_size.pack(side="left")

#criando o botão update
btn=tkinter.Button(frame, text="Up",command=Update)
btn.pack(side="left")

#criação area do texto
text_area=tkinter.Text(window,font="Arial 20 bold", width=1200, height=800)
text_area.pack()

#criação do menu
main_menu=tkinter.Menu(window)
arquivo_menu=tkinter.Menu(main_menu,tearoff=0)
arquivo_menu.add_command(label="Novo",command=Novo)
arquivo_menu.add_command(label="Abrir",command=Abrir)
arquivo_menu.add_command(label="Salvar",command=Salvar)
arquivo_menu.add_command(label="Fechar",command= window.quit)
main_menu.add_cascade(label='Arquivo',menu=arquivo_menu)
window.config(menu=main_menu)

#criação do botão novo
arquivo_menu.add_command(label="Novo")





#final do programa
window.mainloop()