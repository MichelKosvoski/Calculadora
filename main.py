from tkinter import *
from tkinter import Tk

#cores
cor1 = "#3b3b3b" # preta
cor2 = "#feffff" # Branco
cor3 = "#38576b" # azul
cor4 = "#ECEFF1" # Cinza
cor5 = "#d1992a" # laranja Lamborghini

#Tela
janela =Tk()
janela.title("Calculater")
janela.geometry("235x310")
janela.config(bg=cor1)
janela.resizable(False,False)

#Frames
frame_tela = Frame(janela, width= 235, height= 50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 235, height= 268)
frame_corpo.grid(row=1, column=0)





# Criando Butoes
Button_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_1.place(x=0, y=0)

Button_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_2.place(x=118, y=0)

Button_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=0)


Button_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=0, y=52)
Button_4 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=59, y=52)
Button_4 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=118, y=52)
Button_3 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=52)


Button_4 = Button(frame_corpo, text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=0, y=104)
Button_4 = Button(frame_corpo, text="5", width=5, height=2, bg=cor4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=59, y=104)
Button_4 = Button(frame_corpo, text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=118, y=104)
Button_3 = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=104)



Button_4 = Button(frame_corpo, text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=0, y=156)
Button_4 = Button(frame_corpo, text="2", width=5, height=2, bg=cor4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=59, y=156)
Button_4 = Button(frame_corpo, text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=118, y=156)
Button_3 = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=156)

Button_4 = Button(frame_corpo, text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=0, y=208)
Button_4 = Button(frame_corpo, text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=118, y=208)
Button_3 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=208)










janela.mainloop()

