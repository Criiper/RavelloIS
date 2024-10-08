import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from components.clientesTabla import TablaClientes
from components.pedidosTabla import PedidosTabla
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path


class ClientesScreen(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(master=root, background=styles.BACKGROUND)
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

        TablaClientes(contenedor,
                      self.manager
        ).grid(row=1, column=0, sticky=tk.NSEW)
        
        frameMesa = tk.Frame(master=contenedor,
                             background=styles.BACKGROUND)
        
        frameMesa.grid(row=0, column=0, sticky=tk.NSEW)
        frameMesa.columnconfigure(0, weight=1)
        frameMesa.columnconfigure(1, weight=1)

        frameBotones = tk.Frame(master=self,
                                 background=styles.LIGHT_BACKGROUND)
        
        frameBotones.grid(row=0, column=0, sticky=tk.NS)


        ######ZONAS DE TRABAJO#######

        def zonaNuevo():

            def guardar():
                nombre = nombreVar.get()
                telefono = int(telefonoVar.get())
                correo = correoEntry.get()
                direccion = direccionEntry.get()
                cedula = documentoEntry.get()

                self.controller.newCliente(nombre=nombre, telefono=telefono, correo=correo, direccion=direccion, cedula=cedula)

                nombreVar.set("")
                telefonoVar.set("")
                correoVar.set("")
                direccionVar.set("")
                documentoVar.set("")

            for widgets in frameMesa.winfo_children():
                widgets.destroy()

            #LABELS Y BOTONES


            nombreLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nombre")
            nombreLabel.grid(column=0, row=1, padx=5, pady=5, sticky=tk.NSEW)

            nombreVar = tk.StringVar()
            nombreEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=nombreVar)
            nombreEntry.grid(column=0, row=2, padx=5, pady=5, sticky=tk.NSEW)


            documentoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Numero de Documento")
            documentoLabel.grid(column=1, row=1, padx=5, pady=5, sticky=tk.NSEW)

            documentoVar = tk.StringVar()
            documentoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=documentoVar)
            documentoEntry.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)


            correoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Correo Electronico")
            correoLabel.grid(column=0, row=3, padx=5, pady=5, sticky=tk.NSEW)

            correoVar = tk.StringVar()
            correoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=correoVar)
            correoEntry.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)


            direccionLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Dirección")
            direccionLabel.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)

            direccionVar = tk.StringVar()
            direccionEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=direccionVar)
            direccionEntry.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)


            telefonoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Teléfono")
            telefonoLabel.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            telefonoVar = tk.StringVar()
            telefonoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=telefonoVar)
            telefonoEntry.grid(column=1, row=0, padx=5, pady=5, sticky=tk.NSEW)


            btnGuardarCliente = tk.Button(master=frameMesa,
                                        text="GUARDAR",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=guardar)
            
            btnGuardarCliente.config(height=30)
            btnGuardarCliente.grid(row=5, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnGuardarCliente.bind('<Enter>', styles.on_enter)
            btnGuardarCliente.bind('<Leave>', styles.on_leave)
            
            
        def zonaEliminar():

            def borrar():
                identificacion = int(telefonoVar.get())

                self.controller.delCliente(identificacion)


                nombreVar.set("")
                telefonoVar.set("")
                direccionVar.set("")
                correoVar.set("")
                cedulaVar.set("")

            def buscar():
                identificacion = telefonoVar.get()
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                c.execute("SELECT * FROM cliente")
                registros = c.fetchall()

                for registro in registros:
                    if str(registro[2]) == identificacion:
                        nombreVar.set(registro[1])
                        direccionVar.set(registro[5])
                        correoVar.set(registro[4])
                        cedulaVar.set(registro[6])
                        
            
            for widgets in frameMesa.winfo_children():
                widgets.destroy()

            
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


            telefonoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Teléfono")
            telefonoLabel.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            telefonoVar = tk.StringVar()
            telefonoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=telefonoVar)
            telefonoEntry.grid(column=1, row=0, padx=5, pady=5, sticky=tk.NSEW)

            correoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Correo Electronico")
            correoLabel.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)

            correoVar = tk.StringVar()
            correoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=correoVar,
                                state="disabled")
            correoEntry.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)



            direccionLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Direccion")
            direccionLabel.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)

            direccionVar = tk.StringVar()
            direccionEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=direccionVar,
                                state="disabled")
            direccionEntry.grid(column=0, row=5, padx=5, pady=5, sticky=tk.NSEW)


            cedulaLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Numero de Documento")
            cedulaLabel.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)

            cedulaVar = tk.StringVar()
            cedulaEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=cedulaVar,
                                state="disabled")
            cedulaEntry.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NSEW)

        

            btnBorrarCliente = tk.Button(master=frameMesa,
                                        text="BORRAR",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=borrar)
            
            btnBorrarCliente.config(height=30)
            btnBorrarCliente.grid(row=6, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnBorrarCliente.bind('<Enter>', styles.on_enter)
            btnBorrarCliente.bind('<Leave>', styles.on_leave)
            
            btnBuscarCliente = tk.Button(master=frameMesa,
                                        text=" BUSCAR",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=buscar)
            
            btnBuscarCliente.config(height=30)
            btnBuscarCliente.grid(row=1, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnBuscarCliente.bind('<Enter>', styles.on_enter)
            btnBuscarCliente.bind('<Leave>', styles.on_leave)
            

        def zonaEditar():

            for widgets in frameMesa.winfo_children():
                widgets.destroy()

            def guardar():
                nombre = nombreVar.get()
                telefono = int(telefonoVar.get())
                correo = correoVar.get()
                direccion = direccionVar.get()
                cedula = cedulaVar.get()

                self.controller.updateCliente(nombres=nombre, telefono=telefono, correo=correo, direccion=direccion, cedula=cedula)


                nombreVar.set("")
                telefonoVar.set("")
                correoVar.set("")
                direccionVar.set("")
                cedulaVar.set("")

            def buscar():
                identificacion = telefonoVar.get()
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                c.execute("SELECT * FROM cliente")
                registros = c.fetchall()

                for registro in registros:
                    if str(registro[2]) == identificacion:
                        nombreVar.set(registro[1])
                        correoVar.set(registro[4])
                        direccionVar.set(registro[5])
                        cedulaVar.set(registro[6])
                        
            
            for widgets in frameMesa.winfo_children():
                widgets.destroy()

            
            nombreLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nombre")
            nombreLabel.grid(column=0, row=2, padx=5, pady=5, sticky=tk.NSEW)

            nombreVar = tk.StringVar()
            nombreEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=nombreVar)
            nombreEntry.grid(column=0, row=3, padx=5, pady=5, sticky=tk.NSEW)


            telefonoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Teléfono")
            telefonoLabel.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            telefonoVar = tk.StringVar()
            telefonoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=telefonoVar)
            telefonoEntry.grid(column=1, row=0, padx=5, pady=5, sticky=tk.NSEW)

            correoLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Correo Electronico")
            correoLabel.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)

            correoVar = tk.StringVar()
            correoEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=correoVar)
            correoEntry.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)


            direccionLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Direccion")
            direccionLabel.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)

            direccionVar = tk.StringVar()
            direccionEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=direccionVar)
            direccionEntry.grid(column=0, row=5, padx=5, pady=5, sticky=tk.NSEW)


            
            cedulaLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Numero de Documento")
            cedulaLabel.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)

            cedulaVar = tk.StringVar()
            cedulaEntry = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=cedulaVar)
            cedulaEntry.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NSEW)


            btnGuardarCliente = tk.Button(master=frameMesa,
                                        text="GUARDAR",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=guardar)
            
            btnGuardarCliente.config(height=30)
            btnGuardarCliente.grid(row=6, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnGuardarCliente.bind('<Enter>', styles.on_enter)
            btnGuardarCliente.bind('<Leave>', styles.on_leave)
            
            btnBuscarCliente = tk.Button(master=frameMesa,
                                        text=" BUSCAR",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=buscar)
            
            btnBuscarCliente.config(height=30)
            btnBuscarCliente.grid(row=1, column=1, padx=10, pady=15, sticky=tk.NSEW)
            btnBuscarCliente.bind('<Enter>', styles.on_enter)
            btnBuscarCliente.bind('<Leave>', styles.on_leave)
            
            
            

        #######BOTONES#######

        botonAñadir = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" NUEVO CLIENTE",
                                image=self.iconoNuevo,
                                command= zonaNuevo)
        botonAñadir.pack(padx=10, pady=5, fill="both", expand=True)
        botonAñadir.bind('<Enter>', styles.on_enter)
        botonAñadir.bind('<Leave>', styles.on_leave)

        botonEditar = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" EDITAR CLIENTE",
                                image=self.iconoEditar,
                                command=zonaEditar)
        botonEditar.pack(padx=10, pady=5, fill="both", expand=True)
        botonEditar.bind('<Enter>', styles.on_enter)
        botonEditar.bind('<Leave>', styles.on_leave)

        botonEliminar = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" ELIMINAR CLIENTE",
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