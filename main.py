from tkinter import *
from tkinter import Tk

#cores
cor1 = "#141414" # preta
cor2 = "#2a435e" # azul
cor3 = "#ffffff" # Branco
cor4 = "#424242" # Cinza
cor5 = "#db4b12" # laranja Lamborghini

#Tela
janela =Tk()
janela.title("Calculater")
janela.geometry("500x500")
janela.config(bg=cor1)

#Frames
frame_tela = Frame(janela, width= 500, height= 90, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 500, height= 45)
frame_corpo.grid(row=1, column=0)



janela.mainloop()

