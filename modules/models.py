
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean


Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"
    idCliente = Column(Integer, primary_key=True)
    nombre = Column(String(40))
    telefono = Column(Integer)
    pedidosHechos = Column(Integer)


class Producto(Base):
    __tablename__ = "producto"
    idProducto = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(500))
    valor = Column(Float)
    nivelCuidado = Column(Integer)
    estimadoRosas = Column(Integer)
    estimadoChocolates = Column(Integer)
#Una Venta se relaciona con los Productos por medio de la tabla enlace ProductosComprados

class Domicilio(Base):
    __tablename__ = "domicilio"
    idDomicilio = Column(Integer, primary_key=True)
    nombreDestinatario = Column(String(50))
    telefonoDestinatario = Column(Integer)
    nomenclatura = Column(String(100))
    barrio = Column(String(50))
    municipio = Column(String(50))
    codigoPostal = Column(Integer)
    infoAdicional = Column(String(500))
    idPedido = Column(Integer, ForeignKey("pedido.idPedido"))
    pedido = relationship("Pedido", back_populates="domicilio", foreign_keys=[idPedido])

class Pedido(Base):
    __tablename__ = "pedido"
    idPedido = Column(Integer, primary_key=True)
    fechaEntrega = Column(String)
    idCliente = Column(Integer, ForeignKey("cliente.idCliente"))
    cliente = relationship("Cliente")
    idDomicilio = Column(Integer, ForeignKey("domicilio.idDomicilio"))
    domicilio = relationship("Domicilio", back_populates="pedido", foreign_keys=[Domicilio.idPedido])
    infoAdicional = Column(String(500))
    mensajeTarjeta = Column(String(1000))
    valorTotal = Column(Integer)
    medioPago = Column(String(40))
    estado = Column(String(40))
    

class ProductosVendidos(Base):
    __tablename__ = "productosVendidos"
    id = Column(Integer, primary_key=True)
    idProducto = Column(Integer, ForeignKey("producto.idProducto"))
    cantidad = Column(Integer)
    idPedido = Column(Integer, ForeignKey("pedido.idPedido"))
    producto = relationship("Producto")
    pedido = relationship("Pedido")


class ProductosGenericos(Base):
    __tablename__ = "productosGenericos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    precio = Column(Integer)
    cantidad = Column(Integer)
    idPedido = Column(Integer, ForeignKey("pedido.idPedido"))
    Pedido = relationship("Pedido")


if __name__ == "__main__":
    engine = create_engine('sqlite:///database\\ravello.db', echo=True)
    Base.metadata.create_all(engine)
