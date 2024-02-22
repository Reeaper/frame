from tkinter import *

janela=Tk()
janela.geometry('500x400+50+200')
janela.iconbitmap('icons8-capivara-48.ico')
janela.title('ListBox')

def selecao():
    tag['text']=lista.get(ANCHOR)

lista=Listbox(janela)
lista.pack()
mylist=['SP','RJ','MG']

for item in mylist:
    lista.insert(END,item)

btn=Button(janela,text='Finalizar',command=selecao)
btn.pack()

tag=Label(janela,text=' ')
tag.pack()

janela.mainloop()