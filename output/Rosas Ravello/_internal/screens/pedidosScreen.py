import tkinter as tk
import time
from datetime import datetime, date
from tkcalendar import Calendar
from tkinter import ttk
import sqlite3 as sql
from modules.controller import Controller
from modules.controller import resource_path
from components.pedidosTabla import PedidosTabla
from PIL import Image, ImageTk
from style import styles

class PedidosScreen(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(master=root, background=styles.BACKGROUND)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.manager = manager
        self.controller = Controller()
        self.initWidgets()

    def initWidgets(self):

        self.iconoVenta = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoVenta25px.png")))
        self.iconoBack = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoBack25px.png")))
        self.iconoBuscar = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoBuscar25px.png")))
        self.iconoIngresos = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoIngresos25px.png")))
        self.iconoGuardar = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoGuardar.png")))
        self.iconoRefresh = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoRefresh.png")))
        self.iconoPrinter = ImageTk.PhotoImage(Image.open(resource_path("assets\\iconoPrinter.png")))

        def calendario(entry):   
            global calendarioWin, cal


            calendarioWin = tk.Toplevel()
            calendarioWin.grab_set()
            calendarioWin.title("Seleccionar Fecha")
            calendarioWin.geometry("250x220")

            cal = Calendar(calendarioWin,
                           selectmode="day",
                           datepattern="d/m/y")
            cal.pack(padx=5, pady=2, fill="both", expand=True)

            enviarBoton = tk.Button(calendarioWin,
                                    **styles.BUTTON,
                                    text="Seleccionar",
                                    command=lambda: setFecha(entry))
            enviarBoton.config(height=10)
            enviarBoton.pack(padx=5, pady=2)

        def setFecha(entry):
            entry.set(cal.get_date())
            calendarioWin.destroy()

        def convertir_fecha(fecha):
                partes = fecha.split('/')
                fecha = partes[2]+"-"+partes[0]+"-"+partes[1]
                fecha = datetime.strptime(fecha, '%y-%m-%d')
                return fecha.date()
        

        def reloj():
            labelTime = tk.Label(master=frameMenu, 
                                 **styles.LABEL,
                                 width=30,
                                 )
            
            labelTime.grid(row=0, column=0, padx=10, pady=5)

            hora_actual = time.strftime('%d %b %Y %I:%M:%S')
            labelTime.config(text=hora_actual)
            frameMenu.after(1000, reloj)

        def zonaVenta():

            #def _on_mousewheel(event):
                #canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

            
            def labelProductos(event):

                

                
                def domicilioForm():
                    if domiciliosCheckVar.get() == True:

                        nombreLabel = tk.Label(menuDomicilios,
                                   **styles.LABEL,
                                   text="Nombre")
                        nombreLabel.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=5)


                        
                        nombreEntry = tk.Entry(menuDomicilios,
                                                textvariable=nombreVar,
                                                font=('Abhadi', 12)
                                                )
                        nombreEntry.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=5)
                        


                        telefonoLabel = tk.Label(menuDomicilios,
                                   **styles.LABEL,
                                   text="Telefono")
                        telefonoLabel.grid(row=1, column=1, sticky=tk.NSEW, padx=10, pady=5)

                        
                        telefonoEntry = tk.Entry(menuDomicilios,
                                                textvariable=telefonoVar,
                                                font=('Abhadi', 12)
                                                )
                        telefonoEntry.grid(row=1, column=2, sticky=tk.NSEW, padx=10, pady=5)



                        direccionLabel = tk.Label(menuDomicilios,
                                   **styles.LABEL,
                                   text="Dirección")
                        direccionLabel.grid(row=0, column=3, sticky=tk.NSEW, padx=10, pady=5)

                        
                        direccionEntry = tk.Entry(menuDomicilios,
                                                textvariable=direccionVar,
                                                font=('Abhadi', 12)
                                                )
                        direccionEntry.grid(row=0, column=4, sticky=tk.NSEW, padx=10, pady=5)



                        barrioLabel = tk.Label(menuDomicilios,
                                   **styles.LABEL,
                                   text="Barrio")
                        barrioLabel.grid(row=1, column=3, sticky=tk.NSEW, padx=10, pady=5)

                        
                        BarrioEntry = tk.Entry(menuDomicilios,
                                                textvariable=barrioVar,
                                                font=('Abhadi', 12)
                                                )
                        BarrioEntry.grid(row=1, column=4, sticky=tk.NSEW, padx=10, pady=5)



                        ciudadLabel = tk.Label(menuDomicilios,
                                   **styles.LABEL,
                                   text="Ciudad")
                        ciudadLabel.grid(row=2, column=3, sticky=tk.NSEW, padx=10, pady=5)

                        
                        ciudadEntry = tk.Entry(menuDomicilios,
                                                textvariable=ciudadVar,
                                                font=('Abhadi', 12)
                                                )
                        ciudadEntry.grid(row=2, column=4, sticky=tk.NSEW, padx=10, pady=5)



                        postalLabel = tk.Label(menuDomicilios,
                                   **styles.LABEL,
                                   text="Código Postal")
                        postalLabel.grid(row=3, column=3, sticky=tk.NSEW, padx=10, pady=5)

                        
                        postalEntry = tk.Entry(menuDomicilios,
                                                textvariable=postalVar,
                                                font=('Abhadi', 12)
                                                )
                        postalEntry.grid(row=3, column=4, sticky=tk.NSEW, padx=10, pady=5)



                        infoDomiLabel = tk.Label(menuDomicilios,
                                   **styles.LABEL,
                                   text="Información Adicional")
                        infoDomiLabel.grid(row=4, column=1, sticky=tk.NSEW, padx=10, pady=5)


                        
                        infoDomiEntry = tk.Entry(menuDomicilios,
                                                font=('Abhadi', 12),
                                                textvariable=infoDomiVar
                                                )
                        infoDomiEntry.grid(row=4, column=2, sticky=tk.NSEW, padx=10, pady=5)




                        
                    else:
                        for widgets in menuDomicilios.winfo_children():
                            widgets.destroy()
                            ponerCheckBox()

                def ponerCheckBox():
                    domiciliosCheck = tk.Checkbutton(master=menuDomicilios,
                                        border=0,
                                        text=" ¿Domicilio? ",
                                        font=("Abhadi", 12),
                                        variable=domiciliosCheckVar,
                                        onvalue=True, offvalue=False,
                                        background=styles.LIGHT_BACKGROUND,
                                        foreground="WHITE",
                                        selectcolor=styles.LIGHT_BACKGROUND,
                                        command=domicilioForm)
                                            
                
                    domiciliosCheck.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=5)


                '''def añadirProductoGenerico(event, index):
                    if entrysIds[index].get() == "":
                        entrysIds[index].config(state="readonly")
                        entrysNombres[index].config(state="normal")
                        entrysPrecios[index].config(state="normal")'''
                
                def nuevoPedido():
                    ####PEDIDO####
                    cliente = ClienteVar.get()
                    medioPago = cboxMedioPago.get()
                    valor = totalVar.get()

                    
                    fechaEntrega = convertir_fecha(fechaEntregaVar.get())
                    

                    infoPedido = infoEntry.get("1.0","end-1c")
                    tarjeta = mensajeEntry.get("1.0","end-1c")
                    estado = "Por Pagar"
                    
                    
                    ####DOMICILIO####
                    if domiciliosCheckVar.get() == True:
                        nombre = nombreVar.get()
                        telefono = int(telefonoVar.get())
                        nomenclatura = direccionVar.get()
                        barrio = barrioVar.get().lower()
                        municipio = ciudadVar.get().lower()
                        postal = int(postalVar.get())
                        infoAdicional = infoDomiVar.get()

                        domicilio=[nombre, telefono, nomenclatura, barrio, municipio, postal, infoAdicional]
                    else:
                        domicilio=[]



                    productos = []


                    for i in range(len(entrysProductos)):
                        if entrysProductos[i].get() != "":
                            for producto in productos_lista:
                                if producto[0] == entrysProductos[i].get():
                                    idProducto = producto[1]

                            productos.append([idProducto, int(entrysUnidades[i].get())])
                        


                    self.controller.newPedido(fechaEntrega=fechaEntrega,
                                             idCliente=cliente,
                                             valorTotal= valor,
                                             medioPago=medioPago,
                                             infoAdicionalPedido=infoPedido,
                                             mensajeTarjeta=tarjeta,
                                             estado=estado,
                                             productos=productos,
                                             infoDomicilio=domicilio)
                    
                    zonaVenta()
                                       
                def fillEntrys(event, index):


                    conn = sql.connect(resource_path("database\\ravello.db"))
                    c = conn.cursor()

                    
                    nombreProducto = entrysProductos[index].get()
                    idProducto = 0

                    for producto in productos_lista:
                        if producto[0] == nombreProducto:
                            idProducto = producto[1]
                                     
                    c.execute("SELECT * FROM producto WHERE idProducto = ?", (idProducto,))
                    producto = c.fetchone()

                    precioVar = tk.IntVar()
                    precioVar.set(producto[3])
                    entrysPrecios[index].config(textvariable=precioVar)

                    c.close()
                    conn.close()

                def fillValores(event, index):
                    conn = sql.connect(resource_path("database\\ravello.db"))
                    c = conn.cursor()

                    
                    nombreProducto = entrysProductos[index].get()
                    idProducto = 0

                    for producto in productos_lista:
                        if producto[0] == nombreProducto:
                            idProducto = producto[1]
                    
                    if idProducto!=0: 
                        c.execute("SELECT * FROM producto WHERE idProducto = ?", (idProducto,))
                        producto = c.fetchone()

                        suma_valor = int(entrysUnidades[index].get())*int(producto[3])

                        totalVar.set(totalVar.get()+suma_valor)

                        entrysProductos[index].config(state="disabled")
                        entrysUnidades[index].config(state="readonly")

                    c.close()
                    conn.close()

                spinCantidadProductos.config(state="disabled")
                
                labelNombre = ttk.Label(menu2,
                                   **styles.LABEL,
                                   text="Nombre")
                labelNombre.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=5)

                labelUnd = tk.Label(menu2,
                                   **styles.LABEL,
                                   text="Cantidad")
                labelUnd.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=5)


                labelPrecio = tk.Label(menu2,
                                   **styles.LABEL,
                                   text="Precio")
                labelPrecio.grid(row=0, column=3, sticky=tk.NSEW, padx=10, pady=5)



                labels = []
                entrysProductos = []
                entrysUnidades = []
                entrysNombres = []
                entrysPrecios = []
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()
                c.execute("SELECT nombre, idProducto FROM producto")
                productos_lista = c.fetchall()

                cProductos = int(spinCantidadProductos.get())



                
                for i in range(cProductos):

                    producto = tk.Label(menu2,
                                        **styles.LABEL,
                                        text=f'Producto #{i+1}'
                                        )
                    producto.grid(row=i+1, column=0, sticky=tk.NSEW, padx=10, pady=5)
                    labels.append(producto)


                    ###RECOGER DATOS DE PRODUCTOS DE LA BASE DE DATOS###
                    productos_values = [producto[0]  for producto in productos_lista]
                    
                    productoVar = tk.StringVar()
                    productoEntry = ttk.Combobox(menu2,
                                             font=('Abhadi', 12),
                                             values=productos_values,
                                             textvariable=productoVar,
                                             state="readonly",
                                             width=50)
                    productoEntry.grid(row=i+1, column=1, sticky=tk.NSEW, padx=10, pady=5)
                    productoEntry.bind('<Return>', lambda event, index=i: fillEntrys(event, index))
                    entrysProductos.append(productoEntry)

                    cantidad = tk.Entry(menu2,
                                             font=('Abhadi', 12))
                    cantidad.grid(row=i+1, column=2, sticky=tk.NSEW, padx=10, pady=5)
                    cantidad.bind('<Return>', lambda event, index=i: fillValores(event, index))
                    entrysUnidades.append(cantidad)


                    precioProducto = tk.Entry(menu2,
                                             font=('Abhadi', 12),
                                             state="readonly")
                    precioProducto.grid(row=i+1, column=3, sticky=tk.NSEW, padx=10, pady=5)
                    entrysPrecios.append(precioProducto)




               
                LabelTotal = tk.Label(menu2,
                                   **styles.LABEL,
                                   text="Total")
                LabelTotal.grid(row=cProductos+3, column=1, sticky=tk.NSEW, padx=10, pady=5)


                totalVar = tk.IntVar()
                entryTotal = tk.Entry(menu2,
                                         state="readonly",
                                         textvariable=totalVar,
                                         font=('Abhadi', 12)
                                         )
                entryTotal.grid(row=cProductos+3, column=2, sticky=tk.NSEW, padx=10, pady=5)

                
                botonGuardar = tk.Button(frameInterior,
                                         **styles.BUTTON,
                                         text=" GUARDAR",
                                         image=self.iconoGuardar,
                                         command=nuevoPedido)
                botonGuardar.config(height=28, font=('Abhadi', 12))
                botonGuardar.bind("<Enter>", styles.on_enter)
                botonGuardar.bind("<Leave>", styles.on_leave)
                botonGuardar.grid(row=3, column=0, sticky=tk.NSEW, padx=10, pady=5)


                infoLabel = tk.Label(menu2,
                                        **styles.LABEL,
                                        text="Información Adicional: ")
                infoLabel.grid(row=cProductos+4, column=0, sticky=tk.EW, padx=10, pady=15)

                infoEntry = tk.Text(menu2,
                                       font=('Abhadi', 12),
                                       width=15, height=4)
                infoEntry.grid(row=cProductos+4, column=1, sticky=tk.NSEW, padx=10, pady=15)


                mensajeLabel = tk.Label(menu2,
                                        **styles.LABEL,
                                        text="Tarjeta: ")
                mensajeLabel.grid(row=cProductos+4, column=2, sticky=tk.EW, padx=10, pady=15)

                mensajeEntry = tk.Text(menu2,
                                       font=('Abhadi', 12),
                                       width=20, height=4)
                mensajeEntry.grid(row=cProductos+4, column=3, sticky=tk.NSEW, padx=10, pady=15)

                ponerCheckBox()

                nombreVar = tk.StringVar()
                telefonoVar = tk.StringVar()
                direccionVar = tk.StringVar()
                barrioVar = tk.StringVar()
                ciudadVar = tk.StringVar()
                postalVar = tk.StringVar()
                infoDomiVar = tk.StringVar()

            #######DEFINICION DE LOS MENUS############

            for widgets in zonaTrabajo.winfo_children():
                widgets.destroy()


            zonaTrabajo.columnconfigure(0, weight=1)
            zonaTrabajo.rowconfigure(0, weight=1)

            canvas = tk.Canvas(zonaTrabajo,
                               bg=styles.BACKGROUND)
            scrollbar = ttk.Scrollbar(zonaTrabajo, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=scrollbar.set)
            
            frameInterior = ttk.Frame(canvas,
                                      )
            frameInterior.columnconfigure(0, weight=1)
            frameInterior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            menu1 = tk.LabelFrame(frameInterior,
                             bg=styles.BACKGROUND,
                             foreground="white",
                             text="Nueva Venta")
            menu1.grid(row=0, column=0, sticky=tk.NSEW)
            

            menu2 = tk.Frame(frameInterior,
                             bg=styles.BACKGROUND,
                             )
            menu2.grid(row=1, column=0, sticky=tk.NSEW)

            
            menuDomicilios = tk.LabelFrame(frameInterior,
                             bg=styles.BACKGROUND,
                             foreground="white",
                             text="Información sobre destinatario")
            menuDomicilios.grid(row=2, column=0, sticky=tk.NSEW)   
            domiciliosCheckVar = tk.BooleanVar()


            labelCliente = tk.Label(menu1,
                                    **styles.LABEL,
                                    text="Cliente",
                                    )
            labelCliente.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=2)

            labelMedioPago = tk.Label(menu1,
                                    **styles.LABEL,
                                    text="Medio de Pago",
                                    )
            labelMedioPago.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=2)


            labelCantidadProductos = tk.Label(menu1,
                                    **styles.LABEL,
                                    text="Cantidad de Productos",
                                    )
            labelCantidadProductos.grid(row=3, column=0, sticky=tk.NSEW, padx=5, pady=2)

            fechaLabel = tk.Label(menu1,
                                    **styles.LABEL,
                                    text="Fecha de Entrega",
                                    )
            fechaLabel.grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=2)
            
            fechaEntregaVar = tk.StringVar()
            fechaEntregaVar.set("mm/dd/yy")
            entryFecha1 = tk.Entry(menu1,
                                state="readonly",
                                textvariable=fechaEntregaVar
                                )
            entryFecha1.bind('<ButtonRelease-1>', lambda event: calendario(fechaEntregaVar))
            entryFecha1.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=2)

            '''ClienteVar = tk.IntVar()
            entryCliente = tk.Entry(menu1,
                                    font=('Abhadi', 12),
                                    textvariable=ClienteVar)
            entryCliente.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=2)
'''

            conn = sql.connect(resource_path("database\\ravello.db"))
            c = conn.cursor()
            c.execute("SELECT telefono FROM cliente")
            registros = c.fetchall()
            
            

            ClienteVar = tk.IntVar()

            entryCliente = ttk.Combobox(menu1,
                                         height=25,
                                         state="readonly",
                                         textvariable=ClienteVar,
                                         values=registros)
            entryCliente.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=2)
            

            cboxMedioPago = ttk.Combobox(menu1,
                                         height=25,
                                         state="readonly",
                                         values=["Efectivo","QR","Transferencia","Otro"])
            cboxMedioPago.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)

            spinCantidadProductos = tk.Spinbox(menu1,
                                               from_=1,
                                               to=100,
                                               increment=1
                                               )                                               
            spinCantidadProductos.grid(row=3, column=1, padx=10, pady=10, sticky=tk.EW)
            
            spinCantidadProductos.bind('<Return>', labelProductos)




            canvas.create_window((0, 0), window=frameInterior, anchor='nw')
            canvas.columnconfigure(0, weight=1)
            canvas.rowconfigure(0, weight=1)
            canvas.grid(row=0, column=0, sticky=tk.NSEW)
            #canvas.bind_all("<MouseWheel>", _on_mousewheel)
            scrollbar.grid(row=0, column=1, sticky="ns")

        def pedidoToTxt():

            hoy = datetime.now()
            hoyStr =f"{hoy.month}.{hoy.day}.{hoy.year % 100}"
            hoyStrPedido =f"{hoy.month}/{hoy.day}/{hoy.year % 100}"
            

            path = "pedidos/"+hoyStr+".txt"


            try:
                with open(resource_path(path), 'w') as txtPedido:
                    txtPedido.write(f'########AGENDA DEL DIA:  {hoyStr}  ########')
                    txtPedido.write("\n\n")

                    conn = sql.connect(resource_path("database\\ravello.db"))
                    c = conn.cursor()

                    c.execute("SELECT * FROM pedido WHERE fechaEntrega = ?", (hoyStrPedido,))
                    registros = c.fetchall()
                    
                    global count
                    count=0

                    for registro in registros:
                        
                        idPedido = str(registro[0])
                        infoAdicional = str(registro[4])
                        tarjeta = str(registro[5])

                        
                        c.execute("SELECT * FROM cliente WHERE idCliente = ?", (registro[2],))   
                        cliente = c.fetchone()
                        clienteNombre = cliente[1]
                        clienteTelefono = str(cliente[2])
                                                
                        c.execute("SELECT * FROM productosVendidos WHERE idPedido = ?", (registro[0],))   
                        productos = c.fetchall()

                        c.execute("SELECT * FROM productosGenericos WHERE idPedido = ?", (registro[0],))   
                        genericos = c.fetchall()

                        txtPedido.write(f"ID PEDIDO: {idPedido}\n")
        
                        txtPedido.write(f"Nombre Cliente: {clienteNombre}\n")
                        txtPedido.write(f"Telefono Cliente: {clienteTelefono}\n")
                        txtPedido.write("\n\n")
                        txtPedido.write(f"Informacion Adicional: {infoAdicional}\n")
                        txtPedido.write(f"Mensaje para la tarjeta: {tarjeta}\n")
                        txtPedido.write("\n\n")

                        for producto in productos:

                            c.execute("SELECT * FROM producto WHERE idProducto = ?", (producto[1],))   
                            productoInfo = c.fetchone()
                            

                            cantidad = str(producto[2])
                            txtPedido.write(f"{count+1}. {productoInfo[1]}\nCantidad: {cantidad}\nDescripcion: {productoInfo[2]}")
                            count+=1
                            txtPedido.write("\n\n")

                        for generico in genericos:
                            cantidad = str(generico[3])
                            txtPedido.write(f"{count+1}. {generico[1]}\nCantidad: {cantidad}")
                            count+=1
                            txtPedido.write("\n\n")
                    
            except FileNotFoundError:
                print("The 'docs' directory does not exist")

        #########################MENÚ##############################################
        contenedor = tk.Frame(master=self,
                           background=styles.BACKGROUND)
        
        contenedor.rowconfigure(2, weight=1)
        contenedor.columnconfigure(0, weight=1)
        contenedor.grid(row=0, column=0, sticky=tk.NSEW)

        
        frameMenu = tk.Frame(master=contenedor, 
                             bg=styles.LIGHT_BACKGROUND)
        frameMenu.rowconfigure(0, weight=1)
        frameMenu.grid(row=0, column=0, sticky=tk.EW)

        zonaTrabajo = tk.Frame(master=contenedor,
                               bg= styles.LIGHT_BACKGROUND)
        zonaTrabajo.rowconfigure(0, weight=1)
        zonaTrabajo.columnconfigure(0, weight=1)
        zonaTrabajo.grid(row=1, column=0, sticky=tk.EW)
        

        frameTree = tk.Frame(master=contenedor,
                             background="red")
        frameTree.rowconfigure(0, weight=1)
        frameTree.columnconfigure(0, weight=1)
        frameTree.grid(row=2, column=0, sticky=tk.EW, pady=15)
        PedidosTabla(root=frameTree, manager=self.manager).grid(row=0, column=0, sticky=tk.NSEW)


        VentaBoton = tk.Button(master=frameMenu,
                                **styles.BUTTON,
                                text=" NUEVA VENTA",
                                image=self.iconoVenta,
                                command=zonaVenta)
        VentaBoton.config(height=30, font=('Abhadi', 14))
        VentaBoton.bind("<Enter>", styles.on_enter)
        VentaBoton.bind("<Leave>", styles.on_leave)
        VentaBoton.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)


        btnPrintAgenta = tk.Button(master=frameMenu,
                                **styles.BUTTON,
                                text=" IMPRIMIR AGENDA DEL DIA",
                                image=self.iconoPrinter,
                                command=pedidoToTxt)
        btnPrintAgenta.config(height=30, font=('Abhadi', 14))
        btnPrintAgenta.bind("<Enter>", styles.on_enter)
        btnPrintAgenta.bind("<Leave>", styles.on_leave)
        btnPrintAgenta.grid(row=0, column=2, padx=10, pady=5, sticky=tk.EW)

        botonBack = tk.Button(master=frameMenu,
                                **styles.BUTTON,
                                image=self.iconoBack,
                                command=self.manager.to_home,
                                text=" VOLVER")
        botonBack.config(height=30, font=('Abhadi', 14))
        botonBack.bind("<Enter>", styles.on_enter)
        botonBack.bind("<Leave>", styles.on_leave)
        botonBack.grid(row=0, column=4, padx=10, pady=10, sticky=tk.EW)

        

        reloj()
        zonaVenta()

        

        