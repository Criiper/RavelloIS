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

        LogoRavello = Image.open(resource_path("assets\\LogoRavello.png"))

        # Redimensionar la imagen
        LogoRavello = LogoRavello.resize((500, 500), Image.LANCZOS)

        # Convertir la imagen a un formato compatible con Tkinter
        self.iLogoRavello = ImageTk.PhotoImage(LogoRavello)

        self.iconoVenta = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoVenta.png")))
        self.iconoProducto = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoRosas.png")))
        self.iconoDomicilio = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoDomicilio.png")))
        self.iconoPedido = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoPedido.png")))
        self.iconoClientes = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoClientes.png")))

        frameMenu = tk.Frame(self, bg=styles.BACKGROUND)
        frameMenu.grid(row=0, column=0, sticky=tk.NSEW)

        frameLogo = tk.Frame(self, bg=styles.HIGHLIGHT)
        frameLogo.grid(row=0, column=1, sticky=tk.NSEW)


        #BOTON VENTAS
        botonPedidos = tk.Button(master=frameMenu,
                                **styles.BUTTON,
                                text="  PEDIDOS",
                                image=self.iconoPedido,
                                command=self.manager.show_pedidos)
        
        botonPedidos.bind("<Enter>", styles.on_enter)
        botonPedidos.bind("<Leave>", styles.on_leave)
        
        botonPedidos.pack(fill="both", expand=True, padx=20, pady=5)


        #BOTON PRODUCTOS
        botonProducto = tk.Button(master=frameMenu,
                                **styles.BUTTON,
                                text="  PRODUCTOS",
                                image=self.iconoProducto,
                                command=self.manager.show_productos)
        
        botonProducto.bind("<Enter>", styles.on_enter)
        botonProducto.bind("<Leave>", styles.on_leave)
        
        botonProducto.pack(fill="both", expand=True, padx=20, pady=5)


        #BOTON INVENTARIO
        botonDomicilios = tk.Button(master=frameMenu,
                                **styles.BUTTON,
                                text="  DOMICILIOS",
                                image=self.iconoDomicilio,
                                command=self.manager.show_inventario)
        
        botonDomicilios.bind("<Enter>", styles.on_enter)
        botonDomicilios.bind("<Leave>", styles.on_leave)
        
        botonDomicilios.pack(fill="both", expand=True, padx=20, pady=5)


        #BOTON COMPRAS
        botonVentas = tk.Button(master=frameMenu,
                                **styles.BUTTON,
                                text="  VENTAS",
                                image=self.iconoVenta,
                                command=self.manager.show_compras)
        
        botonVentas.bind("<Enter>", styles.on_enter)
        botonVentas.bind("<Leave>", styles.on_leave)
        
        botonVentas.pack(fill="both", expand=True, padx=20, pady=5)


        #BOTON CLIENTES
        botonClientes = tk.Button(master=frameMenu,
                                **styles.BUTTON,
                                text="  CLIENTES",
                                command=self.manager.show_clientes,
                                image=self.iconoClientes)
        
        botonClientes.bind("<Enter>", styles.on_enter)
        botonClientes.bind("<Leave>", styles.on_leave)
        
        botonClientes.pack(fill="both", expand=True, padx=20, pady=5)

       
        #LOGO COPETE
        labelLogo = tk.Label(frameLogo, image=self.iLogoRavello, background=styles.HIGHLIGHT)
        labelLogo.pack(expand=True)