import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path
from datetime import datetime



class PedidosTabla(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(master=root, background=styles.LIGHT_BACKGROUND)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.controller = Controller()
        self.manager = manager
        self.initWidgets()

    def initWidgets(self):

        self.iconoBack = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoBack25px.png")))
        self.iconoBuscar = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoBuscar25px.png")))
        self.iconoRefresh = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoRefresh.png")))
        self.iconoPrinter = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoPrinter.png")))

    
            
        def Filtro():
            
            
            seleccion = cajaFiltros.get()
            busqueda = entryFiltro.get()
            treeTabla.delete(*treeTabla.get_children())
            conn = sql.connect(resource_path("database\\ravello.db"))
            c = conn.cursor()

            c.execute("SELECT * FROM pedido")
            registros = c.fetchall()

        

            global count
            count = 0

            if busqueda != "" or busqueda=="":
                if seleccion == "ID":
                    treeTabla.delete(*treeTabla.get_children())

                    # Filtrar elementos de la tabla según el texto de búsqueda
                    for registro in registros:
                        if busqueda in str(registro[0]): 
                            # Comprobar si el texto de búsqueda está en el elemento

                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],)) 
                            cliente = c.fetchone()

                            if registro[3] == 0:
                                domicilio = "recoge"
                            else:
                                domicilio = registro[3]
                            
                            if count % 2 == 0:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="evenrow")
                            else:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="oddrow")    
                            count+=1
                            
                elif seleccion == "Fecha":
                    treeTabla.delete(*treeTabla.get_children())

                    # Filtrar elementos de la tabla según el texto de búsqueda
                    for registro in registros:
                        if busqueda in str(registro[1]): 
                            # Comprobar si el texto de búsqueda está en el elemento

                            c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],)) 
                            cliente = c.fetchone()

                            if registro[3] == 0:
                                domicilio = "recoge"
                            else:
                                domicilio = registro[3]

                            if count % 2 == 0:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="evenrow")
                            else:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="oddrow")    
                            count+=1

                elif seleccion == "Pendientes de Pago":
                    treeTabla.delete(*treeTabla.get_children())

                    # Filtrar elementos de la tabla según el texto de búsqueda
                    for registro in registros:

                        c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],)) 
                        cliente = c.fetchone()

                        if registro[8] == "Por Pagar":

                            if registro[3] == 0:
                                domicilio = "recoge"
                            else:
                                domicilio = registro[3]

                            if count % 2 == 0:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="evenrow")
                            else:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="oddrow")    
                            count+=1

                elif seleccion == "Entrega Pendiente":
                    treeTabla.delete(*treeTabla.get_children())

                    # Filtrar elementos de la tabla según el texto de búsqueda
                    for registro in registros:

                        c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],)) 
                        cliente = c.fetchone()

                        if registro[8] == "Entrega Pendiente":

                            if registro[3] == 0:
                                domicilio = "recoge"
                            else:
                                domicilio = registro[3]

                            if count % 2 == 0:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="evenrow")
                            else:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="oddrow")    
                            count+=1

                elif seleccion == "Entrega no Completada":
                    treeTabla.delete(*treeTabla.get_children())

                    # Filtrar elementos de la tabla según el texto de búsqueda
                    for registro in registros:
                        c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))  
                        cliente = c.fetchone()

                        if registro[8] == "Entrega no Completada":

                            if registro[3] == 0:
                                domicilio = "recoge"
                            else:
                                domicilio = registro[3]

                            if count % 2 == 0:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="evenrow")
                            else:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="oddrow")    
                            count+=1
                
                elif seleccion == "Entregados":
                    treeTabla.delete(*treeTabla.get_children())

                    # Filtrar elementos de la tabla según el texto de búsqueda
                    for registro in registros:

                        c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))  
                        cliente = c.fetchone()

                        if registro[8] == "Entregado":

                            if registro[3] == 0:
                                domicilio = "recoge"
                            else:
                                domicilio = registro[3]

                            if count % 2 == 0:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="evenrow")
                            else:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="oddrow")    
                            count+=1

                elif seleccion == "Pedidos del Dia":
                    treeTabla.delete(*treeTabla.get_children())

                    hoy = datetime.now()
                    hoyStr =f"{hoy.month}/{hoy.day}/{hoy.year % 100}"


                    # Filtrar elementos de la tabla según el texto de búsqueda
                    for registro in registros:

                        c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],)) 
                        cliente = c.fetchone()

                        if registro[1] == hoyStr:

                            if registro[3] == 0:
                                domicilio = "recoge"
                            else:
                                domicilio = registro[3]

                            if count % 2 == 0:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="evenrow")
                            else:
                                treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="oddrow")    
                            count+=1

                else:
                    treeTabla.delete(*treeTabla.get_children())
                    fetchVentasDB()
        
        def fetchVentasDB():
            treeTabla.delete(*treeTabla.get_children())
            conn = sql.connect(resource_path("database\\ravello.db"))
            c = conn.cursor()

            c.execute("SELECT * FROM pedido")
            registros = c.fetchall()
            
            global count
            count=0

            for registro in registros:
                
                if registro[3] == 0:
                    domicilio = "recoge"
                else:
                    domicilio = registro[3]

                
                c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                cliente = c.fetchone()
                

                if count % 2 == 0:
                    treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="evenrow")
                else:
                    treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], cliente[2], domicilio, registro[4], registro[5], registro[6], registro[7], registro[8]), tags="oddrow")    
                count+=1

            conn.commit()
            c.close()
            conn.close()

        def zonaFactura(event):

            def marcarEntrega():
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                pedido = idPedido.get() 
                estado = "Entregado"  

                try:
                    c.execute("UPDATE pedido SET estado = ? WHERE idPedido = ?", (estado, pedido))
                    
                    conn.commit()

                except sql.Error as e:
                    print(f"An error occurred: {e}")

                finally:
                    # Close the connection
                    conn.close()

                
                winFactura.destroy()
                fetchVentasDB()

            def marcarNoEntrega():
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                pedido = idPedido.get() 
                estado = "Entrega no Completada"  

                try:
                    c.execute("UPDATE pedido SET estado = ? WHERE idPedido = ?", (estado, pedido))
                    
                    conn.commit()

                except sql.Error as e:
                    print(f"An error occurred: {e}")

                finally:
                    # Close the connection
                    conn.close()

                
                winFactura.destroy()
                fetchVentasDB()

            def marcarPago():
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                pedido = idPedido.get() 
                estado = "Entrega Pendiente"  

                try:
                    c.execute("UPDATE pedido SET estado = ? WHERE idPedido = ?", (estado, pedido))
                    
                    conn.commit()

                except sql.Error as e:
                    print(f"An error occurred: {e}")

                finally:
                    # Close the connection
                    conn.close()

                
                winFactura.destroy()
                fetchVentasDB()

            def borrarPedido():
                self.controller.delPedido(idPedido.get())

                winFactura.destroy()
                fetchVentasDB()

            def tablaProductos():

                

                def fetchProductosVentaDB():
                    treeFactura.delete(*treeFactura.get_children())
                    conn = sql.connect(resource_path("database\\ravello.db"))
                    c = conn.cursor()

                    pedidoId = int(valores[0])

                    c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (pedidoId,))
                    registros = c.fetchall()


                    global count
                    count=0

                    for registro in registros:
                        
                        productoID = registro[1]
                        c.execute("SELECT * FROM producto WHERE idProducto = ?", (productoID,))
                        producto = c.fetchone()


                        productoNombre = str(producto[1])
                        productoPrecio = int(producto[3])

                        if count % 2 == 0:
                            treeFactura.insert(parent="", index=0, iid=count, values=( registro[1], productoNombre, registro[2], productoPrecio), tags="evenrow")
                        else:
                            treeFactura.insert(parent="", index=0, iid=count, values=( registro[1], productoNombre, registro[2], productoPrecio), tags="oddrow")    
                        count+=1

                    conn.commit()

                    c.close()
                    conn.close()
                
                estilo = ttk.Style()
                estilo.theme_use("default")
                estilo.configure("Treeview",
                                background = "WHITE",
                                foreground = "BLACK",
                                rowheight = 30,
                                fieldbackground = "WHITE")
                estilo.map('Treeview',
                        background=[('selected', styles.COMPONENT)])

                scrollbar = tk.Scrollbar(contenedor)
                scrollbar.pack(side="right", fill="y")

                treeFactura = ttk.Treeview(contenedor, yscrollcommand=scrollbar.set, selectmode="extended")

                scrollbar.config(command=treeFactura.yview)

                treeFactura['columns'] = ("ID Producto", "Nombre", "Cantidad", "Precio")

                treeFactura.column("#0", width=0, stretch=False)
                treeFactura.column("ID Producto", width=20, minwidth=20, anchor="center")
                treeFactura.column("Nombre", width=40, minwidth=20, anchor="e")
                treeFactura.column("Cantidad", width=20, minwidth=20, anchor="center")
                treeFactura.column("Precio", width=20, minwidth=20, anchor="center")
                

                treeFactura.heading("ID Producto", text="ID Producto", anchor="center")
                treeFactura.heading("Nombre", text="Nombre ", anchor="e")
                treeFactura.heading("Cantidad", text="Cantidad", anchor="center")
                treeFactura.heading("Precio", text="Precio", anchor="center")
                
                

                treeFactura.tag_configure("oddrow", background="WHITE")
                treeFactura.tag_configure("evenrow", background="#FFC9C6")

                fetchProductosVentaDB()
                treeFactura.pack(padx=10, pady=15, fill="both", expand=True)


            winFactura = tk.Toplevel()
            winFactura.geometry('720x360')
            winFactura.title("Orden de Pedido")
            #winFactura.iconbitmap(resource_path("icono.ico"))
            winFactura.resizable(width=False, height=False)
            winFactura.columnconfigure(0, weight=1)
            winFactura.rowconfigure(0, weight=1)

            item = treeTabla.focus()
            valores = treeTabla.item(item, 'values')

            print(valores)

            idPedido = tk.StringVar()
            idPedido.set(str(valores[0]))
            
            fechaEntregaVar = tk.StringVar()
            fechaEntregaVar.set(str(valores[1]))
            
            telefonoClienteVar = tk.StringVar()
            telefonoClienteVar.set(str(valores[2]))

            clienteVar = tk.IntVar()
            conn = sql.connect(resource_path("database\\ravello.db"))
            c = conn.cursor()
            c.execute("SELECT * FROM cliente WHERE telefono = ?", (telefonoClienteVar.get(),)) 
            registros = c.fetchone()
            clienteVar.set(registros[1])
            

            idDomicilioVar = tk.StringVar()
            idDomicilioVar.set(valores[3])
            
            estadoVar = tk.StringVar()
            estadoVar.set(valores[8])
            
            medioCompraVar = tk.StringVar()
            medioCompraVar.set(valores[7])
            
            valorVar = tk.StringVar()
            valorVar.set(valores[6])


            contenedor = tk.Frame(winFactura,
                                bg=styles.LIGHT_BACKGROUND)
            contenedor.columnconfigure(0, weight=1)                
            contenedor.rowconfigure(0, weight=1)
            contenedor.pack(fill="both", expand=True)

            frameDatos = tk.Frame(contenedor,
                                bg=styles.LIGHT_BACKGROUND)
            frameDatos.columnconfigure(0, weight=1)
            frameDatos.columnconfigure(1, weight=1)
            frameDatos.columnconfigure(2, weight=1)
            frameDatos.columnconfigure(3, weight=1)
            frameDatos.columnconfigure(4, weight=1)
            frameDatos.pack(fill="both", expand=True)


            labelFecha = tk.Label(frameDatos,
                                text='Fecha Entrega',
                                **styles.LABEL)
            labelFecha.grid(row=0, column=0, pady=2, padx=2, sticky=tk.NSEW)

            entryFecha = tk.Entry(frameDatos,
                                textvariable=fechaEntregaVar,
                                state='readonly')
            entryFecha.grid(row=0, column=1, pady=2, padx=2, sticky=tk.EW)


            labelId = tk.Label(frameDatos,
                            **styles.LABEL,
                            textvariable=idPedido)
            labelId.grid(row=0, column=4, pady=2, padx=2, sticky=tk.NSEW)


            valorLabel = tk.Label(frameDatos,
                                text='Valor',
                                **styles.LABEL)
            valorLabel.grid(row=1, column=0, pady=2, padx=2, sticky=tk.NSEW)

            valorEntry = tk.Entry(frameDatos,
                                textvariable=valorVar,
                                state='readonly')
            valorEntry.grid(row=1, column=1, pady=2, padx=2, sticky=tk.EW)
            


            medioLabel = tk.Label(frameDatos,
                                text='Medio Pago',
                                **styles.LABEL)
            medioLabel.grid(row=2, column=0, pady=2, padx=2, sticky=tk.NSEW)

            medioEntry = tk.Entry(frameDatos,
                                textvariable=medioCompraVar,
                                state='readonly')
            medioEntry.grid(row=2, column=1, pady=2, padx=2, sticky=tk.EW)

            

            clienteLabel = tk.Label(frameDatos,
                                text='Cliente',
                                **styles.LABEL)
            clienteLabel.grid(row=3, column=0, pady=2, padx=2, sticky=tk.NSEW)

            clienteEntry = tk.Entry(frameDatos,
                                textvariable=clienteVar,
                                state='readonly')
            clienteEntry.grid(row=3, column=1, pady=2, padx=2, sticky=tk.EW)

            

            telefonoClienteLabel = tk.Label(frameDatos,
                                text='Telefono',
                                **styles.LABEL)
            telefonoClienteLabel.grid(row=4, column=0, pady=2, padx=2, sticky=tk.NSEW)

            telefonoClienteEntry = tk.Entry(frameDatos,
                                textvariable=telefonoClienteVar,
                                state='readonly')
            telefonoClienteEntry.grid(row=4, column=1, pady=2, padx=2, sticky=tk.EW)
            
            

            domicilioLabel = tk.Label(frameDatos,
                                text='ID Domicilio',
                                **styles.LABEL)
            domicilioLabel.grid(row=1, column=2, pady=2, padx=2, sticky=tk.NSEW)

            domicilioEntry = tk.Entry(frameDatos,
                                textvariable=idDomicilioVar,
                                state='readonly')
            domicilioEntry.grid(row=1, column=3, pady=2, padx=2, sticky=tk.EW)
            
            

            estadoLabel = tk.Label(frameDatos,
                                text='Estado',
                                **styles.LABEL)
            estadoLabel.grid(row=2, column=2, pady=2, padx=2, sticky=tk.NSEW)

            estadoEntry = tk.Entry(frameDatos,
                                textvariable=estadoVar,
                                state='readonly')
            estadoEntry.grid(row=2, column=3, pady=2, padx=2, sticky=tk.EW)

            if estadoVar.get() == "Por Pagar":
                
                btnBorrar = tk.Button(frameDatos,
                                      **styles.BUTTON_H,
                                      text="Borrar Pedido",
                                      command=borrarPedido
                                      )
                btnBorrar.grid(row=3, column=3, pady=2, padx=2, sticky=tk.NSEW)
                btnBorrar.bind("<Enter>", styles.on_enter)
                btnBorrar.bind("<Leave>", styles.on_leave)

                btnMarcarPago = tk.Button(frameDatos,
                                      **styles.BUTTON_H,
                                      text="Marcar Pago",
                                      command=marcarPago)
                btnMarcarPago.grid(row=3, column=2, pady=2, padx=2, sticky=tk.NSEW)
                btnMarcarPago.bind("<Enter>", styles.on_enter)
                btnMarcarPago.bind("<Leave>", styles.on_leave)

            if estadoVar.get() == "Entrega Pendiente":
                
                btnEntregado = tk.Button(frameDatos,
                                      **styles.BUTTON_H,
                                      text="Marcar Entrega",
                                      command=marcarEntrega
                                      )
                btnEntregado.grid(row=3, column=3, pady=2, padx=2, sticky=tk.NSEW)
                btnEntregado.bind("<Enter>", styles.on_enter)
                btnEntregado.bind("<Leave>", styles.on_leave)

                btnEntregaIncom = tk.Button(frameDatos,
                                      **styles.BUTTON_H,
                                      text="Entrega no Completada",
                                      command=marcarNoEntrega,
                                      )
                btnEntregaIncom.grid(row=3, column=2, pady=2, padx=2, sticky=tk.NSEW)
                btnEntregaIncom.bind("<Enter>", styles.on_enter)
                btnEntregaIncom.bind("<Leave>", styles.on_leave)

            if estadoVar.get() == "Entrega no Completada":
                
                btnEntregado = tk.Button(frameDatos,
                                      **styles.BUTTON_H,
                                      text="Marcar Entrega",
                                      command=marcarEntrega
                                      )
                btnEntregado.grid(row=3, column=3, pady=2, padx=2, sticky=tk.NSEW)
                btnEntregado.bind("<Enter>", styles.on_enter)
                btnEntregado.bind("<Leave>", styles.on_leave)


            tablaProductos()

        
        frameBusqueda = tk.Frame(self,
                            bg=styles.LIGHT_BACKGROUND)
        frameBusqueda.pack(fill="both", expand=True)

        frameTabla =tk.Frame(self,
                            bg=styles.LIGHT_BACKGROUND)
        frameTabla.pack(fill="both", expand=True)

        #######MENU######

        cajaFiltros = ttk.Combobox(frameBusqueda,
                            height=25,
                            state="readonly",
                            values=["ID","Fecha","Pendientes de Pago", "Entrega Pendiente", "Entrega no Completada", "Entregados", "Pedidos del Dia"])
        cajaFiltros.grid(row=0, column=0, padx=10, pady=5, sticky=tk.EW)
        
        entryFiltro = tk.Entry(frameBusqueda,
                            font=('Abhadi', 12))
        entryFiltro.bind('<KeyRelease>', lambda event: Filtro())
        entryFiltro.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)

        botonActualizar = tk.Button(frameBusqueda,
                                    text=" ACTUALIZAR",
                                    **styles.BUTTON,
                                    image=self.iconoRefresh,
                                    command=Filtro)
        botonActualizar.config(height=28)
        botonActualizar.bind("<Enter>", styles.on_enter)
        botonActualizar.bind("<Leave>", styles.on_leave)
        botonActualizar.grid(row=0, column=2, padx=10, pady=5, sticky=tk.NSEW)


        #######TABLA######
        
        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("Treeview",
                        background = "WHITE",
                        foreground = "BLACK",
                        rowheight = 30,
                        fieldbackground = "WHITE")
        estilo.map('Treeview',
                background=[('selected', styles.COMPONENT)])

        treeBarra = tk.Scrollbar(frameTabla)
        treeBarra.pack(side="right", fill="y")

        treeTabla = ttk.Treeview(frameTabla, yscrollcommand=treeBarra.set, selectmode="extended")

        treeBarra.config(command=treeTabla.yview)

        treeTabla['columns'] = ("ID", "Fecha", "Cliente", "idDomicilio", "infoAdicional", "Mensaje", "Valor", "Medio de Pago", "Estado")

        treeTabla.column("#0", width=0, stretch=False)
        treeTabla.column("ID", width=10, minwidth=10, anchor="center")
        treeTabla.column("Fecha", width=30, minwidth=80, anchor="e")
        treeTabla.column("Cliente", width=40, minwidth=20, anchor="center")
        treeTabla.column("idDomicilio", width=20, minwidth=20, anchor="center")
        treeTabla.column("infoAdicional", width=80, minwidth=20, anchor="w")
        treeTabla.column("Mensaje", width=80, minwidth=20, anchor="w")
        treeTabla.column("Valor", width=30, minwidth=20, anchor="center")
        treeTabla.column("Medio de Pago", width=20, minwidth=20, anchor="e")
        treeTabla.column("Estado", width=20, minwidth=20, anchor="center")
        

        treeTabla.heading("ID", text="ID", anchor="center")
        treeTabla.heading("Fecha", text="Fecha Entrega ", anchor="e")
        treeTabla.heading("Cliente", text="Cliente", anchor="center")
        treeTabla.heading("idDomicilio", text="N°Domicilio", anchor="center")
        treeTabla.heading("infoAdicional", text="Informacion Adicional", anchor="w")
        treeTabla.heading("Mensaje", text="Tarjeta", anchor="w")
        treeTabla.heading("Valor", text="Valor Total", anchor="center")
        treeTabla.heading("Medio de Pago", text="Medio de Pago", anchor="center")
        treeTabla.heading("Estado", text="Estado", anchor="center")

        treeTabla.tag_configure("oddrow", background="WHITE")
        treeTabla.tag_configure("evenrow", background=styles.HIGHLIGHT)

        fetchVentasDB()
        treeTabla.bind('<Double-1>', zonaFactura)
        treeTabla.pack(fill="both", expand=True)
