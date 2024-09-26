import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from PIL import Image, ImageTk
from style import styles
from modules.controller import Controller
from modules.controller import resource_path

class TablaDomicilios(tk.Frame):
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

                c.execute("SELECT * FROM domicilio")
                registros = c.fetchall()

                global count
                count=0

                for registro in registros:

                    c.execute("SELECT * FROM pedido WHERE idDomicilio = ?", (registro[0],)) 
                    pedido = c.fetchone()

                    if count % 2 == 0:
                        treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[8], registro[3], registro[4], registro[6], pedido[1], registro[9]), tags="evenrow")
                    else:
                        treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[8], registro[3], registro[4], registro[6], pedido[1], registro[9]), tags="oddrow")    
                    count+=1


                conn.commit()
                conn.close()


            def Filtro():               
                
                busqueda = entryFiltro.get()
                treeTabla.delete(*treeTabla.get_children())
                conn = sql.connect(resource_path("database\\ravello.db"))
                c = conn.cursor()

                c.execute("SELECT * FROM domicilio")
                registros = c.fetchall()

            

                global count
                count = 0

                
                treeTabla.delete(*treeTabla.get_children())

                # Filtrar elementos de la tabla según el texto de búsqueda
                for registro in registros:
                    if busqueda in str(registro[0]): 
                        # Comprobar si el texto de búsqueda está en el elemento

                        c.execute("SELECT * FROM pedido WHERE idDomicilio = ?", (registro[0],)) 
                        pedido = c.fetchone()

                        
                        if count % 2 == 0:
                            treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[8], registro[3], registro[4], registro[6], pedido[1], registro[9]), tags="evenrow")
                        else:
                            treeTabla.insert(parent="", index=0, iid=count, values=( registro[0], registro[8], registro[3], registro[4], registro[6], pedido[1], registro[9]), tags="oddrow")    
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
            botonReload.grid(row=0, column=2, padx=10, pady=5)

            
            entryFiltro = tk.Entry(frameBusqueda,
                                font=('Abhadi', 12))
            entryFiltro.bind('<KeyRelease>', lambda event: Filtro())
            entryFiltro.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)


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

            treeTabla['columns'] = ("idDomicilio", "idPedido", "Direccion", "Barrio", "Postal", "Fecha", "Zona")

            treeTabla.column("#0", width=0, stretch=False)
            treeTabla.column("idDomicilio", width=20, minwidth=20, anchor="center")
            treeTabla.column("idPedido", width=100, minwidth=60, anchor="center")
            treeTabla.column("Direccion", width=180, minwidth=100, anchor="w")
            treeTabla.column("Barrio", width=40, minwidth=20, anchor="e")
            treeTabla.column("Postal", width=20, minwidth=20, anchor="center")
            treeTabla.column("Fecha", width=30, minwidth=20, anchor="center")
            treeTabla.column("Zona", width=80, minwidth=80, anchor="e")


            treeTabla.heading("idDomicilio", text="ID Domicilio", anchor="center")
            treeTabla.heading("idPedido", text="ID Pedido ", anchor="center")
            treeTabla.heading("Direccion", text="Dirección", anchor="center")
            treeTabla.heading("Barrio", text="Barrio", anchor="e")
            treeTabla.heading("Postal", text="C. Postal", anchor="center")
            treeTabla.heading("Fecha", text="Fecha Entrega", anchor="center")
            treeTabla.heading("Zona", text="Zona de Ruta", anchor="e")

            treeTabla.tag_configure("oddrow", background="WHITE")
            treeTabla.tag_configure("evenrow", background=styles.HIGHLIGHT)

            fetchProductosDB()
            treeTabla.pack(fill="both", expand=True)

        

            


