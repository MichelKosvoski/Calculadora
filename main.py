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

todos_valores = ""

valor_text = StringVar()

#Criando funções
def entrar_valores(event):
    
    global todos_valores

    todos_valores = todos_valores + str(event)
   

    valor_text.set(todos_valores)


def calcular(): 
    resultado = eval(todos_valores)
    
    valor_text.set(str(resultado))



def clear_tela():
    global todos_valores
    todos_valores =""
    valor_text.set("")






app_Label = Label(frame_tela, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 14 bold'), bg=cor3, fg=cor2)
app_Label.place(x=0, y=0)



# Criando Butoes
Button_1 = Button(frame_corpo, command= clear_tela,text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_1.place(x=0, y=0)

Button_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_2.place(x=118, y=0)

Button_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=0)


Button_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=0, y=52)
Button_4 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=59, y=52)
Button_4 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=118, y=52)
Button_3 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=52)


Button_4 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=0, y=104)
Button_4 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=59, y=104)
Button_4 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=118, y=104)
Button_3 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=104)



Button_4 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=0, y=156)
Button_4 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=59, y=156)
Button_4 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=118, y=156)
Button_3 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=156)

Button_4 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=0, y=208)
Button_4 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_4.place(x=118, y=208)
Button_3 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
Button_3.place(x=177, y=208)


janela.mainloop()

