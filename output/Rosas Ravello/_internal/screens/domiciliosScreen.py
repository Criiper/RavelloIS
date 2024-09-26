import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
import sqlite3 as sql

from matplotlib.pyplot import bar
from components.domiciliosTabla import TablaDomicilios
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path

class DomiciliosScreen(tk.Frame):
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
        self.iconoPrinter = ImageTk.PhotoImage(Image.open(resource_path("assets\\printer.png")))
        #######FRAMES#######

        contenedor = tk.Frame(master=self,
                           background=styles.BACKGROUND)
        
        contenedor.rowconfigure(1, weight=1)
        contenedor.columnconfigure(0, weight=1)
        contenedor.grid(row=0, column=1, sticky=tk.NSEW)

        TablaDomicilios(contenedor,
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


        ################ZONAS DE TRABAJO :D ###########################

        def zonaAgregar():

            def buscar():
                idPedido = int(idPedidoVar.get())

                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                c.execute("SELECT * FROM domicilio WHERE idPedido = ?", (idPedido,)) 
                pedido = c.fetchone()

                if pedido == None:
                    entryBarrio.config(state="normal")
                    entryCiudad.config(state="normal")
                    entryDireccion.config(state="normal")
                    entryNombre.config(state="normal")
                    entryPostal.config(state="normal")
                    entryTelefono.config(state="normal")
                    infoDomiEntry.config(state="normal")

            def agregarDomicilio():
                idPedido = int(idPedidoVar.get())
                nombre = nombreVar.get()
                telefono = int(telefonoVar.get())
                direccion = direccionVar.get()
                ciudad = ciudadVar.get()
                barrio = barrioVar.get()
                postal = postalVar.get()
                info = infoDomiEntry.get("1.0","end-1c")

                self.controller.newDomicilio(idPedido=idPedido, nombre=nombre, telefono=telefono, ciudad=ciudad, direccion=direccion,
                                        barrio=barrio, postal=postal, infoadicional=info)

                
                idPedidoVar.set("")
                nombreVar.set("")
                telefonoVar.set("")
                direccionVar.set("")
                ciudadVar.set("")
                barrioVar.set("")
                postalVar.set("")
                infoDomiEntry.delete("1.0","end")




            for widgets in frameMesa.winfo_children():
                widgets.destroy()


            ###LABELS y ENTRYS###

            zonaLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Agregar Domicilio")
            zonaLabel.config(background=styles.BACKGROUND, font=('Abhadi', 14))
            zonaLabel.grid(column=2, row=0, padx=5, pady=5, sticky=tk.NSEW)


            labelIdPedido = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Id del Pedido")
            labelIdPedido.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            idPedidoVar = tk.StringVar()
            entryIdPedido = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=idPedidoVar)
            entryIdPedido.grid(column=0, row=1, padx=5, pady=5, sticky=tk.NSEW)




            labelNombre = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nombre")
            labelNombre.grid(column=0, row=2, padx=5, pady=5, sticky=tk.NSEW)

            nombreVar = tk.StringVar()
            entryNombre = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=nombreVar,
                                state="disabled")
            entryNombre.grid(column=0, row=3, padx=5, pady=5, sticky=tk.NSEW)
            



            labelTelefono = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Telefono")
            labelTelefono.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)

            telefonoVar = tk.StringVar()
            entryTelefono = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=telefonoVar,
                                state="disabled")
            entryTelefono.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)
            



            labelCiudad = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Ciudad")
            labelCiudad.grid(column=2, row=2, padx=5, pady=5, sticky=tk.NSEW)

            ciudadVar = tk.StringVar()
            entryCiudad = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=ciudadVar,
                                state="disabled")
            entryCiudad.grid(column=2, row=3, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelDireccion = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Direccion")
            labelDireccion.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)

            direccionVar = tk.StringVar()
            entryDireccion = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=direccionVar,
                                state="disabled")
            entryDireccion.grid(column=0, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelBarrio = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Barrio")
            labelBarrio.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)

            barrioVar = tk.StringVar()
            entryBarrio = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=barrioVar,
                                state="disabled")
            entryBarrio.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelPostal = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Codigo Postal")
            labelPostal.grid(column=2, row=4, padx=5, pady=5, sticky=tk.NSEW)

            postalVar = tk.StringVar()
            entryPostal = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=postalVar,
                                state="disabled")
            entryPostal.grid(column=2, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelInfo = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Informacion Adicional")
            labelInfo.grid(column=0, row=6, padx=5, pady=5, sticky=tk.EW)


            infoDomiVar = tk.StringVar()
            infoDomiEntry = tk.Text(master=frameMesa,
                                       font=('Abhadi', 12),
                                       width=15, height=4,
                                       state="disabled",
                                       )
            infoDomiEntry.grid(row=6, column=1, sticky=tk.NSEW, padx=5, pady=5)


            ######BOTONES (ZONAAGREGAR)#################

            botonBuscar = tk.Button(master=frameMesa,
                                        text="  Buscar",
                                        **styles.BUTTON,
                                        image=self.iconoBuscar,
                                        command=buscar)
            
            botonBuscar.config(height=18)
            botonBuscar.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
            botonBuscar.bind('<Enter>', styles.on_enter)
            botonBuscar.bind('<Leave>', styles.on_leave)


            botonGuardar = tk.Button(master=frameMesa,
                                        text="Guardar",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=agregarDomicilio)
            
            botonGuardar.config(height=30)
            botonGuardar.grid(row=7, column=1, padx=5, pady=5, sticky=tk.NSEW)
            botonGuardar.bind('<Enter>', styles.on_enter)
            botonGuardar.bind('<Leave>', styles.on_leave)


        def zonaEditar():

            def buscar():
                idPedido = int(idPedidoVar.get())

                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                c.execute("SELECT * FROM domicilio WHERE idPedido = ?", (idPedido,)) 
                domicilio = c.fetchone()

                if domicilio != None:
                    nombreVar.set(domicilio[1])
                    entryNombre.config(state="normal")
                    telefonoVar.set(domicilio[2])
                    entryTelefono.config(state="normal")
                    ciudadVar.set(domicilio[5])
                    entryCiudad.config(state="normal")
                    barrioVar.set(domicilio[4])
                    entryBarrio.config(state="normal")
                    direccionVar.set(domicilio[3])
                    entryDireccion.config(state="normal")
                    postalVar.set(domicilio[6])
                    entryPostal.config(state="normal")
                    infoDomiEntry.config(state="normal")
                    infoDomiEntry.insert("end-1c", domicilio[7])

            def editarDomicilio():
                idPedido = int(idPedidoVar.get())
                nombre = nombreVar.get()
                telefono = int(telefonoVar.get())
                direccion = direccionVar.get()
                ciudad = ciudadVar.get()
                barrio = barrioVar.get()
                postal = postalVar.get()
                info = infoDomiEntry.get("1.0","end-1c")

                self.controller.updateDomicilio(idPedido=idPedido, nombre=nombre, telefono=telefono, ciudad=ciudad, direccion=direccion,
                                        barrio=barrio, postal=postal, infoadicional=info)

                
                idPedidoVar.set("")
                
                nombreVar.set("")
                entryNombre.config(state="disabled")
                telefonoVar.set("")
                entryTelefono.config(state="disabled")
                direccionVar.set("")
                entryDireccion.config(state="disabled")
                ciudadVar.set("")
                entryCiudad.config(state="disabled")
                barrioVar.set("")
                entryBarrio.config(state="disabled")
                postalVar.set("")
                entryPostal.config(state="disabled")
                infoDomiEntry.delete("1.0","end")
                infoDomiEntry.config(state="disabled")

            for widgets in frameMesa.winfo_children():
                widgets.destroy()


            ###LABELS y ENTRYS###

            zonaLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Editar Domicilio")
            zonaLabel.config(background=styles.BACKGROUND, font=('Abhadi', 14))
            zonaLabel.grid(column=2, row=0, padx=5, pady=5, sticky=tk.NSEW)


            labelIdPedido = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Id del Pedido")
            labelIdPedido.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            idPedidoVar = tk.StringVar()
            entryIdPedido = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=idPedidoVar)
            entryIdPedido.grid(column=0, row=1, padx=5, pady=5, sticky=tk.NSEW)




            labelNombre = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nombre")
            labelNombre.grid(column=0, row=2, padx=5, pady=5, sticky=tk.NSEW)

            nombreVar = tk.StringVar()
            entryNombre = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=nombreVar,
                                state="readonly")
            entryNombre.grid(column=0, row=3, padx=5, pady=5, sticky=tk.NSEW)
            



            labelTelefono = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Telefono")
            labelTelefono.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)

            telefonoVar = tk.StringVar()
            entryTelefono = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=telefonoVar,
                                state="readonly")
            entryTelefono.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)
            



            labelCiudad = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Ciudad")
            labelCiudad.grid(column=2, row=2, padx=5, pady=5, sticky=tk.NSEW)

            ciudadVar = tk.StringVar()
            entryCiudad = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=ciudadVar,
                                state="readonly")
            entryCiudad.grid(column=2, row=3, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelDireccion = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Direccion")
            labelDireccion.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)

            direccionVar = tk.StringVar()
            entryDireccion = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=direccionVar,
                                state="readonly")
            entryDireccion.grid(column=0, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelBarrio = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Barrio")
            labelBarrio.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)

            barrioVar = tk.StringVar()
            entryBarrio = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=barrioVar,
                                state="readonly")
            entryBarrio.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelPostal = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Codigo Postal")
            labelPostal.grid(column=2, row=4, padx=5, pady=5, sticky=tk.NSEW)

            postalVar = tk.StringVar()
            entryPostal = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=postalVar,
                                state="readonly")
            entryPostal.grid(column=2, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelInfo = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Informacion Adicional")
            labelInfo.grid(column=0, row=6, padx=5, pady=5, sticky=tk.EW)


            infoDomiVar = tk.StringVar()
            infoDomiEntry = tk.Text(master=frameMesa,
                                       font=('Abhadi', 12),
                                       width=15, height=4,
                                state="disabled")
            infoDomiEntry.grid(row=6, column=1, sticky=tk.NSEW, padx=5, pady=5)


            ######BOTONES (ZONAEDITAR)#################

            botonBuscar = tk.Button(master=frameMesa,
                                        text="  Buscar",
                                        **styles.BUTTON,
                                        image=self.iconoBuscar,
                                        command=buscar)
            
            botonBuscar.config(height=18)
            botonBuscar.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
            botonBuscar.bind('<Enter>', styles.on_enter)
            botonBuscar.bind('<Leave>', styles.on_leave)


            botonGuardar = tk.Button(master=frameMesa,
                                        text="Guardar",
                                        **styles.BUTTON,
                                        image=self.iconoGuardar,
                                        command=editarDomicilio)
            
            botonGuardar.config(height=30)
            botonGuardar.grid(row=7, column=1, padx=5, pady=5, sticky=tk.NSEW)
            botonGuardar.bind('<Enter>', styles.on_enter)
            botonGuardar.bind('<Leave>', styles.on_leave)


        def zonaEliminar():

            def buscar():
                idPedido = int(idPedidoVar.get())

                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                c.execute("SELECT * FROM domicilio WHERE idPedido = ?", (idPedido,)) 
                domicilio = c.fetchone()

                if domicilio != None:
                    nombreVar.set(domicilio[1])
                    telefonoVar.set(domicilio[2])
                    ciudadVar.set(domicilio[5])
                    barrioVar.set(domicilio[4])
                    direccionVar.set(domicilio[3])
                    postalVar.set(domicilio[6])
                    infoDomiEntry.config(state="normal")
                    infoDomiEntry.insert("end-1c", domicilio[7])

            def eliminarDomicilio():

                idPedido = int(idPedidoVar.get())

                self.controller.delDomicilio(idPedido=idPedido)

                nombreVar.set("")
                telefonoVar.set("")
                direccionVar.set("")
                ciudadVar.set("")
                barrioVar.set("")
                postalVar.set("")
                infoDomiEntry.delete("1.0", "end")

            for widgets in frameMesa.winfo_children():
                widgets.destroy()


            ###LABELS y ENTRYS###

            zonaLabel = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Eliminar Domicilio")
            zonaLabel.config(background=styles.BACKGROUND, font=('Abhadi', 14))
            zonaLabel.grid(column=2, row=0, padx=5, pady=5, sticky=tk.NSEW)


            labelIdPedido = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Id del Pedido")
            labelIdPedido.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            idPedidoVar = tk.StringVar()
            entryIdPedido = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=idPedidoVar)
            entryIdPedido.grid(column=0, row=1, padx=5, pady=5, sticky=tk.NSEW)




            labelNombre = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Nombre")
            labelNombre.grid(column=0, row=2, padx=5, pady=5, sticky=tk.NSEW)

            nombreVar = tk.StringVar()
            entryNombre = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=nombreVar,
                                state="readonly")
            entryNombre.grid(column=0, row=3, padx=5, pady=5, sticky=tk.NSEW)
            



            labelTelefono = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Telefono")
            labelTelefono.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NSEW)

            telefonoVar = tk.StringVar()
            entryTelefono = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=telefonoVar,
                                state="readonly")
            entryTelefono.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NSEW)
            



            labelCiudad = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Ciudad")
            labelCiudad.grid(column=2, row=2, padx=5, pady=5, sticky=tk.NSEW)

            ciudadVar = tk.StringVar()
            entryCiudad = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=ciudadVar,
                                state="readonly")
            entryCiudad.grid(column=2, row=3, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelDireccion = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Direccion")
            labelDireccion.grid(column=0, row=4, padx=5, pady=5, sticky=tk.NSEW)

            direccionVar = tk.StringVar()
            entryDireccion = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=direccionVar,
                                state="readonly")
            entryDireccion.grid(column=0, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelBarrio = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Barrio")
            labelBarrio.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NSEW)

            barrioVar = tk.StringVar()
            entryBarrio = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=barrioVar,
                                state="readonly")
            entryBarrio.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelPostal = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Codigo Postal")
            labelPostal.grid(column=2, row=4, padx=5, pady=5, sticky=tk.NSEW)

            postalVar = tk.StringVar()
            entryPostal = tk.Entry(master=frameMesa,
                                font=('Abhadi', 12),
                                textvariable=postalVar,
                                state="readonly")
            entryPostal.grid(column=2, row=5, padx=5, pady=5, sticky=tk.NSEW)
            
            



            labelInfo = tk.Label(master=frameMesa,
                            **styles.LABEL,
                            text="Informacion Adicional")
            labelInfo.grid(column=0, row=6, padx=5, pady=5, sticky=tk.EW)


            infoDomiVar = tk.StringVar()
            infoDomiEntry = tk.Text(master=frameMesa,
                                       font=('Abhadi', 12),
                                       width=15, height=4,
                                state="disabled")
            infoDomiEntry.grid(row=6, column=1, sticky=tk.NSEW, padx=5, pady=5)


            ######BOTONES (ZONAELIMINAR)#################

            botonBuscar = tk.Button(master=frameMesa,
                                        text="  Buscar",
                                        **styles.BUTTON,
                                        command=buscar,
                                        image=self.iconoBuscar)
            
            botonBuscar.config(height=18)
            botonBuscar.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
            botonBuscar.bind('<Enter>', styles.on_enter)
            botonBuscar.bind('<Leave>', styles.on_leave)


            botonBorrar = tk.Button(master=frameMesa,
                                        text="Borrar",
                                        **styles.BUTTON,
                                        image=self.iconoBorrar25px,
                                        command=eliminarDomicilio)
            
            botonBorrar.config(height=30)
            botonBorrar.grid(row=7, column=1, padx=5, pady=5, sticky=tk.NSEW)
            botonBorrar.bind('<Enter>', styles.on_enter)
            botonBorrar.bind('<Leave>', styles.on_leave)

        def convertir_fecha(fecha):
                partes = fecha.split('/')
                fecha = partes[2]+"-"+partes[0]+"-"+partes[1]
                return datetime.strptime(fecha, '%y-%m-%d').strftime('%Y-%m-%d')

        def rutaToTxt():

            hoy = datetime.now()
            hoyStr =f"{hoy.month}.{hoy.day}.{hoy.year % 100}"
            hoyStrPedido =f"{hoy.month}/{hoy.day}/{hoy.year % 100}"
            hoyStrPedido = convertir_fecha(hoyStrPedido)

            path = "rutas/"+hoyStr+".txt"


            try:
                with open(resource_path(path), 'w') as txtPedido:
                    txtPedido.write(f'########DOMICILIOS DEL DIA:  {hoyStr}  ########')
                    txtPedido.write("\n\n")

                    conn = sql.connect(resource_path("database\\ravello.db"))
                    c = conn.cursor()

                    c.execute("SELECT * FROM pedido WHERE fechaEntrega = ? AND idDomicilio > 0", (hoyStrPedido,))
                    registros = c.fetchall()
                    
                    global count
                    count=0

                    for registro in registros:
                        print(f"registo: {registro}")

                        c.execute("SELECT * FROM domicilio WHERE idPedido = ?", (registro[0],))
                        domicilio = c.fetchone()
                      
                        
                        print(f"Domicilio: {domicilio}")

                        if domicilio[9] == "zona suroccidental":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona sur":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona sur2":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona suroriental":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona centro oriental":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona centro occidental":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona suroriental":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona nororiental":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona noroccidental":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

                        if domicilio[9] == "zona norte":
                            print("paso la sapa esta!")
                            idPedido = str(registro[0])
                            infoAdicional = str(registro[4])
                            tarjeta = str(registro[5])

                            idDomicilio = str(domicilio[0])
                            nombre = domicilio[1]
                            telefono = str(domicilio[2])
                            direccion = domicilio[3]
                            barrio = domicilio[4]
                            ciudad = domicilio[5]
                            infoAdicionalDomi= domicilio[7]
                            zona = domicilio[9]


                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                            cliente = c.fetchone()
                            clienteNombre = cliente[1]
                            clienteTelefono = str(cliente[2])
                                                    
                            c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                            productos = c.fetchall()

                            txtPedido.write(f"ZONA: {zona}\n")

                            txtPedido.write(f"ID PEDIDO: {idPedido}\n")
            
                            txtPedido.write(f"Cliente que Envia: {clienteNombre}\n")
                            txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                            txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("\n\n")
                            txtPedido.write("INFORMACION DEL DOMICILIO\n")
                            txtPedido.write(f"id del Domicilio: {idDomicilio}\n")
                            txtPedido.write(f"Nombre de quien recibe: {nombre}\n")
                            txtPedido.write(f"Telefono de quien recibe: {telefono}\n")
                            txtPedido.write(f"Direccion: {direccion}\n")
                            txtPedido.write(f"Barrio: {barrio}\n")
                            txtPedido.write(f"Ciudad: {ciudad}\n")
                            txtPedido.write(f"Informacion Adicional de Entrega: {infoAdicionalDomi}\n")
                            txtPedido.write("\n\n")

                            for producto in productos:

                                c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                                productoInfo = c.fetchone()
                                

                                cantidad = str(producto[2])
                                txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}\nNivel de Cuidado: {productoInfo[4]}\n\n")
                                count+=1
                                txtPedido.write("\n\n")

            except FileNotFoundError:
                print("The 'docs' directory does not exist")

        ##########BOTONES########################

        botonAgregar = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" AGREGAR DOMICILIO A PEDIDO",
                                image=self.iconoNuevo,
                                command=zonaAgregar)
        botonAgregar.pack(padx=10, pady=5, fill="both", expand=True)
        botonAgregar.config(font=("Abhadi", 14), wraplength=250)
        botonAgregar.bind('<Enter>', styles.on_enter)
        botonAgregar.bind('<Leave>', styles.on_leave)

        botonEditar = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" EDITAR INFORMACION DE DOMICILIO",
                                image=self.iconoEditar,
                                command=zonaEditar)
        botonEditar.pack(padx=10, pady=5, fill="both", expand=True)
        botonEditar.config(font=("Abhadi", 14), wraplength=250)
        botonEditar.bind('<Enter>', styles.on_enter)
        botonEditar.bind('<Leave>', styles.on_leave)

        botonEliminar = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" ELIMINAR DOMICILIO DE PEDIDO",
                                image=self.iconoBorrar,
                                command=zonaEliminar)
        botonEliminar.pack(padx=10, pady=5, fill="both", expand=True)
        botonEliminar.config(font=("Abhadi", 14), wraplength=250)
        botonEliminar.bind('<Enter>', styles.on_enter)
        botonEliminar.bind('<Leave>', styles.on_leave)



        botonPrint = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" GENERAR RUTA DE DOMICILIOS",
                                image=self.iconoPrinter,
                                command=rutaToTxt)
        botonPrint.pack(padx=10, pady=5, fill="both", expand=True)
        botonPrint.config(font=("Abhadi", 14), wraplength=250)
        botonPrint.bind('<Enter>', styles.on_enter)
        botonPrint.bind('<Leave>', styles.on_leave)



        botonBack = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" VOLVER",
                                image=self.iconoBack,
                                command=self.manager.to_home)
        botonBack.pack(padx=10, pady=5, fill="both", expand=True)
        botonBack.config(font=("Abhadi", 14), wraplength=250)
        botonBack.bind('<Enter>', styles.on_enter)
        botonBack.bind('<Leave>', styles.on_leave)