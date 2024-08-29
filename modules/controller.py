import sqlalchemy
import sqlalchemy.orm
from modules.models import Cliente, Producto, Pedido, ProductosVendidos, Domicilio, ProductosGenericos
from sqlite3 import ProgrammingError
import sqlite3 as sql
import os
import sys


#########ESTE METODO ES JESUCRISTO PARA EL EJECUTABLE####
#En resumen crea una ruta relativa para poder cargar desde las imagenes hasta los modulos de la base de datos.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Controller:
    def __init__(self) -> None:
        db_path = resource_path('database/ravello.db')
        db_uri = f'sqlite:///{db_path}'
        engine = sqlalchemy.create_engine(db_uri, echo=True)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = Session()
        #Crea un motor y una sesion para trabajar con la db. El echo imprime que hace

    def newCliente(self, nombre, telefono):
        cliente = Cliente(nombre=nombre, telefono=telefono, pedidosHechos=0)
        self.session.add(cliente)
        self.session.commit()
        
    
    def newProducto(self, nombre, descripcion, valor, nivelCuidado, estimadoRosas, estimadoChocolates):

        producto = Producto(nombre=nombre, valor=valor, 
                                descripcion=descripcion, nivelCuidado=nivelCuidado,
                                estimadoChocolates=estimadoChocolates, estimadoRosas=estimadoRosas)
        self.session.add(producto)
        self.session.commit()

        


    def newPedido(self, fechaEntrega, idCliente, infoAdicionalPedido,
                  mensajeTarjeta, valorTotal,  medioPago, estadoPago,
                  estadoEntrega, productos, genericos,
                  infoDomicilio):   
        verificacion = self.session.query(Cliente).filter(Cliente.idCliente == idCliente).first()

        if verificacion == None:
            raise ProgrammingError("Cliente no se encuentra en base de datos!")
        else:
            pedido = Pedido(fechaEntrega=fechaEntrega, idCliente=idCliente, mensajeTarjeta=mensajeTarjeta,
                            infoAdicional=infoAdicionalPedido, valorTotal=valorTotal, medioPago=medioPago,
                            estadoEntrega=estadoEntrega, estadoPago=estadoPago) #primero crea Venta y la agrega a db
            
            self.session.add(pedido)
            self.session.commit()

            conn = sql.connect(resource_path("database\\ravello.db"))
            c = conn.cursor()

            c.execute(f"SELECT COUNT(*) FROM pedido")
            resultado = c.fetchone()
            idventa = int(resultado[0])

            c.close()
            conn.close()

            for i in range(len(productos)):
                #Agrega los Productos comprados (y su cantidad) referenciados al Pedido a la db
                producto = ProductosVendidos(idProducto=productos[i][0], cantidad=productos[i][1], idVenta=idventa)
                self.session.add(producto)
                self.session.commit()

            for i in range(len(genericos)):
                #Agrega los Productos comprados (y su cantidad) referenciados al Pedido a la db
                producto = ProductosGenericos(nombre=genericos[i][0], cantidad=genericos[i][1], precio=genericos[i][2], idVenta=idventa)
                self.session.add(producto)
                self.session.commit()

            domicilio = Domicilio(nombreDestinatario=infoDomicilio[0], telefonoDestinatario=infoDomicilio[1],
                                  nomenclatura=infoDomicilio[2], barrio=infoDomicilio[3],
                                  municipio=infoDomicilio[4], codigoPostal=infoDomicilio[5], infoAdicional=infoDomicilio[6])
            self.session.add(domicilio)
            self.session.commit()

    def delDomicilio(self, idPedido):
        domicilio = self.session.query(Domicilio).filter(Domicilio.idPedido == idPedido).first()

        if domicilio == None:
            raise ProgrammingError("Producto no se encuentra en base de datos!")
        else:
            self.session.delete(domicilio)
            self.session.commit()    

    def updatePedido(self,  idPedido, fechaEntrega, mensajeTarjeta, infoAdicional, estadoEntrega, estadoPago, infoDomicilio):
        pedido = self.session.query(Pedido).filter(Pedido.idPedido == idPedido).first()

        if pedido != None:
            pedido.fechaEntrega=fechaEntrega
            pedido.mensajeTarjeta=mensajeTarjeta
            pedido.infoAdicional=infoAdicional
            pedido.estadoEntrega=estadoEntrega
            pedido.estadoPago=estadoPago

            
            self.session.commit()
        
            domicilio = self.session.query(Domicilio).filter(Domicilio.idPedido == idPedido).first()

            if domicilio != None:
                domicilio.nombreDestinatario = infoDomicilio[0]
                domicilio.telefonoDestinatario = infoDomicilio[1]
                domicilio.nomenclatura = infoDomicilio[2]
                domicilio.barrio = infoDomicilio[3]
                domicilio.municipio = infoDomicilio[4]
                domicilio.codigoPostal = infoDomicilio[5]
                domicilio.infoAdicional = infoDomicilio[6]

            else:
                raise ProgrammingError("Domicilio no se encuentra en base de datos!")
            
        else:
            raise ProgrammingError("Pedido no se encuentra en base de datos!")


    def delCliente(self, telefonoCliente):
        cliente = self.session.query(Cliente).filter(Cliente.telefono == telefonoCliente).first()

        if cliente == None:
            raise ProgrammingError("Cliente no se encuentra en base de datos!")
        else:
            self.session.delete(cliente)
            self.session.commit()
    
    def delProducto(self, idProducto):
        producto = self.session.query(Producto).filter(Producto.idProducto == idProducto).first()

        if producto == None:
            raise ProgrammingError("Producto no se encuentra en base de datos!")
        else:
            self.session.delete(producto)
            self.session.commit()

    def delVenta(self, idPedido):
        venta = self.session.query(Pedido).filter(Pedido.idPedido == idPedido).first()

        if venta == None:
            raise ProgrammingError("Pedido no se encuentra en base de datos!")
        else:
            self.session.delete(venta)          


    def updateCliente(self,nombres, telefono):

        cliente = self.session.query(Cliente).filter(Cliente.telefono == telefono).first()

        if cliente != None:
            cliente.nombre=nombres
            cliente.telefono = telefono
            
            self.session.commit()
        
        else:
            raise ProgrammingError("Cliente no se encuentra en base de datos!")
        
    
    def updateProducto(self, identificacion, newNombre, newValor, newNivelCuidado, newEstimadoRosas, newEstimadoChocolates, newDescripcion):

        producto = self.session.query(Producto).filter(Producto.idProducto == identificacion).first()

        if producto != None:  #las claves primarias no deben de ser modificadas (idProducto)
                producto.nombre= newNombre
                producto.valor = newValor 
                producto.estimado_chocolates = newEstimadoChocolates
                producto.estimado_rosas = newEstimadoRosas
                producto.descripcion = newDescripcion
                producto.nivelCuidado = newNivelCuidado

                self.session.commit()
        else:
            raise ProgrammingError("Producto no se encuentra en base de datos!")
        

