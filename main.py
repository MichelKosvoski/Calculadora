from tkinter import *
from tkinter import Tk

#cores
cor1 = "#141414" # preta
cor2 = "#2a435e" # azul
cor3 = "#ffffff" # Branco
cor4 = "#424242" # Cinza
cor5 = "#d1992a" # laranja Lamborghini

#Tela
janela =Tk()
janela.title("Calculater")
janela.geometry("500x500")
janela.config(bg=cor1)

#Frames
frame_tela = Frame(janela, width= 500, height= 85, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 500, height= 45)
frame_corpo.grid(row=1, column=0)


# Criando Butoes

Button_on_of = Button(frame_corpo, text="On/Off", width=12, height=3)
Button_on_of.place(x=0, y=0)

Button_1 = Button(frame_corpo, text="C", width=12, height=3, bg=cor4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
Button_1.place(x=219, y=0)

Button_2 = Button(frame_corpo, text="%", width=12, height=3, bg=cor4 , font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
Button_1.place(x=219, y=0)
Button_2.place(x=312, y=0)

Button_1 = Button(frame_corpo, text="/", width=12, height=3, bg=cor5, fg=cor3, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
Button_1.place(x=219, y=0)
Button_1.place(x=406, y=0)





janela.mainloop()

