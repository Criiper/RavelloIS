import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import comm
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar
from datetime import datetime
from components.ventasTabla  import VentasTabla
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path

class VentasScreen(tk.Frame):
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
        self.iconoList = ImageTk.PhotoImage(Image.open(resource_path("assets\\list.png")))
        self.iconoDashboard = ImageTk.PhotoImage(Image.open(resource_path("assets\\dashboard.png")))

        #######FRAMES#######

        contenedor = tk.Frame(master=self,
                           background=styles.BACKGROUND)
        
        contenedor.rowconfigure(1, weight=1)
        contenedor.columnconfigure(0, weight=1)
        contenedor.grid(row=0, column=1, sticky=tk.NSEW)

        '''TablaDomicilios(contenedor,
                      self.manager
        ).grid(row=1, column=0, sticky=tk.NSEW)'''
        
        frameMesa = tk.Frame(master=contenedor,
                             background=styles.BACKGROUND)
        
        frameMesa.grid(row=0, column=0, sticky=tk.NSEW)
        frameMesa.columnconfigure(0, weight=1)
        

        frameBotones = tk.Frame(master=self,
                                 background=styles.BACKGROUND)
        
        frameBotones.grid(row=0, column=0, sticky=tk.NS)


        ################ZONAS DE TRABAJO :D ###########################
        def RegistroVentas():
            for widgets in frameMesa.winfo_children():
                widgets.destroy()

            VentasTabla(frameMesa,
                    self.manager
                            ).grid(row=1, column=0, sticky=tk.NSEW)

        def zonaDashboard():

            for widgets in frameMesa.winfo_children():
                widgets.destroy()

            

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
                return datetime.strptime(fecha, '%y-%m-%d').strftime('%Y-%m-%d')

            
            def PedidosEntreFechas():

                for widgets in frameDashboard.winfo_children():
                    widgets.destroy()

                fecha_inicio = convertir_fecha(fechaInicioVar.get())
                fecha_fin = convertir_fecha(fechaFinVar.get())
                conn = sql.connect(resource_path("database\\ravello.db"))
                cursor = conn.cursor()

                # Consulta SQL para obtener la cantidad de pedidos entre las fechas dadas
                query = '''
                SELECT fechaEntrega, COUNT(idPedido) as total_pedidos
                FROM pedido
                WHERE fechaEntrega BETWEEN ? AND ?
                GROUP BY fechaEntrega
                ORDER BY fechaEntrega;
                '''
                cursor.execute(query, (fecha_inicio, fecha_fin))
                resultados = cursor.fetchall()

                # Cerrar la conexión
                conn.close()

                # Verificar si se obtuvieron resultados
                if not resultados:
                    print("No se encontraron pedidos entre las fechas proporcionadas.")
                    return

                # Desglosar resultados
                fechas = [datetime.strptime(row[0], '%Y-%m-%d') for row in resultados]
                total_pedidos = [row[1] for row in resultados]

                            # Crear la figura y los ejes
                fig, ax = plt.subplots(figsize=(8, 5))

                # Graficar los datos
                ax.plot(fechas, total_pedidos, linestyle='solid', marker='o', color='blue')

                # Formatear el eje X para mostrar fechas correctamente
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
                ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
                fig.autofmt_xdate()

                # Etiquetas y título
                ax.set_xlabel('Fecha de Entrega')
                ax.set_ylabel('Cantidad de Pedidos')
                ax.set_title(f'Pedidos realizados entre {fecha_inicio} y {fecha_fin}')

                # Agregar cuadrícula (opcional)
                ax.grid(True)

                # Etiquetar cada punto con su fecha correspondiente
                for i, fecha in enumerate(fechas):
                    # Anotar la fecha debajo de cada punto en el eje X
                    ax.annotate(fecha.strftime('%Y-%m-%d'), xy=(fechas[i], total_pedidos[i]), 
                                xytext=(fechas[i], total_pedidos[i] - 0.5),  # Ajustar la posición de la etiqueta
                                ha='center', fontsize=8, rotation=45)

                # Identificar los días con más pedidos
                max_pedidos = max(total_pedidos)
                
                for i, total in enumerate(total_pedidos):
                    if total == max_pedidos:
                        # Colocar etiqueta solo en los días con más pedidos
                        ax.annotate(f'{total} pedidos', xy=(fechas[i], total_pedidos[i]), 
                                    xytext=(fechas[i], total_pedidos[i] + 0.5),
                                    arrowprops=dict(facecolor='black', arrowstyle='->'),
                                    ha='center')


                canvas1 = FigureCanvasTkAgg(fig, frameDashboard)
                canvas1.draw()
                canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

            def IngresosEntreFechas():
                for widgets in frameDashboard.winfo_children():
                    widgets.destroy()

                fecha_inicio = convertir_fecha(fechaInicioVar.get())
                fecha_fin = convertir_fecha(fechaFinVar.get())

                conn = sql.connect(resource_path("database\\ravello.db"))
                cursor = conn.cursor()

                # Consulta SQL para obtener los ingresos por pedidos entre las fechas dadas
                query = '''
                SELECT fechaEntrega, SUM(valorTotal) as ingresos_totales
                FROM pedido
                WHERE fechaEntrega BETWEEN ? AND ?
                GROUP BY fechaEntrega
                ORDER BY fechaEntrega;
                '''
                cursor.execute(query, (fecha_inicio, fecha_fin))
                resultados = cursor.fetchall()

                # Cerrar la conexión
                conn.close()

                # Verificar si se obtuvieron resultados
                if not resultados:
                    print("No se encontraron ingresos entre las fechas proporcionadas.")
                    return

                # Desglosar resultados
                fechas = [datetime.strptime(row[0], '%Y-%m-%d') for row in resultados]
                ingresos_totales = [row[1] for row in resultados]

                # Crear la figura y los ejes
                fig, ax = plt.subplots(figsize=(10, 6))

                # Graficar los datos
                ax.plot(fechas, ingresos_totales, linestyle='solid', marker='o', color='green')

                # Formatear el eje X
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
                ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
                fig.autofmt_xdate()

                # Etiquetas y título
                ax.set_xlabel('Fecha de Entrega')
                ax.set_ylabel('Ingresos Totales ($)')
                ax.set_title(f'Ingresos por pedidos entre {fecha_inicio} y {fecha_fin}')
                ax.grid(True)

                # Etiquetar cada punto con la fecha correspondiente
                for i, fecha in enumerate(fechas):
                    ax.annotate(fecha.strftime('%Y-%m-%d'), xy=(fechas[i], ingresos_totales[i]), 
                                xytext=(fechas[i], ingresos_totales[i] - 2),  # Ajustar la posición
                                ha='center', fontsize=8, rotation=45, 
                                bbox=dict(facecolor='white', alpha=0.7))  # Caja de texto

                # Identificar el día con los mayores ingresos y agregar anotación
                max_ingresos = max(ingresos_totales)
                for i, total in enumerate(ingresos_totales):
                    if total == max_ingresos:
                        ax.annotate(f'{total:.2f} $', xy=(fechas[i], ingresos_totales[i]), 
                                    xytext=(fechas[i], ingresos_totales[i] + 5),  # Ajustar la posición
                                    arrowprops=dict(facecolor='black', arrowstyle='->'), 
                                    bbox=dict(facecolor='yellow', alpha=0.5),  # Fondo amarillo
                                    fontsize=10)

                # Mostrar la gráfica
                canvas = FigureCanvasTkAgg(fig, frameDashboard)
                canvas.draw()
                canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

            def IngresosPorMedioPago():
                for widgets in frameDashboard.winfo_children():
                    widgets.destroy()

                conn = sql.connect(resource_path("database\\ravello.db"))
                cursor = conn.cursor()

                # Consulta SQL para obtener los ingresos totales por medio de pago
                query = '''
                SELECT medioPago, SUM(valorTotal) as ingresos_totales
                FROM pedido
                GROUP BY medioPago
                ORDER BY ingresos_totales DESC;
                '''
                cursor.execute(query)
                resultados = cursor.fetchall()

                # Cerrar la conexión
                conn.close()

                # Verificar si se obtuvieron resultados
                if not resultados:
                    print("No se encontraron ingresos registrados.")
                    return

                # Desglosar resultados
                medios_pago = [row[0] for row in resultados]
                ingresos_totales = [row[1] for row in resultados]

                # Crear la figura y los ejes
                fig, ax = plt.subplots(figsize=(10, 5))

                # Graficar los datos como un gráfico de barras
                ax.bar(medios_pago, ingresos_totales, color='skyblue')

                # Etiquetas y título
                ax.set_xlabel('Medio de Pago')
                ax.set_ylabel('Ingresos Totales ($)')
                ax.set_title('Ingresos registrados por Medio de Pago')
                ax.set_xticklabels(medios_pago, rotation=0, ha='right')  # Rotar etiquetas del eje X

                # Añadir etiquetas a las barras
                for i, total in enumerate(ingresos_totales):
                    ax.text(i, total, f'{total:.2f}', ha='center', va='bottom', fontsize=10)  # Etiqueta sobre cada barra

                # Añadir cuadrícula
                ax.yaxis.grid(True, linestyle='--', alpha=0.7)  # Cuadrícula horizontal

                # Ajustar límites del eje Y para mejorar la visualización
                ax.set_ylim(0, max(ingresos_totales) * 1.1)  # Un poco más alto que el máximo para el espacio

                # Mostrar la gráfica
                canvas = FigureCanvasTkAgg(fig, frameDashboard)
                canvas.draw()
                canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

            def ProductosMasVendidos():
                for widgets in frameDashboard.winfo_children():
                    widgets.destroy()

                fecha_inicio = convertir_fecha(fechaInicioVar.get())
                fecha_fin = convertir_fecha(fechaFinVar.get())

                conn = sql.connect(resource_path("database\\ravello.db"))
                cursor = conn.cursor()

                # Consulta SQL para obtener los productos más vendidos entre las fechas dadas
                query = '''
                        SELECT producto.nombre, SUM(productosVendidos.cantidad) AS total_vendido
                        FROM productosVendidos
                        JOIN pedido ON productosVendidos.idPedido = pedido.idPedido
                        JOIN producto ON productosVendidos.idProducto = producto.idProducto
                        WHERE pedido.fechaEntrega BETWEEN ? AND ?
                        GROUP BY productosVendidos.idProducto
                        ORDER BY total_vendido DESC
                        LIMIT 10;
                        '''

                cursor.execute(query, (fecha_inicio, fecha_fin))
                resultados = cursor.fetchall()

                # Cerrar la conexión
                conn.close()

                # Verificar si se obtuvieron resultados
                if not resultados:
                    print("No se encontraron productos vendidos entre las fechas proporcionadas.")
                    return

                # Desglosar resultados
                nombres_productos = [row[0] for row in resultados]
                cantidades_vendidas = [row[1] for row in resultados]

                # Crear la figura y los ejes
                fig, ax = plt.subplots(figsize=(8, 6))
                
                # Graficar los datos como un gráfico de barras
                ax.barh(nombres_productos, cantidades_vendidas, color='skyblue')

                # Etiquetas y título
                ax.set_xlabel('Cantidad Vendida')
                ax.set_ylabel('Producto')
                ax.set_title(f'10 Productos más vendidos entre {fecha_inicio} y {fecha_fin}')

                # Añadir etiquetas a las barras
                for i, cantidad in enumerate(cantidades_vendidas):
                    ax.text(cantidad, i, str(cantidad), ha='left', va='center', fontsize=10)  # Etiqueta al final de cada barra

                # Añadir cuadrícula
                ax.xaxis.grid(True, linestyle='--', alpha=0.7)  # Cuadrícula horizontal

                # Ajustar límites del eje X para mejorar la visualización
                ax.set_xlim(0, max(cantidades_vendidas) * 1.1)  # Un poco más alto que el máximo para el espacio

                # Mostrar la gráfica
                plt.tight_layout() 

                canvas = FigureCanvasTkAgg(fig, frameDashboard)
                canvas.draw()
                canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

            def ProductosMenosVendidos():
                for widgets in frameDashboard.winfo_children():
                    widgets.destroy()

                fecha_inicio = convertir_fecha(fechaInicioVar.get())
                fecha_fin = convertir_fecha(fechaFinVar.get())

                # Conectar a la base de datos
                conn = sql.connect(resource_path("database\\ravello.db"))
                cursor = conn.cursor()

                # Consulta SQL para obtener los 10 productos menos vendidos
                query = '''
                SELECT producto.nombre, SUM(productosVendidos.cantidad) AS total_vendido
                FROM productosVendidos
                JOIN pedido ON productosVendidos.idPedido = pedido.idPedido
                JOIN producto ON productosVendidos.idProducto = producto.idProducto
                WHERE pedido.fechaEntrega BETWEEN ? AND ?
                GROUP BY productosVendidos.idProducto
                ORDER BY total_vendido ASC
                LIMIT 10;
                '''
                
                # Ejecutar la consulta con parámetros
                cursor.execute(query, (fecha_inicio, fecha_fin))
                resultados = cursor.fetchall()

                # Cerrar la conexión
                conn.close()

                # Verificar si hay resultados
                if resultados:
                    productos = [fila[0] for fila in resultados]  # Nombres de los productos
                    cantidades = [fila[1] for fila in resultados]  # Total vendido por cada producto

                    # Crear la gráfica
                    fig, ax = plt.subplots(figsize=(10, 6))
                    ax.barh(productos, cantidades, color='lightblue')
                    ax.set_xlabel('Cantidad Vendida')
                    ax.set_ylabel('Productos')
                    ax.set_title('10 Productos Menos Vendidos')
                    ax.invert_yaxis()  # Invertir el eje Y para mostrar el producto menos vendido en la parte superior

                    # Anotaciones para mejorar la legibilidad
                    for index, value in enumerate(cantidades):
                        ax.text(value, index, str(value))  # Añadir el valor encima de cada barra

                    fig.tight_layout()  # Ajustar el layout
                    
                    canvas = FigureCanvasTkAgg(fig, frameDashboard)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

        



            #######FRAMES#########
            frameCalendar = tk.Frame(master=frameMesa,
                                 background=styles.LIGHT_BACKGROUND)
            frameCalendar.pack(side="top", expand=True, fill="x")

            frameMenu = tk.Frame(master=frameMesa,
                                 background=styles.LIGHT_BACKGROUND)
            frameMenu.pack(side="top", expand=True, fill="x")

            frameDashboard = tk.Frame(master=frameMesa,
                                      background=styles.BACKGROUND)
            frameDashboard.pack(side="top", expand=True, fill="both")



            #######CALENDARIOS#####

            labelFechaInicio = tk.Label(master=frameCalendar,
                            **styles.LABEL,
                            text="Fecha de Inicio")
            labelFechaInicio.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NSEW)

            fechaInicioVar = tk.StringVar()
            fechaInicioVar.set("mm/dd/yy")
            entryFechaInicio = tk.Entry(frameCalendar,
                                state="readonly",
                                textvariable=fechaInicioVar,
                                font=('Abhadi', 14)
                                )
            entryFechaInicio.bind('<ButtonRelease-1>', lambda event: calendario(fechaInicioVar))
            entryFechaInicio.grid(row=1, column=0, sticky=tk.EW, padx=5, pady=2)


            labelFechaFin = tk.Label(master=frameCalendar,
                            **styles.LABEL,
                            text="Fecha de Cierre")
            labelFechaFin.grid(column=1, row=0, padx=5, pady=5, sticky=tk.NSEW)

            fechaFinVar = tk.StringVar()
            fechaFinVar.set("mm/dd/yy")
            entryFechaFin = tk.Entry(frameCalendar,
                                state="readonly",
                                textvariable=fechaFinVar,
                                font=('Abhadi', 14)
                                )
            entryFechaFin.bind('<ButtonRelease-1>', lambda event: calendario(fechaFinVar))
            entryFechaFin.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)




            #######BOTONES#######
            btnPedidosTiempo = tk.Button(master=frameMenu,
                                         text="Relación Pedidos-Tiempo",
                                         **styles.BUTTON,
                                         command=PedidosEntreFechas
                                         )
            btnPedidosTiempo.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnPedidosTiempo.pack(side="left", padx=5, pady=5, expand=True)
            btnPedidosTiempo.bind('<Enter>', styles.on_enter)
            btnPedidosTiempo.bind('<Leave>', styles.on_leave)


            btnIngresosTiempo = tk.Button(master=frameMenu,
                                         text="Relación Ingresos-Tiempo",
                                         **styles.BUTTON,
                                         command=IngresosEntreFechas
                                         )
            btnIngresosTiempo.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnIngresosTiempo.pack(side="left", padx=5, pady=5, expand=True)
            btnIngresosTiempo.bind('<Enter>', styles.on_enter)
            btnIngresosTiempo.bind('<Leave>', styles.on_leave)


            btnIngresosMedio = tk.Button(master=frameMenu,
                                         text="Relación Ingresos por MedioPago",
                                         **styles.BUTTON,
                                         command=IngresosPorMedioPago
                                         )
            btnIngresosMedio.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnIngresosMedio.pack(side="left", padx=5, pady=5, expand=True)
            btnIngresosMedio.bind('<Enter>', styles.on_enter)
            btnIngresosMedio.bind('<Leave>', styles.on_leave)

            
            btnProductosMas = tk.Button(master=frameMenu,
                                         text="Productos Mas Vendidos",
                                         **styles.BUTTON,
                                         command=ProductosMasVendidos
                                         )
            btnProductosMas.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnProductosMas.pack(side="left", padx=5, pady=5, expand=True)
            btnProductosMas.bind('<Enter>', styles.on_enter)
            btnProductosMas.bind('<Leave>', styles.on_leave)


            btnProductosMenos = tk.Button(master=frameMenu,
                                         text="Productos Menos Vendidos",
                                         **styles.BUTTON,
                                         command=ProductosMenosVendidos
                                         )
            btnProductosMenos.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnProductosMenos.pack(side="left", padx=5, pady=5, expand=True)
            btnProductosMenos.bind('<Enter>', styles.on_enter)
            btnProductosMenos.bind('<Leave>', styles.on_leave)

        ##########BOTONES########################

        botonDashboard = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" DASHBOARD",
                                image=self.iconoDashboard,
                                command=zonaDashboard
                                )
        botonDashboard.pack(padx=10, pady=5, fill="both", expand=True)
        botonDashboard.config(font=("Abhadi", 14), wraplength=250)
        botonDashboard.bind('<Enter>', styles.on_enter)
        botonDashboard.bind('<Leave>', styles.on_leave)

        botonRegistro = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" REGISTRO DE VENTAS",
                                image=self.iconoList,
                                command=RegistroVentas)
        botonRegistro.pack(padx=10, pady=5, fill="both", expand=True)
        botonRegistro.config(font=("Abhadi", 14), wraplength=250)
        botonRegistro.bind('<Enter>', styles.on_enter)
        botonRegistro.bind('<Leave>', styles.on_leave)


        botonBack = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" VOLVER",
                                image=self.iconoBack,
                                command=self.manager.to_home)
        botonBack.pack(padx=10, pady=5, fill="both", expand=True)
        botonBack.config(font=("Abhadi", 14), wraplength=250)
        botonBack.bind('<Enter>', styles.on_enter)
        botonBack.bind('<Leave>', styles.on_leave)

        RegistroVentas()