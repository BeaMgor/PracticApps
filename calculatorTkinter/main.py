from tkinter import *
from tkinter import ttk
from math import *

#creamos la ventana de la calculadora

def hacer_click():
    pass
   
class MainApp(Tk):
    Tk.__init__(self)

# continuar yo



ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("265x350")
ventana.configure(bg = "grey40")

#Variable para color fondo botones
colorOpera=("SeaGreen1")
colorNumeros=("MistyRose2")
color_Espec=("SkyBlue3")
color_tex=("red")
ventana.resizable(0,0)


#crear operativa






#Variable apra tamaño de botones
wBoton=5
hBoton=2

#Variablo font
myFont = ("Arial",20,"bold") #para poner cursiva slant = "Italic"
cifra = DoubleVar(value = "") #para introducir numeros float

#creamos el cuadrado para la entrada numérica
entrada = Entry(ventana, font=("Arial",30, "bold"), textvariable = cifra, bg="khaki1", justify=RIGHT).place (x=10, y=10, width=245, height=75)
#Interfaz Gráfica
botonInicio = Button(ventana, text = "AC", font=("Arial",20, "italic"), fg=color_tex,bg=color_Espec, command=hacer_click).place (x=10, y=90, width=60, height=50)
botonSigno= Button(ventana, text = "+/-",bg=color_Espec,fg=color_tex,font=myFont).place (x=70, y=90, width=60, height=50)
botonPorce = Button(ventana, text = "%",font=myFont, fg=color_tex, bg=color_Espec).place (x=130, y=90, width=60, height=50)
botonDiv = Button(ventana, text = "/",bg=colorOpera,fg=color_tex, font=myFont,width=wBoton, height=hBoton).place (x=190, y=90)

boton5 = Button(ventana, text = "7",font=myFont,fg=color_tex,bg=colorNumeros,width=wBoton, height=hBoton).place (x=10, y=140)
boton6 = Button(ventana, text = "8",font=myFont,fg=color_tex, bg=colorNumeros,width=wBoton, height=hBoton).place (x=70, y=140)
boton7 = Button(ventana, text = "9",font=myFont, fg=color_tex,bg=colorNumeros,width=wBoton, height=hBoton).place (x=130, y=140)
botonMulti = Button(ventana, text = "*",font=myFont, fg=color_tex, bg=colorOpera, width=wBoton, height=hBoton).place (x=190, y=140)

boton9 = Button(ventana, text = "4",font=myFont,fg=color_tex, bg=colorNumeros,width=wBoton, height=hBoton).place (x=10, y=190)
boton10 = Button(ventana, text = "5",font=myFont,fg=color_tex, bg=colorNumeros,width=wBoton, height=hBoton).place (x=70, y=190)
boton11 = Button(ventana, text = "5",font=myFont,fg=color_tex, bg=colorNumeros,width=wBoton, height=hBoton).place (x=130, y=190)
botonResta = Button(ventana, text = "-",font=myFont,fg=color_tex, bg=colorOpera,width=wBoton, height=hBoton).place (x=190, y=190)

boton13 = Button(ventana, text = "1",font=myFont,fg=color_tex, bg=colorNumeros,width=wBoton, height=hBoton).place (x=10, y=240)
boton14 = Button(ventana, text = "2",font=myFont, fg=color_tex,bg=colorNumeros,width=wBoton, height=hBoton).place (x=70, y=240)
boton15 = Button(ventana, text = "3",font=myFont, fg=color_tex,bg=colorNumeros,width=wBoton, height=hBoton).place (x=130, y=240)
botonSuma = Button(ventana, text = "+",font=myFont, fg=color_tex,bg=colorOpera,width=wBoton, height=hBoton).place (x=190, y=240)

boton0 = Button(ventana, text = "0",font=myFont, fg=color_tex,bg=colorNumeros,width=10, height=hBoton).place (x=10, y=290)
botonComa = Button(ventana, text = ",",font=myFont,fg=color_tex, bg=colorNumeros,width=wBoton, height=hBoton).place (x=130, y=290)
botonIgual = Button(ventana, text = "=",font=myFont,fg=color_tex, bg=colorOpera,width=wBoton, height=hBoton).place (x=190, y=290)


ventana.mainloop()





