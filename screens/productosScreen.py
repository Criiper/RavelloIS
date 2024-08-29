import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from components.productosTabla import TablaProductos
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path

class ProductosScreen(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(master=root, background="#2c2c34")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.manager = manager
        self.controller = Controller()
        self.initWidgets()
    
    def initWidgets(self):
        #######IMAGENES######
        self.iconoGuardar = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoGuardar.png")))
        self.iconoBack = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoBack.png")))
        self.iconoNuevo = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoNuevo.png")))
        self.iconoBorrar = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoBorrar.png")))
        self.iconoEditar = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoEditar.png")))
        self.iconoMasUnd = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoMasUnd.png")))
        self.iconoBuscar = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoBuscar25px.png")))
        self.iconoNuevo25px = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoNuevo25px.png")))
        self.iconoBorrar25px = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoBorrar25px.png")))
        #######FRAMES#######

        contenedor = tk.Frame(master=self,
                           background=styles.BACKGROUND)
        
        contenedor.rowconfigure(1, weight=1)
        contenedor.columnconfigure(0, weight=1)
        contenedor.grid(row=0, column=1, sticky=tk.NSEW)

        TablaProductos(contenedor,
                      self.manager
        ).grid(row=1, column=0, sticky=tk.NSEW)
        
        frameMesa = tk.Frame(master=contenedor,
                             background=styles.BACKGROUND)
        
        frameMesa.grid(row=0, column=0, sticky=tk.NSEW)
        frameMesa.columnconfigure(0, weight=1)
        frameMesa.columnconfigure(1, weight=1)

        frameBotones = tk.Frame(master=self,
                                 background=styles.BACKGROUND)
        
        frameBotones.grid(row=0, column=0, sticky=tk.NS)


        ######ZONAS DE TRABAJO#######

        def zonaNuevo():

            def guardar():
                nombre = nombreVar.get()
                valor = int(valorVar.get())
                rosasEstimadas = int(rosasVar.get())
                chocolatesEstimados = int(chocolatesVar.get())
                nivelCuidado = int(cuidadoVar.get())
                descripcion = descripcionVar.get()


                self.controller.newProducto(nombre=nombre, valor=valor, estimadoRosas=rosasEstimadas,
                                            estimadoChocolates=chocolatesEstimados, nivelCuidado=nivelCuidado,
                                            descripcion=descripcion)
                
                nombreVar.set("")
                valorVar.set("")
                rosasVar.set("")
                chocolatesVar.set("")
                cuidadoVar.set("")
                descripcionVar.set("")


            for widgets in frameMesa.winfo_children():
                widgets.destroy()

            
                #LABELS Y BUTTONS

            nombreLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nombre")
            nombreLabel.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            nombreVar = tk.StringVar()
            nombreEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=nombreVar)
            nombreEntry.grid(column=0, row=1, padx=5, pady=5, sticky=tk.NSEW)


            valorLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Valor")
            valorLabel.grid(column=1, row=0, padx=5, pady=5, sticky=tk.NSEW)

            valorVar = tk.StringVar()
            valorEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=valorVar)
            valorEntry.grid(column=1, row=1, padx=5, pady=5, sticky=tk.NSEW)


            rosasLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Rosas Estimadas")
            rosasLabel.grid(column=0, row=2, padx=5, pady=5, sticky=tk.NSEW)

            rosasVar = tk.StringVar()
            rosasEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=rosasVar)
            rosasEntry.grid(column=0, row=3, padx=5, pady=5, sticky=tk.NSEW)


            chocolatesLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Chocolates Estimados")
            chocolatesLabel.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)

            chocolatesVar = tk.StringVar()
            chocolatesEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=chocolatesVar)
            chocolatesEntry.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)


            cuidadoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nivel de Cuidado Estimado")
            cuidadoLabel.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)

            cuidadoVar = tk.StringVar()
            cuidadoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=cuidadoVar)
            cuidadoEntry.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NSEW)



            descripcionLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Descripción: ")
            descripcionLabel.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)

            descripcionVar = tk.StringVar()
            descripcionEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=descripcionVar)
            descripcionEntry.grid(column=0, row=5, padx=5, pady=5, sticky=tk.NSEW)


            btnGuardarProducto = tk.Button(master=frameMesa,
                                        text="GUARDAR",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=guardar)
            
            btnGuardarProducto.config(height=30)
            btnGuardarProducto.grid(row=6, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnGuardarProducto.bind('<Enter>', styles.on_enter)
            btnGuardarProducto.bind('<Leave>', styles.on_leave)
            

        def zonaEliminar():
            
            def buscar():

                identificacion = int(idVar.get())
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                c.execute("SELECT * FROM producto")
                registros = c.fetchall()

                for registro in registros:
                    if int(registro[0]) == identificacion:
                        nombreVar.set(registro[1])
                        valorVar.set(registro[3])
                        descripcionVar.set(registro[2])
                        rosasVar.set(registro[5])
                        chocolatesVar.set(registro[6])
                        cuidadoVar.set(registro[4])

            def eliminar():

                identificacion = int(idVar.get())

                self.controller.delProducto(identificacion)

                idVar.set("")
                nombreVar.set("")
                valorVar.set("")
                descripcionVar.set("")
                rosasVar.set("")
                chocolatesVar.set("")
                cuidadoVar.set("")
            
            for widgets in frameMesa.winfo_children():
                widgets.destroy()


             #LABELS Y BUTTONS

            idLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="ID Producto")
            idLabel.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            idVar = tk.StringVar()
            idEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=idVar)
            idEntry.grid(column=1, row=0, padx=5, pady=5, sticky=tk.NSEW)



            nombreLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nombre")
            nombreLabel.grid(column=0, row=2, padx=5, pady=5, sticky=tk.NSEW)

            nombreVar = tk.StringVar()
            nombreEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=nombreVar,
                                state="disabled")
            nombreEntry.grid(column=0, row=3, padx=5, pady=5, sticky=tk.NSEW)


            valorLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Valor")
            valorLabel.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)

            valorVar = tk.StringVar()
            valorEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=valorVar,
                                state="disabled")
            valorEntry.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)


            rosasLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Rosas Estimadas")
            rosasLabel.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)

            rosasVar = tk.StringVar()
            rosasEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=rosasVar,
                                state="disabled")
            rosasEntry.grid(column=0, row=5, padx=5, pady=5, sticky=tk.NSEW)


            chocolatesLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Chocolates Estimados")
            chocolatesLabel.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)

            chocolatesVar = tk.StringVar()
            chocolatesEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=chocolatesVar,
                                state="disabled")
            chocolatesEntry.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NSEW)


            cuidadoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nivel de Cuidado Estimado")
            cuidadoLabel.grid(column=1, row=6, padx=5, pady=5, sticky=tk.NSEW)

            cuidadoVar = tk.StringVar()
            cuidadoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=cuidadoVar,
                                state="disabled")
            cuidadoEntry.grid(column=1, row=7, padx=5, pady=5, sticky=tk.NSEW)



            descripcionLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Descripción: ")
            descripcionLabel.grid(column=0, row=6, padx=5, pady=5, sticky=tk.NSEW)

            descripcionVar = tk.StringVar()
            descripcionEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=descripcionVar,
                                state="disabled")
            descripcionEntry.grid(column=0, row=7, padx=5, pady=5, sticky=tk.NSEW)


            btnEliminarProducto = tk.Button(master=frameMesa,
                                        text="ELIMINAR",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=eliminar)
            
            btnEliminarProducto.config(height=30)
            btnEliminarProducto.grid(row=8, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnEliminarProducto.bind('<Enter>', styles.on_enter)
            btnEliminarProducto.bind('<Leave>', styles.on_leave)
            
            btnBuscar = tk.Button(master=frameMesa,
                                        text=" BUSCAR",
                                        **styles.BUTTON,
                                        image=self.iconoBuscar,
                                        command=buscar)
            
            btnBuscar.config(height=20)
            btnBuscar.grid(row=1, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnBuscar.bind('<Enter>', styles.on_enter)
            btnBuscar.bind('<Leave>', styles.on_leave)


        def zonaEditar():

            def buscar():

                identificacion = int(idVar.get())
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                c.execute("SELECT * FROM producto")
                registros = c.fetchall()

                for registro in registros:
                    if int(registro[0]) == identificacion:
                        nombreVar.set(registro[1])
                        valorVar.set(registro[3])
                        descripcionVar.set(registro[2])
                        rosasVar.set(registro[5])
                        chocolatesVar.set(registro[6])
                        cuidadoVar.set(registro[4])

            def update(): 
                identificacion = int(idVar.get())           
                nombre = nombreVar.get()
                valor = float(valorVar.get())
                rosasEstimadas = int(rosasVar.get())
                chocolatesEstimados = int(chocolatesVar.get())
                nivelCuidado = int(cuidadoVar.get())
                descripcion = descripcionVar.get()

                self.controller.updateProducto(identificacion=identificacion, newNombre=nombre,
                                               newDescripcion=descripcion, newValor=valor, newNivelCuidado=nivelCuidado,
                                               newEstimadoChocolates=chocolatesEstimados, newEstimadoRosas=rosasEstimadas)

                idVar.set("")
                nombreVar.set("")
                valorVar.set("")
                descripcionVar.set("")
                rosasVar.set("")
                chocolatesVar.set("")
                cuidadoVar.set("")


            for widgets in frameMesa.winfo_children():
                widgets.destroy()


            #LABELS Y BUTTONS

            idLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="ID Producto")
            idLabel.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            idVar = tk.StringVar()
            idEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=idVar)
            idEntry.grid(column=1, row=0, padx=5, pady=5, sticky=tk.NSEW)



            nombreLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nombre")
            nombreLabel.grid(column=0, row=2, padx=5, pady=5, sticky=tk.NSEW)

            nombreVar = tk.StringVar()
            nombreEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=nombreVar)
            nombreEntry.grid(column=0, row=3, padx=5, pady=5, sticky=tk.NSEW)


            valorLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Valor")
            valorLabel.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)

            valorVar = tk.StringVar()
            valorEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=valorVar)
            valorEntry.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)


            rosasLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Rosas Estimadas")
            rosasLabel.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)

            rosasVar = tk.StringVar()
            rosasEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=rosasVar)
            rosasEntry.grid(column=0, row=5, padx=5, pady=5, sticky=tk.NSEW)


            chocolatesLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Chocolates Estimados")
            chocolatesLabel.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)

            chocolatesVar = tk.StringVar()
            chocolatesEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=chocolatesVar)
            chocolatesEntry.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NSEW)


            cuidadoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nivel de Cuidado Estimado")
            cuidadoLabel.grid(column=1, row=6, padx=5, pady=5, sticky=tk.NSEW)

            cuidadoVar = tk.StringVar()
            cuidadoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=cuidadoVar)
            cuidadoEntry.grid(column=1, row=7, padx=5, pady=5, sticky=tk.NSEW)



            descripcionLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Descripción: ")
            descripcionLabel.grid(column=0, row=6, padx=5, pady=5, sticky=tk.NSEW)

            descripcionVar = tk.StringVar()
            descripcionEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=descripcionVar)
            descripcionEntry.grid(column=0, row=7, padx=5, pady=5, sticky=tk.NSEW)


            btnEliminarProducto = tk.Button(master=frameMesa,
                                        text="GUARDAR",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=update)
            
            btnEliminarProducto.config(height=30)
            btnEliminarProducto.grid(row=8, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnEliminarProducto.bind('<Enter>', styles.on_enter)
            btnEliminarProducto.bind('<Leave>', styles.on_leave)
            
            btnBuscar = tk.Button(master=frameMesa,
                                        text=" BUSCAR",
                                        **styles.BUTTON,
                                        image=self.iconoBuscar,
                                        command=buscar)
            
            btnBuscar.config(height=20)
            btnBuscar.grid(row=1, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnBuscar.bind('<Enter>', styles.on_enter)
            btnBuscar.bind('<Leave>', styles.on_leave)



            

        #######BOTONES#######

        botonAñadir = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" NUEVO PRODUCTO",
                                image=self.iconoNuevo,
                                command= zonaNuevo)
        botonAñadir.pack(padx=10, pady=5, fill="both", expand=True)
        botonAñadir.bind('<Enter>', styles.on_enter)
        botonAñadir.bind('<Leave>', styles.on_leave)

        botonEditar = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" EDITAR PRODUCTO",
                                image=self.iconoEditar,
                                command=zonaEditar)
        botonEditar.pack(padx=10, pady=5, fill="both", expand=True)
        botonEditar.bind('<Enter>', styles.on_enter)
        botonEditar.bind('<Leave>', styles.on_leave)

        botonEliminar = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" ELIMINAR PRODUCTO",
                                image=self.iconoBorrar,
                                command=zonaEliminar)
        botonEliminar.pack(padx=10, pady=5, fill="both", expand=True)
        botonEliminar.bind('<Enter>', styles.on_enter)
        botonEliminar.bind('<Leave>', styles.on_leave)


        botonBack = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" VOLVER",
                                image=self.iconoBack,
                                command=self.manager.to_home)
        botonBack.pack(padx=10, pady=5, fill="both", expand=True)
        botonBack.bind('<Enter>', styles.on_enter)
        botonBack.bind('<Leave>', styles.on_leave)

        zonaNuevo()
            

        