from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from modules.models import Cliente, Producto, Pedido, ProductosVendidos, Domicilio
from modules.controller import Controller
from datetime import  date


if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///database\\ravello.db"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
      

    controlador = Controller()
    controlador.newCliente("Cristian Perez", 3207976410, "crperezlo@unal.edu.co", "Entrerrios", 1035494008)
    controlador.newCliente("Juan Perez", 3133086122, "juan@yopmail.com", "Guayabal", 1002154778)
    controlador.newCliente("Juan Perez", 3133086122, "juan@gmail.com", "Guayabal", 1002154778)
    controlador.newCliente("Maria Gomez", 3223457890, "maria@hotmail.com", "El Poblado", 1003154879)
    controlador.newCliente("Carlos Ruiz", 3015671234, "carlos@yahoo.com", "Laureles", 1004165970)
    controlador.newCliente("Ana Morales", 3047895678, "ana@outlook.com", "Belen", 1005176071)
    controlador.newCliente("Luis Torres", 3112345678, "luis@live.com", "Robledo", 1006187172)
    controlador.newCliente("Carmen Diaz", 3206789123, "carmen@mail.com", "Envigado", 1007198273)
    controlador.newCliente("Jose Muñoz", 3145678901, "jose@protonmail.com", "Sabaneta", 1008209374)
    controlador.newCliente("Laura Rodriguez", 3198765432, "laura@icloud.com", "Itagui", 1009210475)
    controlador.newCliente("Pedro Sanchez", 3176543210, "pedro@yopmail.com", "Calasanz", 1010221576)
    controlador.newCliente("Sofia Castillo", 3187654321, "sofia@gmx.com", "San Javier", 1011232677)

    controlador.newProducto("Caja de Rosas Pequena", "Caja con rosas de cualquier color", 105000, 4, 16, 0)
    controlador.newProducto("Caja de Rosas Roja", "Caja elegante con rosas rojas", 120000, 5, 12, 0)
    controlador.newProducto("Bouquet de Flores Mixto", "Bouquet con variedad de flores", 85000, 3, 20, 0)
    controlador.newProducto("Caja de Rosas y Chocolates", "Caja con rosas rosadas y chocolates finos", 150000, 4, 10, 8)
    controlador.newProducto("Arreglo de Rosas Blancas", "Arreglo con rosas blancas frescas", 95000, 4, 18, 0)
    controlador.newProducto("Caja de Tulipanes", "Caja con tulipanes de colores variados", 135000, 4, 0, 0)
    controlador.newProducto("Rosas de Amor", "Caja con rosas rojas y chocolates en forma de corazón", 175000, 5, 15, 10)
    controlador.newProducto("Caja de Rosas Amarillas", "Caja con rosas amarillas vibrantes", 110000, 3, 16, 0)
    controlador.newProducto("Ramo de Rosas Especial", "Ramo de rosas premium con chocolates importados", 200000, 5, 24, 12)
    controlador.newProducto("Caja de Rosas y Vino", "Caja con rosas rojas y una botella de vino", 180000, 4, 12, 0)
    controlador.newProducto("Centro de Mesa Floral", "Centro de mesa con flores variadas y chocolates", 130000, 3, 8, 6)

    