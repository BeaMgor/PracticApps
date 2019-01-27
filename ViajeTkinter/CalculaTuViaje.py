from tkinter import *
from tkinter import ttk


class MainApp(Tk):
    
    def __init__(self):
        
        Tk.__init__(self)
        self.title("Calcula tu viaje")
        self.geometry("300x600")
        self.configure(bg = "gray93")
        self.resizable(0,0)
        
        #variables de control
        
        self.num_viaje = ["1", "2",'3','4','5']
        self.ida_vuel = BooleanVar()
        self.clase = BooleanVar()
        self.distancia = IntVar()
        self.price = DoubleVar()
        
        #avion = PhotoImage (file="avion.png")
        #self.image = ttk.Label(self, image=self.avion).pack()
        
        self.viajeros = ttk.Label(self, text = "Viajeros:", font=("Helvetica",15,'bold')).place(x=10,y=10) 
        self.combo=ttk.Combobox(self, values=self.num_viaje).place(x=20,y=40)
        
        self.opcVia=ttk.Radiobutton(self, text ="Ida", value=1, variable = self.ida_vuel).place(x=10,y=80)
        self.opcVia=ttk.Radiobutton(self, text ="Ida y vuelta", value=2, variable = self.ida_vuel).place(x=10,y=110)        
        
        
        self.clase_pasajero = ttk.Label(self, text = 'Clase:', font=("Helvetica",15,'bold')).place(x=10,y=140)
        self.turist=ttk.Radiobutton(self, text ='turista', value=1, variable = self.clase).place(x=10,y=170)
        self.primera=ttk.Radiobutton(self, text ='primera', value=2, variable = self.clase).place(x=10,y=200)
        self.lujo=ttk.Radiobutton(self, text ='business', value=3, variable = self.clase).place(x=10,y=230)
        
        
        self.distance = ttk.Label(self, text = 'Kilómetros:', font=("Helvetica",15,'bold')).place(x=10,y=280)
        km = Entry(self, font=("Arial",15), textvariable=self.distancia, borderwidth=2).place (x=20, y=310)
        
        self.pre = ttk.Label(self, text = 'Precio:', font=("Helvetica",15,'bold')).place(x=10,y=360)
        precio = Entry(self, font=("Arial",15), textvariable=self.price, borderwidth=2).place (x=20, y=390)           


        




if __name__ == "__main__":
    app = MainApp()
    mainloop()