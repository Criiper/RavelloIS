from modules.controller import Controller
from modules.controller import resource_path
from screens.homeScreen import HomeScreen
from screens.clientesScreen import ClientesScreen
from screens.productosScreen import ProductosScreen
from screens.pedidosScreen import PedidosScreen
from screens.domiciliosScreen import DomiciliosScreen
from screens.ventasScreen import VentasScreen
import tkinter as tk


class Manager(tk.Tk):
    
    ####DEFINICIÓN PARA LA CLASE QUE GESTIONA EL CAMBIO DE PANTALLAS#######

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ###Hereda de Tk

        self.title("Rosas Ravello | Gestión de Pedidos") #Nombre de la ventana
        self.geometry("1180x620") #Tamaño de la ventana
        self.controller = Controller()  #Instancia la clase que controla la base de datos

        #Crea un Container principal donde van a colocarse las pantallas de la aplicación
        container = tk.Frame(master=self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        
        #Modifica las columnas para que haya un solo lugar para ponerse con el método grid (una sola cuadricula de 1x1)
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        self.frames = {

        }

        ####INSTANCIACIÓN DE LAS PANTALLAS
    
        pantallas = [HomeScreen, ProductosScreen, ClientesScreen, PedidosScreen, DomiciliosScreen, VentasScreen]
        for F in pantallas:
            frame = F(container, self)
            self.frames[F] = frame  # Usar instancias de las clases como claves
            frame.grid(row=0, column=0, sticky=tk.NSEW)
    


        self.show_frame(HomeScreen)
    
    ##Métodos para el cambio a cada pantalla
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
       
    def show_ventas(self):
        self.show_frame(VentasScreen)
        
    def show_pedidos(self):
        self.show_frame(PedidosScreen)

    def show_domicilios(self):
        self.show_frame(DomiciliosScreen)

    def show_productos(self):
        pass
        self.show_frame(ProductosScreen)

    def show_clientes(self):
        self.show_frame(ClientesScreen)

    def to_home(self):
        self.show_frame(HomeScreen)

    
    
