from tkinter import *

janela=Tk()
janela.geometry('500x400+50+20')
janela.iconbitmap('icons8-capivara-48.ico')
janela.title('frame')

frame1=LabelFrame(janela,padx=20,pady=20,bg='#FFF0F5',text='Frame1')
frame1.pack()

tag=Label(frame1,text='Tag 1')
tag.pack()

btn1=Button(frame1,text='Click')
btn1.pack()

frame2=LabelFrame(janela,padx=20,pady=20,bg='#D8BFD8',text='Akira')
frame2.pack()
tag2=Label(frame2,text='Yuki')
tag2.pack()

btn2=Button(frame2,text='Click')
btn2.pack()

janela.mainloop()