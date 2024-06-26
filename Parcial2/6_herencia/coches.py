#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #Metodo constructor

    def _init_(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas

    #El encapsulamiento en Python tambipen es llamado visibilidad y prácticamente se puede hacer que un atributo y/o método sean públicos o privados

    #Atributo público
    atributo_publico="Soy un atributo público"
    #Atributo privado
    __atributo_privado="Soy un atributo privado"
    
    #Nota 1: Para utilizar un atributo privado es necesario hacerlo a través de un métdo público
    def getAtributoPrivado(self):
       return self.__atributo_privado
    
    #Método privado
    def _MetodoPrivado(self):
       print("Soy un método privado")

    #Nota 2: Para utilizar un método privado es necesario hacerlo dentro de un método público
    def MetodoPublico(self):
       self._MetodoPrivado()
    
    
    
    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPlazas(self):
       return self.plazas

    def setPlazas(self,plazas):
      self.plazas=plazas 

    def getInfo(self):
       print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")

class Camiones(Coches):
   def _init_(self,color,marca,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
      super()._init_(color,marca,modelo,velocidad,caballaje,plazas)
      self.__eje=eje
      self.__capacidadCarga=capacidadCarga
    
   __tipo_carga=""
   def cargar(self,tipo_carga):
    self.tipo_carga=tipo_carga
    return self.tipo_carga
   
   def getEje(self):
      return self.__eje
   
   def setEje(self,eje):
      self.__eje=eje
    
   def getcapacidadCarga(self):
      return self.__capacidadCarga
   
   def setcapacidadCarga(self,capacidadCarga):
      self.__capacidadCarga=capacidadCarga
    
   def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp, con {self.getEje()} ejes y una capacidad de carga de {self.getcapacidadCarga()} Toneladas")

class Camionetas(Coches):
   def _init_(self,color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada):
      super()._init_(color,marca,modelo,velocidad,caballaje,plazas)
      self.traccion=traccion
      self.cerrada=cerrada
   
   __num_transporte=""

   def transportar(self,num_transporte):
      self.num_transporte=num_transporte
      return self.num_transporte
   
   def gettraccion(self):
      return self.traccion
   
   def settraccion(self,traccion):
      self.traccion=traccion
   
   def getcerrada(self):
      return self.cerrada
   
   def setcerrada(self,cerrada):
      self.cerrada=cerrada
    
   def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp, una traccion {self.gettraccion()} y esta cerrada: {self.getcerrada()}")
   
#Fin definir clase

   

