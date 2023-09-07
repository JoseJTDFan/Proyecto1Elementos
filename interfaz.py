#Elaborado por: Jose Julián Brenes Garro 
#Elementos de Computación
#Proyecto #1
#Versión 3.9.2

#importacion de librerias
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import askyesno
import turtle
import math

#Variables globales


mainWindow=Tk()
mainWindow.config(bg="#4da8cf")
mainWindow.geometry("1000x450")
mainWindow.title("Crear tríangulos")
mainWindow.resizable(True,True)
mainWindow.iconbitmap('triangulo.ico')

canvas = turtle.ScrolledCanvas(mainWindow)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)

t = turtle.RawTurtle(canvas)
t.pensize(2)
t.shape("turtle")
t.color("darkgreen", "green")


def crearTriangulo(LadoA,LadoB,LadoC,Bisec,Alt,Med,Mediat):

        t.clear()
        t.penup()
        t.goto(-150,10)
        t.pencolor("black")
        t.write("Triángulo=Azul\nBisectriz=Morado\nCirculo Inscrito=Rojo\nMediana=Verde\nAltura=Negro\nMediatriz=Naranja", move=False, align="left", font=("Arial", 8, "normal"))
        t.home()
        t.pendown()
        t.setheading(0)

        #Ángulos
        AnguloA = math.degrees(math.acos((LadoB**2 + LadoC**2 - LadoA**2) / (2 * LadoB * LadoC)))
        AnguloB = math.degrees(math.acos((LadoA**2 + LadoC**2 - LadoB**2) / (2 * LadoA * LadoC)))
        AnguloC = math.degrees(math.acos((LadoA**2 + LadoB**2 - LadoC**2) / (2 * LadoA * LadoB)))


        # Dibujar el triángulo
        t.pencolor("blue")
        verticeUno = t.pos()
        t.forward(LadoC)
        t.left(180 - AnguloB)
        verticeDos = t.pos()
        t.forward(LadoA)
        t.left(180 - AnguloC)
        verticeTres = t.pos()
        t.forward(LadoB)

        #Semiperímetro
        s = (LadoA + LadoB + LadoC) / 2

        #Área del triángulo
        area = math.sqrt(s * (s - LadoA) * (s - LadoB) * (s - LadoC))

        #Calcula las coordenadas exactas del centro del triangulo
        CentroX = (LadoA * verticeUno[0] + LadoB * verticeDos[0] + LadoC * verticeTres[0]) / (LadoA + LadoB + LadoC)
        CentroY = (LadoA * verticeUno[1] + LadoB * verticeDos[1] + LadoC * verticeTres[1]) / (LadoA + LadoB + LadoC)

        #Radio
        radio = area / s

        ###################### CIRCULO INSCRITO ######################
        t.penup()
        t.goto(CentroX, CentroY)
        t.pendown()
        t.dot(5,"purple")
        t.penup()
        t.goto(CentroX, CentroY-radio)
        t.left(180-AnguloA)
        t.pendown()
        t.pencolor("red")
        t.circle(radio)

        if(Bisec==1):
                ################################ BISECTRIZ ################################

                t.pencolor("purple")
                t.penup()
                t.goto(CentroX, CentroY)
                t.pendown()
                t.pensize(3)
                t.goto(verticeUno)
                t.penup()
                t.goto(CentroX, CentroY)
                t.pendown()
                t.goto(verticeDos)
                t.penup()
                t.goto(CentroX, CentroY)
                t.pendown()
                t.goto(verticeTres)
                t.pensize(2)

        if (Med==3):
                ################################ MEDIANA ################################
                t.pencolor("green")
                t.penup()
                t.goto(verticeUno)
                t.forward(LadoC/2)
                t.pendown()
                t.goto(verticeTres)

                t.penup()
                t.left(180 - AnguloB)
                t.goto(verticeDos)
                t.forward(LadoA/2)
                t.pendown()
                t.goto(verticeUno)

                t.penup()
                t.left(180 - AnguloC)
                t.goto(verticeTres)
                t.forward(LadoB/2)
                t.pendown()
                t.goto(verticeDos)

        if (Alt==2):
                ################################ ALTURA ################################
                t.penup()
                t.pencolor("black")
                t.goto(verticeTres)
                t.pendown()
                t.goto(verticeTres[0],verticeUno[1])

        if(Mediat==4):
                ################################ MEDIATRICES ################################
                t.pencolor("orange")
                t.setheading(0)
                t.penup()
                t.goto(verticeUno)
                t.forward(LadoC/2)
                t.pendown()
                t.left(90)
                t.forward(LadoA)
                t.backward(LadoA*2)

                t.penup()
                t.goto(verticeDos)
                t.setheading(0)
                t.left(180 - AnguloB)
                t.forward(LadoA/2)
                t.pendown()
                t.left(90)
                t.forward(LadoA)
                t.backward(LadoA*2)


                t.penup()
                t.goto(verticeTres)
                t.setheading(0)
                t.left(180 - AnguloB)
                t.left(180 - AnguloC)
                t.forward(LadoB/2)
                t.pendown()
                t.left(90)
                t.forward(LadoA)
                t.backward(LadoA*2)

def verificarMedidas():
        try:
                #Verifica que el cliente haya llenado todas las casillas
                if LadoUnoEntry.get()=="" or LadoDosEntry.get()=="" or BaseEntry.get()=="":
                        tkinter.messagebox.showerror(title=None,message="Debe ingresar todos los datos")
                        return
                a=int(LadoUnoEntry.get())
                b=int(LadoDosEntry.get())
                c=int(BaseEntry.get())
                if a + b > c and a + c > b and b + c > a:
                        #Activa todo lo necesario para la siguiente parte donde el cliente escoge que rectas quiere ver
                        opcion_1.grid(row=6,column=2,pady=5)
                        opcion_2.grid(row=7,column=2,pady=5)
                        opcion_3.grid(row=8,column=2,pady=5)
                        opcion_4.grid(row=9,column=2,pady=5)
                        LadoUnoEntry.config(state="disabled")
                        LadoDosEntry.config(state="disabled")
                        BaseEntry.config(state="disabled")
                        buttonVerificarMedidas.config(state="disabled")
                        buttonCrearTriangulo.config(state="normal")
                        return
                tkinter.messagebox.showerror(title=None,message="Debe ingresar medidas adecuadas para un triangulo")
                return
        except: 
              #Except por si introduce caracteres no numericos
              tkinter.messagebox.showerror(title=None,message="Debe ingresar solo numeros")
              return

def enviarMedidas():
        #Recoge las medidas que se ocupan y lo que quiere ver el cliente
        a=int(LadoUnoEntry.get())
        b=int(LadoDosEntry.get())
        c=int(BaseEntry.get())
        Bisectriz =control1.get()
        Altura =control2.get()
        Mediana=control3.get()
        Mediatriz=control4.get()
        buttonCambiarMedidas.config(state="normal")
        crearTriangulo(a,b,c,Bisectriz,Altura,Mediana,Mediatriz)

def cambiarMedidas():
        #Desabilita y habilita todo lo necesario para que esté como al principio
        opcion_1.grid_forget()
        opcion_2.grid_forget()
        opcion_3.grid_forget()
        opcion_4.grid_forget()
        LadoUnoEntry.config(state="normal")
        LadoDosEntry.config(state="normal")
        BaseEntry.config(state="normal")
        buttonVerificarMedidas.config(state="normal")
        buttonCrearTriangulo.config(state="disabled")
        buttonCambiarMedidas.config(state="disabled")

#Título
frameTitulo=Frame(mainWindow,width=300,height=100)
frameTitulo.config(bg="#4da8cf")
frameTitulo.pack(fill="y")

#Botones
frame=Frame(mainWindow,width=3000,height=2000)
frame.config(bg="#4da8cf")
frame.pack()

titulo=Label(frameTitulo,text="No soy un círculo vicioso,\n soy un tríangulo amoroso")
titulo.grid(pady=10)
titulo.config(bg="#4da8cf",font=("arial",17,"bold"))

#################### ENTRIES ####################
#Para que el cliente ponga sus medidas
LadoUnoLabel=Label(frame,text="Lado 1")
LadoUnoLabel.grid(row=3,column=1,pady=5)
LadoUnoLabel.config(bg="#66bde6")

LadoUnoEntry=Entry(frame)
LadoUnoEntry.grid(row=3,column=2,pady=5)

LadoDosLabel=Label(frame,text="Lado 2")
LadoDosLabel.grid(row=4,column=1,pady=5)
LadoDosLabel.config(bg="#66bde6")

LadoDosEntry=Entry(frame)
LadoDosEntry.grid(row=4,column=2,pady=5)

BaseLabel=Label(frame,text="Base")
BaseLabel.grid(row=5,column=1,pady=5)
BaseLabel.config(bg="#66bde6")

BaseEntry=Entry(frame)
BaseEntry.grid(row=5,column=2,pady=5)

######################## CHECK BOXES ###########################
#Para que el cliente escoja las líneas que ocupa ver
control1 = IntVar()
control2 = IntVar()
control3 = IntVar()
control4 = IntVar()

opcion_1 = Checkbutton(frame, text="Bisectrices", variable= control1, onvalue=1,offvalue=0)
opcion_1.grid_forget()
opcion_1.config(bg="#66bde6")
opcion_1.deselect()

opcion_2 = Checkbutton(frame, text="Altura", variable= control2, onvalue=2,offvalue=0)
opcion_2.grid_forget()
opcion_2.config(bg="#66bde6")
opcion_2.deselect()

opcion_3 = Checkbutton(frame, text="Medianas", variable= control3, onvalue=3,offvalue=0)
opcion_3.grid_forget()
opcion_3.config(bg="#66bde6")
opcion_3.deselect()

opcion_4 = Checkbutton(frame, text="Mediatrices", variable= control4, onvalue=4,offvalue=0)
opcion_4.grid_forget()
opcion_4.config(bg="#66bde6")
opcion_4.deselect()

#Botón para mandar a verificar las medidas que el cliente mandó
buttonVerificarMedidas=Button(frame,text="Verificar Medidas",command=verificarMedidas)
buttonVerificarMedidas.grid(row=10,column=1,pady=5)
buttonVerificarMedidas.config(bg="#66bde6")

#Botón para enviar las medidas y las lineas que el cliente quiere ver
buttonCrearTriangulo=Button(frame,text="Crear Triángulo",command=enviarMedidas)
buttonCrearTriangulo.grid(row=11,column=1,pady=5)
buttonCrearTriangulo.config(bg="#66bde6",state="disabled")

#Botón para agregar otras medidas de otro triangulo
buttonCambiarMedidas=Button(frame,text="Agregar otras medidas",command=cambiarMedidas)
buttonCambiarMedidas.grid(row=11,column=2,pady=5)
buttonCambiarMedidas.config(bg="#66bde6",state="disabled")

#Comando para salir
salir=Button(frame,text="Salir",command=mainWindow.quit)
salir.grid(row=12,column=1,pady=5)
salir.config(bg="#66bde6")

mainWindow.mainloop()