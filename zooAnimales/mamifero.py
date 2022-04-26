from zooAnimales.animal import Animal
class Mamifero(Animal):
    caballos=0
    leones=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    def isPelaje(self):
        return self._pelaje
    def setPelaje(self,pl):
        self._pelaje=pl
    def getPatas(self):
        return self._patas
    def setPatas(self,pt):
        self._patas=pt
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        A=Animal(nombre,edad,"pradera",genero,True,4)
        caballos+=1

    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        A=Animal(nombre,edad,"selva",genero,True,4)
        leones+=1

    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero._listado)