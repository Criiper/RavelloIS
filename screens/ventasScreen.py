import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from tkcalendar import Calendar
from datetime import datetime
from components.domiciliosTabla import TablaDomicilios
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

        def zonaDashboard():

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

            def plotPedidosTiempo():
                fechaInicio = fechaInicioVar.get()
                fechaFin = fechaFinVar.get()
                

                fechaInicio = convertir_fecha(fechaInicio)
                fechaFin = convertir_fecha(fechaFin)
                

                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                consulta = """SELECT * FROM pedido WHERE fechaEntrega BETWEEN ? AND ?"""
                                
                c.execute(consulta, (fechaInicio, fechaFin))
                registros = c.fetchall()
                print(registros)
            

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
                                         command=plotPedidosTiempo
                                         )
            btnPedidosTiempo.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnPedidosTiempo.pack(side="left", padx=5, pady=5, expand=True)
            btnPedidosTiempo.bind('<Enter>', styles.on_enter)
            btnPedidosTiempo.bind('<Leave>', styles.on_leave)


            btnIngresosTiempo = tk.Button(master=frameMenu,
                                         text="Relación Ingresos-Tiempo",
                                         **styles.BUTTON
                                         )
            btnIngresosTiempo.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnIngresosTiempo.pack(side="left", padx=5, pady=5, expand=True)
            btnIngresosTiempo.bind('<Enter>', styles.on_enter)
            btnIngresosTiempo.bind('<Leave>', styles.on_leave)


            btnIngresosMedio = tk.Button(master=frameMenu,
                                         text="Relación Ingresos por MedioPago",
                                         **styles.BUTTON
                                         )
            btnIngresosMedio.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnIngresosMedio.pack(side="left", padx=5, pady=5, expand=True)
            btnIngresosMedio.bind('<Enter>', styles.on_enter)
            btnIngresosMedio.bind('<Leave>', styles.on_leave)

            
            btnProductosMas = tk.Button(master=frameMenu,
                                         text="Productos Mas Vendidos",
                                         **styles.BUTTON
                                         )
            btnProductosMas.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnProductosMas.pack(side="left", padx=5, pady=5, expand=True)
            btnProductosMas.bind('<Enter>', styles.on_enter)
            btnProductosMas.bind('<Leave>', styles.on_leave)


            btnProductosMenos = tk.Button(master=frameMenu,
                                         text="Productos Menos Vendidos",
                                         **styles.BUTTON
                                         )
            btnProductosMenos.config(font=('Abhadi', 11), wraplength=150, width=18, height=2)
            btnProductosMenos.pack(side="left", padx=5, pady=5, expand=True)
            btnProductosMenos.bind('<Enter>', styles.on_enter)
            btnProductosMenos.bind('<Leave>', styles.on_leave)

        ##########BOTONES########################

        botonDashboard = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" DASHBOARD",
                                image=self.iconoNuevo,
                                command=zonaDashboard
                                )
        botonDashboard.pack(padx=10, pady=5, fill="both", expand=True)
        botonDashboard.config(font=("Abhadi", 14), wraplength=250)
        botonDashboard.bind('<Enter>', styles.on_enter)
        botonDashboard.bind('<Leave>', styles.on_leave)

        botonRegistro = tk.Button(master=frameBotones,
                                **styles.BUTTON,
                                text=" REGISTRO DE VENTAS",
                                image=self.iconoEditar,)
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