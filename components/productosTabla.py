import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path

class TablaProductos(tk.Frame):
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

                c.execute("SELECT * FROM producto")
                registros = c.fetchall()

                global count
                count=0

                for registro in registros:
                    if count % 2 == 0:
                        treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], registro[3], registro[2], registro[5], registro[6], registro[4]), tags="evenrow")
                    else:
                        treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], registro[3], registro[2], registro[5], registro[6], registro[4]), tags="oddrow")    
                    count+=1


                c.execute(f"SELECT COUNT(*) FROM producto")
                resultado = c.fetchone()
                ContProductos = int(resultado[0])

                labelContVar.set(f"Se han registrado {ContProductos} productos")

                conn.commit()
                conn.close()

            def Filtro():

                busqueda = entryBusqueda.get()
                conn = sql.Connection(resource_path("database\\ravello.db"))
                c = conn.cursor()
                c.execute("SELECT * FROM producto")
                registros = c.fetchall()
                
                global count
                count = 0

                treeTabla.delete(*treeTabla.get_children())

                # Filtrar elementos de la tabla según el texto de búsqueda
                for registro in registros:
                    if busqueda in str(registro[0]):  # Comprobar si el texto de búsqueda está en el elemento
                        if count % 2 == 0:
                            treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]), tags="evenrow")
                        else:
                            treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]), tags="oddrow")    
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
                                     text="Busca por ID",
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

            treeTabla['columns'] = ("ID", "Nombre", "Valor", "Descripcion", "EstimadoRosas", "EstimadoChocolates", "NivelCuidado")

            treeTabla.column("#0", width=0, stretch=False)
            treeTabla.column("ID", width=20, minwidth=20, anchor="center")
            treeTabla.column("Nombre", width=100, minwidth=60, anchor="e")
            treeTabla.column("Valor", width=40, minwidth=20, anchor="center")
            treeTabla.column("Descripcion", width=180, minwidth=100, anchor="e")
            treeTabla.column("EstimadoRosas", width=20, minwidth=20, anchor="center")
            treeTabla.column("EstimadoChocolates", width=30, minwidth=20, anchor="center")
            treeTabla.column("NivelCuidado", width=80, minwidth=80, anchor="center")


            treeTabla.heading("ID", text="ID", anchor="center")
            treeTabla.heading("Nombre", text="Nombre ", anchor="e")
            treeTabla.heading("Valor", text="Valor", anchor="center")
            treeTabla.heading("Descripcion", text="Descripcion", anchor="e")
            treeTabla.heading("EstimadoRosas", text="Rosas*", anchor="center")
            treeTabla.heading("EstimadoChocolates", text="Chocolates*", anchor="center")
            treeTabla.heading("NivelCuidado", text="Nivel de Cuidado* ", anchor="center")

            treeTabla.tag_configure("oddrow", background="WHITE")
            treeTabla.tag_configure("evenrow", background=styles.HIGHLIGHT)

            fetchProductosDB()
            treeTabla.pack(fill="both", expand=True)

        

            


