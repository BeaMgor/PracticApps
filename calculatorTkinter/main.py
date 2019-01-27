from tkinter import *
from tkinter import ttk


valor= ""




#Variable apra tamaño de botones
wBoton=5
hBoton=2

#Variablo font
myFont = ("Arial",20,"bold") #para poner cursiva "Italic"




class MainApp(Tk):
    

    
    def __init__(self):
        Tk.__init__(self)   
        self.title("Calculadora")
        self.geometry("265x350")
        self.configure(bg = "grey40")

        #Variable para color fondo botones
        self.colorOpera=("SeaGreen1")
        self.colorNumeros=("MistyRose2")
        self.color_tex=("red")
        self.resizable(0,0)
        
    
        
        s = ttk.Style()
        s.configure("my.TButton", foreground= "orange")
        self.btn = ttk.Button(self, style="my.TButton")




        self.valorEntrada=StringVar()
        #Interfaz Gráfica
        entrada = Entry(self, font=("Arial",30, "bold"), textvariable=self.valorEntrada, bg="khaki1", justify=RIGHT, borderwidth=15).place (x=10, y=10, width=245, height=75)
        botonInicio = Button(self, text = "AC", font=("Arial",20, "italic"), fg=self.color_tex, width=wBoton, height=hBoton).place (x=10, y=90)
        botonSigno= Button(self, text = "+/-",fg=self.color_tex,font=myFont, width=wBoton, height=hBoton).place (x=70, y=90)
        botonPorce = Button(self, text = "%",font=myFont, fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click("%")).place (x=130, y=90)
        botonDiv = Button(self, text = "/",font=myFont, fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click("/")).place (x=190, y=90)

        boton7 = Button(self, text = "7",font=myFont,fg=self.color_tex,width=wBoton, height=hBoton, command = lambda:do_click(7)).place (x=10, y=140)
        boton8 = Button(self, text = "8",font=myFont,fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click(8)).place (x=70, y=140)
        boton9 = Button(self, text = "9",font=myFont, fg=self.color_tex,width=wBoton, height=hBoton, command = lambda:do_click(9)).place (x=130, y=140)
        botonMulti = Button(self, text = "*",font=myFont, fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click("*")).place (x=190, y=140)

        boton4 = Button(self, text = "4",font=myFont,fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click(4)).place (x=10, y=190)
        boton5 = Button(self, text = "5",font=myFont,fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click(5)).place (x=70, y=190)
        boton6 = Button(self, text = "6",font=myFont,fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click(6)).place (x=130, y=190)
        botonResta = Button(self, text = "-",font=myFont,fg=self.color_tex,width=wBoton, height=hBoton,command = lambda:do_click("-")).place (x=190, y=190)
        
        boton1 = Button(self, text = "1",font=myFont,fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click(1)).place (x=10, y=240)
        boton2 = Button(self, text = "2",font=myFont, fg=self.color_tex,width=wBoton, height=hBoton, command = lambda:do_click(2)).place (x=70, y=240)
        boton3 = Button(self, text = "3",font=myFont, fg=self.color_tex,width=wBoton, height=hBoton, command = lambda:do_click(3)).place (x=130, y=240)
        botonSuma = Button(self, text = "+",font=myFont, fg=self.color_tex,width=wBoton, height=hBoton, command = lambda:do_click("+")).place (x=190, y=240)

        boton0 = Button(self, text = "0",font=myFont, fg=self.color_tex,width=10, height=hBoton, command = lambda:do_click(0)).place (x=10, y=290)
        botonComa = Button(self, text = ",",font=myFont,fg=self.color_tex, width=wBoton, height=hBoton, command = lambda:do_click(",")).place (x=130, y=290)
        botonIgual = Button(self, text = "=",font=myFont,fg=self.color_tex, width=wBoton, height=hBoton).place (x=190, y=290)


    def do_click(num):
    
        valorEntrada=StringVar()
    
        global valor
        valor = valor + str(num)
        valorEntrada.set(valor)

     



if __name__ == "__main__":
    
    app = MainApp()
    mainloop()