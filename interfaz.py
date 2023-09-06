#Elaborado por: Jose Julián Brenes Garro 
#Elementos de COmputación
#Versión 3.9.2

#importacion de librerias
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox
import re
from tkinter.messagebox import askyesno
import turtle
import math

#Variables globales


mainWindow=Tk()
mainWindow.config(bg="#4da8cf")
mainWindow.geometry("800x350")
mainWindow.title("Personalidades")
mainWindow.resizable(False,False)

def hola():
    '''
    t = turtle.Turtle()
    turtle.bgcolor("lightblue")
    turtle.title("Realizar triángulo")
    t.fd(45)
    t.lt(120)
    t.fd(30)
    t.lt(120)
    t.fd(70)
    t.lt(120)
    t.fd(22.5)
    t.circle(28.86751346)'''
    a=200
    b=300
    c=400
    if a + b > c and a + c > b and b + c > a:
        # Calcular los ángulos usando la ley de los cosenos
        #A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        
        print(B)
        print(C)

        # Dibujar el triángulo
        t = turtle.Turtle()
        t.forward(c)
        t.left(180 - B)
        t.forward(a)
        t.left(180 - C)
        t.forward(b)

        # Calcular el semiperímetro
        s = (a + b + c) / 2

        # Calcular el área del triángulo usando la fórmula de Herón
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Calcular el radio del círculo inscrito
        r = area / s

        t.penup()
        t.goto(-r, 0)  # Mover el cursor al centro del círculo inscrito
        t.pendown()
        t.circle(r)

#Título
frameTitulo=Frame(mainWindow,width=300,height=100)
frameTitulo.config(bg="#4da8cf")
frameTitulo.pack(fill="y")

#Botones
frame=Frame(mainWindow,width=3000,height=2000)
frame.config(bg="#4da8cf")
frame.pack()

titulo=Label(frameTitulo,text="No soy un círculo vicioso, soy un tríangulo amoroso")
titulo.grid(pady=10)
titulo.config(bg="#4da8cf",font=("arial",17,"bold"))

cargarBD=Button(frame,text="Registrar datos de una persona",command=hola)
cargarBD.grid(row=3,column=1,pady=5)
cargarBD.config(bg="#66bde6", width=44)

registroDinamico=Button(frame,text="Registro dinámico")
registroDinamico.grid(row=4,column=1,pady=5)
registroDinamico.config(bg="#66bde6",width=44)

modificar=Button(frame,text="Modificar los datos de una persona")
modificar.grid(row=5,column=1,pady=5)
modificar.config(bg="#66bde6",width=44)

eliminar=Button(frame,text="Eliminar los datos de una persona")
eliminar.grid(row=6,column=1,pady=5)
eliminar.config(bg="#66bde6",width=44)

xml=Button(frame,text="Crear XML")
xml.grid(row=7,column=1,pady=5)
xml.config(bg="#66bde6",width=44)

reporteBoton=Button(frame,text="Reportes")
reporteBoton.grid(row=8,column=1,pady=5)
reporteBoton.config(bg="#66bde6",width=44)

salir=Button(frame,text="Salir",command=mainWindow.quit)
salir.grid(row=9,column=1,pady=5)
salir.config(bg="#66bde6",width=44)

mainWindow.mainloop()