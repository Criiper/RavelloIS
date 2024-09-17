import sqlalchemy
import sqlalchemy.orm
from modules.models import Cliente, Producto, Pedido, ProductosVendidos, Domicilio
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

    def newCliente(self, nombre, telefono, correo, direccion, cedula):
        cliente = Cliente(nombre=nombre, telefono=telefono, pedidosHechos=0, correo=correo, direccion=direccion, cedula=cedula)
        self.session.add(cliente)
        self.session.commit()
        
    
    def newProducto(self, nombre, descripcion, valor, nivelCuidado, estimadoRosas, estimadoChocolates):

        producto = Producto(nombre=nombre, valor=valor, 
                                descripcion=descripcion, nivelCuidado=nivelCuidado,
                                estimadoChocolates=estimadoChocolates, estimadoRosas=estimadoRosas)
        self.session.add(producto)
        self.session.commit()

        


    def newPedido(self, fechaEntrega, idCliente, infoAdicionalPedido,
                  mensajeTarjeta, valorTotal,  medioPago, estado, productos, infoDomicilio):   
        cliente = self.session.query(Cliente).filter(Cliente.telefono == idCliente).first()

        if cliente == None:
            raise ProgrammingError("Cliente no se encuentra en base de datos!")
        else:
            pedido = Pedido(fechaEntrega=fechaEntrega, idCliente=cliente.idCliente, mensajeTarjeta=mensajeTarjeta,
                            infoAdicional=infoAdicionalPedido, valorTotal=valorTotal, medioPago=medioPago,
                            estado=estado, idDomicilio=0) #primero crea Venta y la agrega a db
            
            self.session.add(pedido)
            self.session.commit()

            conn = sql.connect(resource_path("database\\ravello.db"))
            c = conn.cursor()

            c.execute(f"SELECT COUNT(*) FROM pedido")
            resultado = c.fetchone()
            idPedido = int(resultado[0])

            c.close()
            conn.close()

            for i in range(len(productos)):
                #Agrega los Productos comprados (y su cantidad) referenciados al Pedido a la db
                producto = ProductosVendidos(idProducto=productos[i][0], cantidad=productos[i][1], idPedido=idPedido)
                self.session.add(producto)
                self.session.commit()

            
            pedido = self.session.query(Pedido).filter(Pedido.idPedido == idPedido).first()
            if len(infoDomicilio)>0:
                domicilio = Domicilio(idPedido=pedido.idPedido, nombreDestinatario=infoDomicilio[0], telefonoDestinatario=infoDomicilio[1],
                                    nomenclatura=infoDomicilio[2], barrio=infoDomicilio[3],
                                    municipio=infoDomicilio[4], codigoPostal=infoDomicilio[5], infoAdicional=infoDomicilio[6])
                self.session.add(domicilio)
                self.session.commit()


                domicilio = self.session.query(Domicilio).filter(Domicilio.idPedido == idPedido).first()
                pedido.idDomicilio = domicilio.idDomicilio
                self.session.commit()


            cliente.pedidosHechos +=1
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

    def delPedido(self, idPedido):
        venta = self.session.query(Pedido).filter(Pedido.idPedido == idPedido).first()

        if venta == None:
            raise ProgrammingError("Pedido no se encuentra en base de datos!")
        else:
            self.session.delete(venta)          
            self.session.commit()

    def updateCliente(self,nombres, telefono, correo, direccion, cedula):

        cliente = self.session.query(Cliente).filter(Cliente.telefono == telefono).first()

        if cliente != None:
            cliente.nombre=nombres
            cliente.telefono = telefono
            cliente.correo = correo
            cliente.direccion = direccion
            cliente.cedula  = cedula
            
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
        

