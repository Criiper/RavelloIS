import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path

class TablaClientes(tk.Frame):
    def __init__(self, root, manager):
        super().__init__(master=root, background=styles.LIGHT_BACKGROUND)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.manager = manager
        self.initWidgets()

    def initWidgets(self):
        
        #######IMAGENES#######
        
        self.iconoReload = ImageTk.PhotoImage(Image.open(resource_path('assets\\iconoReload25px.png')))

        #######FUNCIONES######
        def fetchProductosDB():
            treeTabla.delete(*treeTabla.get_children())
            conn = sql.connect(resource_path("database\\ravello.db"))
            c = conn.cursor()

            c.execute("SELECT * FROM cliente")
            registros = c.fetchall()

            global count
            count=0

            for registro in registros:
                if count % 2 == 0:
                    treeTabla.insert(parent="", index=0, iid=count, values=(registro[6], registro[1], registro[2], registro[4], registro[5], registro[3]), tags="evenrow")
                else:
                    treeTabla.insert(parent="", index=0, iid=count, values=(registro[6], registro[1], registro[2], registro[4], registro[5], registro[3]), tags="oddrow")    
                count+=1


            c.execute(f"SELECT COUNT(*) FROM cliente")
            resultado = c.fetchone()
            ContProductos = int(resultado[0])

            labelContVar.set(f"Se han registrado {ContProductos} clientes")
            
            conn.commit()
            conn.close()

        def Filtro():

            busqueda = entryBusqueda.get()
            conn = sql.Connection(resource_path("database\\ravello.db"))
            c = conn.cursor()
            c.execute("SELECT * FROM cliente")
            registros = c.fetchall()
            
            global count
            count = 0

            treeTabla.delete(*treeTabla.get_children())

            # Filtrar elementos de la tabla según el texto de búsqueda
            for registro in registros:
                if busqueda in str(registro[2]):  # Comprobar si el texto de búsqueda está en el elemento
                    if count % 2 == 0:
                        treeTabla.insert(parent="", index=0, iid=count, values=( registro[6], registro[1], registro[2], registro[4], registro[5], registro[3]), tags="evenrow")
                    else:
                        treeTabla.insert(parent="", index=0, iid=count, values=( registro[6], registro[1], registro[2], registro[4], registro[5], registro[3]), tags="oddrow")    
                    count+=1
            
            

        ######FRAMES#######
        
        frameBusqueda = tk.Frame(master=self,
                                    background=styles.LIGHT_BACKGROUND,
                                    height=5)
        frameBusqueda.rowconfigure(0, weight=1)
        frameBusqueda.columnconfigure(3, weight=1)
        frameBusqueda.grid(row=0, column=0, sticky=tk.NSEW)

        botonReload = tk.Button(master=frameBusqueda,
                                text="ACTUALIZAR",
                                **styles.BUTTON,
                                image=self.iconoReload,
                                command=fetchProductosDB
                            )
        botonReload.bind('<Enter>', styles.on_enter)
        botonReload.bind('<Leave>', styles.on_leave)
        
        botonReload.config(height=30)
        botonReload.grid(row=0, column=0, padx=10, pady=5)

        labelBusqueda = tk.Label(frameBusqueda,
                                    text="Busca por Télefono",
                                    **styles.LABEL)
        labelBusqueda.grid(row=0, column=1, padx=10, pady=5)

        entryBusqueda = tk.Entry(master=frameBusqueda,
                                    font=('Abhadi', 12))
        entryBusqueda.grid(row=0, column=2, padx=5, pady=5)
        entryBusqueda.bind('<KeyRelease>', lambda event: Filtro())

        labelContVar = tk.StringVar()
        labelCont = tk.Label(frameBusqueda,
                                    textvariable=labelContVar,
                                    **styles.LABEL)
        labelCont.grid(row=0, column=3, padx=10, pady=5)

        frameTree = tk.Frame(master=self,
                            background=styles.LIGHT_BACKGROUND)
        frameTree.grid(row=1, column=0, sticky=tk.NSEW)
    

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

        treeBarra = tk.Scrollbar(frameTree)
        treeBarra.pack(side="right", fill="y")

        treeTabla = ttk.Treeview(frameTree, yscrollcommand=treeBarra.set, selectmode="extended")

        treeBarra.config(command=treeTabla.yview)

        treeTabla['columns'] = ("ID", "Nombres", "Telefono", "Correo", "Direccion", "Pedidos Realizados")

        treeTabla.column("#0", width=0, stretch=False)
        treeTabla.column("ID", width=60, minwidth=20, anchor="center")
        treeTabla.column("Nombres", width=90, minwidth=80, anchor="e")
        treeTabla.column("Telefono", width=40, minwidth=20, anchor="center")
        treeTabla.column("Correo", width=90, minwidth=80, anchor="e")
        treeTabla.column("Direccion", width=90, minwidth=80, anchor="e")
        treeTabla.column("Pedidos Realizados", width=20, minwidth=20, anchor="center")
        
        

        treeTabla.heading("ID", text="Documento de Identificacion", anchor="center")
        treeTabla.heading("Nombres", text="Nombre ", anchor="e")
        treeTabla.heading("Telefono", text="Teléfono", anchor="center")
        treeTabla.heading("Correo", text="Correo", anchor="e")
        treeTabla.heading("Direccion", text="Direccion ", anchor="e")
        treeTabla.heading("Pedidos Realizados", text="N°Pedidos", anchor="center")
        
        

        treeTabla.tag_configure("oddrow", background="WHITE")
        treeTabla.tag_configure("evenrow", background=styles.HIGHLIGHT)

        fetchProductosDB()
        treeTabla.pack(fill="both", expand=True)
