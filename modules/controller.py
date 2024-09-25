import sqlalchemy
import sqlalchemy.orm
from modules.models import Cliente, Producto, Pedido, ProductosVendidos, Domicilio
from sqlite3 import ProgrammingError
import sqlite3 as sql
import os
import sys

comunas = {
    "popular": ["santo domingo", "popular", "granizal", "moscu", "villa guadalupe", "san pablo", "aldea pablo vi", "la esperanza", "el compromiso", "la avanzada", "carpinelo"],
    "santa cruz": ["la isla", "el playon", "pablo vi", "la frontera", "la francia", "andalucia", "villa del socorro", "villa niza", "santa cruz", "la rosa"],
    "manrique": ["la salle", "las granjas", "campo valdes", "santa ines", "el raizal", "el pomar", "manrique", "manrique oriental", "versalles", "la cruz", "oriente", "maria cano", "carambolas", "san jose la cima"],
    "aranjuez": ["berlin", "san isidro", "palermo", "bermejal", "los alamos", "moravia", "sevilla", "san pedro", "las esmeraldas", "la pinuela", "aranjuez", "brasilia", "miranda"],
    "castilla": ["toscana", "las brisas", "florencia", "tejelo", "boyaca", "hector abad gomez", "belalcazar", "girardot", "tricentenario", "castilla", "francisco antonio zea", "alfonso lopez", "caribe", "el progreso"],
    "doce de octubre": ["santander", "doce de octubre", "pedregal", "la esperanza", "san martin de porres", "kennedy", "picacho", "picachito", "mirador del doce", "progreso", "el triunfo"],
    "robledo": ["el volador", "san german", "facultad de minas", "pilarica", "bosques de san pablo", "altamira", "cordoba", "lopez de mesa", "el diamante", "aures", "bello horizonte", "villa flora", "palenque", "robledo", "cucaracho", "fuente clara", "santa margarita", "olaya herrera", "pajarito", "monteclaro", "la iguana"],
    "villa hermosa": ["villa hermosa", "la mansion", "san miguel", "la ladera", "batallon girardot", "llanaditas", "los mangos", "enciso", "sucre", "el pinal", "trece de noviembre", "la libertad", "villatina", "san antonio", "las estancias", "villa turbay", "la sierra", "villa lilliam"],
    "buenos aires": ["juan pablo ii", "barrios de jesus", "el vergel", "alejandro echavarria", "caicedo", "buenos aires", "miraflores", "cataluna", "la milagrosa", "gerona", "el salvador", "loreto", "asomadera", "ocho de marzo"],
    "la candelaria": ["prado", "jesus nazareno", "el chagualo", "estacion villa", "san benito", "guayaquil", "corazon de jesus", "calle nueva", "perpetuo socorro", "barrio colon", "las palmas", "bombona", "boston", "los angeles", "villa nueva", "la candelaria", "san diego"],
    "laureles estadio": ["carlos e restrepo", "suramericana", "naranjal", "san joaquin", "los conquistadores", "bolivariana", "laureles", "las acacias", "la castellana", "lorena", "el velodromo", "estadio", "los colores", "cuarta brigada", "florida nueva"],
    "la america": ["ferrini", "calasanz", "los pinos", "la america", "la floresta", "santa lucia", "el danubio", "campo alegre", "santa monica", "barrio cristobal", "simon bolivar", "santa teresita", "calasanz"],
    "san javier": ["el pesebre", "blanquizal", "santa rosa de lima", "los alcazares", "metropolitano", "la pradera", "juan xiii", "la quiebra", "san javier", "veinte de julio", "belencito", "betania", "el corazon", "las independencias", "nuevos conquistadores", "el salado", "eduardo santos", "antonio narino", "el socorro"],
    "el poblado": ["barrio colombia", "simesa", "villa carlota", "castropol", "lalinde", "las lomas", "altos del poblado", "el tesoro", "los naranjos", "los balsos", "san lucas", "el diamante", "el castillo", "alejandria", "la florida", "el poblado", "manila", "astorga", "patio bonito", "la aguacatala", "santa maria de los angeles"],
    "guayabal": ["tenche", "trinidad", "santa fe", "aeroarque juan pablo ii", "campo amor", "noel", "cristo rey", "guayabal", "la colina", "el rodeo"],
    "belen": ["fatima", "rosales", "belen", "granada", "san bernardo", "las playas", "diego echevarria", "la mota", "la hondonada", "rincon", "la loma de los bernal", "la gloria", "altavista", "la palma", "los alpes", "las violetas", "las mercedes", "nueva villa de aburra", "miravalle", "el nogal", "los almendros", "cerro nutibara"]
}
zonas = {
    "zona nororiental": ["popular", "santa cruz", "manrique", "aranjuez"],
    "zona noroccidental": ["castilla", "robledo", "doce de octubre"],
    "zona centro oriental": ["villa hermosa", "buenos aires", "la candelaria"],
    "zona centro occidental": ["laureles estadio", "la america", "san javier"],
    "zona suroriental": ["poblado"],
    "zona suroccidental": ["guayabal", "belen"],
    "zona sur" : ["envigado", "itagui"],
    "zona sur2" : ["san antonio de prado", "caldas"],
    "zona norte" : ["bello", "niquia", "copacabana"]
}

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

                if infoDomicilio[4] == "itagui" or infoDomicilio[4] == "envigado":
                    zona = "Zona Sur"
                elif infoDomicilio[4] == "san antonio de prado" or infoDomicilio[4] == "caldas":
                    zona = "Zona Sur2"
                elif infoDomicilio[4] == "medellin":
                    comuna = None  # Inicializar comuna
                    for key in comunas:
                        if infoDomicilio[3] in comunas[key]:
                            comuna = key
                            break
                    if comuna:  # Solo proceder si se encontró una comuna
                        for key in zonas:
                            if comuna in zonas[key]:
                                zona = key
                                break

                domicilio = Domicilio(idPedido=pedido.idPedido, nombreDestinatario=infoDomicilio[0], telefonoDestinatario=infoDomicilio[1],
                                    nomenclatura=infoDomicilio[2], barrio=infoDomicilio[3],
                                    municipio=infoDomicilio[4], codigoPostal=infoDomicilio[5], infoAdicional=infoDomicilio[6], zona=zona)
                


                self.session.add(domicilio)
                self.session.commit()


                domicilio = self.session.query(Domicilio).filter(Domicilio.idPedido == idPedido).first()
                pedido.idDomicilio = domicilio.idDomicilio
                self.session.commit()


            cliente.pedidosHechos +=1
            self.session.commit()

    def newDomicilio(self, idPedido, nombre, telefono, ciudad, direccion, barrio, postal, infoadicional):
        pedido = self.session.query(Pedido).filter(Pedido.idPedido == idPedido).first()

        conn = sql.connect(resource_path("database\\ravello.db"))
        c = conn.cursor()

        c.execute(f"SELECT COUNT(*) FROM domicilio")
        resultado = c.fetchone()
        
        
        pedido.idDomicilio = int(resultado[0])+1
        self.session.commit()

        c.close()
        conn.close()

        if ciudad.lower() == "itagui" or ciudad.lower() == "envigado":
            zona = "Zona Sur"
        elif ciudad.lower() == "san antonio de prado" or ciudad.lower()== "caldas":
            zona = "Zona Sur2"
        elif ciudad.lower() == "medellin":
            comuna = None  # Inicializar comuna
            for key in comunas:
                if barrio.lower() in comunas[key]:
                    comuna = key
                    break
            if comuna:  # Solo proceder si se encontró una comuna
                for key in zonas:
                    if comuna in zonas[key]:
                        zona = key
                        break
        print(zona)
        
        domicilio = Domicilio(idPedido=idPedido, nombreDestinatario=nombre, telefonoDestinatario=telefono, municipio=ciudad, nomenclatura=direccion,
                              barrio=barrio, codigoPostal=postal, infoAdicional=infoadicional, zona=zona)
        self.session.add(domicilio)
        self.session.commit()

    def updateDomicilio(self, idPedido, nombre, telefono, ciudad, direccion, barrio, postal, infoadicional):
        domicilio = self.session.query(Domicilio).filter(Domicilio.idPedido == idPedido).first()

        if ciudad.lower() == "itagui" or ciudad.lower() == "envigado":
            zona = "Zona Sur"
        elif ciudad.lower() == "san antonio de prado" or ciudad.lower()== "caldas":
            zona = "Zona Sur2"
        elif ciudad.lower() == "medellin":
            comuna = None  # Inicializar comuna
            for key in comunas:
                if barrio.lower() in comunas[key]:
                    comuna = key
                    break
            if comuna:  # Solo proceder si se encontró una comuna
                for key in zonas:
                    if comuna in zonas[key]:
                        zona = key
                        break

        if domicilio != None:
            domicilio.nombreDestinatario = nombre
            domicilio.telefonoDestinatario = telefono
            domicilio.municipio = ciudad
            domicilio.nomenclatura = direccion
            domicilio.barrio = barrio
            domicilio.codigoPostal = postal
            domicilio.infoAdicional = infoadicional
            domicilio.zona = zona
            
            self.session.commit()
        
        else:
            raise ProgrammingError("Domicilio no se encuentra en base de datos!")

    def delDomicilio(self, idPedido):
        domicilio = self.session.query(Domicilio).filter(Domicilio.idPedido == idPedido).first()
        pedido = self.session.query(Pedido).filter(Pedido.idPedido == idPedido).first()

        pedido.idDomicilio = 0
        self.session.commit()

        if domicilio == None:
            raise ProgrammingError("Domicilio no se encuentra en base de datos!")
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
        

    