import tkinter as tk
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path

class HomeScreen(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(master=root, background=styles.BACKGROUND)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.manager = manager
        self.controller = Controller()
        self.initWidgets()
    
    def initWidgets(self):

        LogoCopete = Image.open(resource_path("assets\\LogoRavello.png"))

        # Redimensionar la imagen
        LogoCopete = LogoCopete.resize((500, 500), Image.LANCZOS)

        # Convertir la imagen a un formato compatible con Tkinter
        self.iLogoCopete = ImageTk.PhotoImage(LogoCopete)

        self.iconoVenta = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoVenta.png")))
        self.iconoProducto = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoProducto.png")))
        self.iconoClientes = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoClientes.png")))
        self.iconoInventario = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoInventario.png")))
        self.iconoCompras = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoMasUnd.png")))

        frameMenu = tk.Frame(self, bg=styles.BACKGROUND)
        frameMenu.grid(row=0, column=0, sticky=tk.NSEW)

        frameLogo = tk.Frame(self, bg=styles.HIGHLIGHT)
        frameLogo.grid(row=0, column=1, sticky=tk.NSEW)


        #BOTON VENTAS
        botonVentas = tk.Button(master=frameMenu,
                                **styles.BOTON,
                                text="  VENTAS",
                                image=self.iconoVenta,
                                command=self.manager.show_ventas)
        
        botonVentas.bind("<Enter>", styles.on_enter)
        botonVentas.bind("<Leave>", styles.on_leave)
        
        botonVentas.pack(fill="both", expand=True, padx=20, pady=5)


        #BOTON PRODUCTOS
        botonProducto = tk.Button(master=frameMenu,
                                **styles.BOTON,
                                text="  PRODUCTOS",
                                image=self.iconoProducto,
                                command=self.manager.show_productos)
        
        botonProducto.bind("<Enter>", styles.on_enter)
        botonProducto.bind("<Leave>", styles.on_leave)
        
        botonProducto.pack(fill="both", expand=True, padx=20, pady=5)


        #BOTON INVENTARIO
        botonInventario = tk.Button(master=frameMenu,
                                **styles.BOTON,
                                text="  INVENTARIO",
                                image=self.iconoInventario,
                                command=self.manager.show_inventario)
        
        botonInventario.bind("<Enter>", styles.on_enter)
        botonInventario.bind("<Leave>", styles.on_leave)
        
        botonInventario.pack(fill="both", expand=True, padx=20, pady=5)


        #BOTON COMPRAS
        botonCompras = tk.Button(master=frameMenu,
                                **styles.BOTON,
                                text="  COMPRAS",
                                image=self.iconoCompras,
                                command=self.manager.show_compras)
        
        botonCompras.bind("<Enter>", styles.on_enter)
        botonCompras.bind("<Leave>", styles.on_leave)
        
        botonCompras.pack(fill="both", expand=True, padx=20, pady=5)


        #BOTON CLIENTES
        botonClientes = tk.Button(master=frameMenu,
                                **styles.BOTON,
                                text="  CLIENTES",
                                command=self.manager.show_clientes,
                                image=self.iconoClientes)
        
        botonClientes.bind("<Enter>", styles.on_enter)
        botonClientes.bind("<Leave>", styles.on_leave)
        
        botonClientes.pack(fill="both", expand=True, padx=20, pady=5)

       
        #LOGO COPETE
        labelLogo = tk.Label(frameLogo, image=self.iLogoCopete, background=styles.HIGHLIGHT)
        labelLogo.pack(expand=True)