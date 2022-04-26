from zooAnimales.animal import Animal
class Reptil(Animal):
    iguanas=0
    serpientes=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,ce):
        self._colorEscamas=ce
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self,lc):
        self._largoCola=lc
    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        A=Reptil(nombre,edad,"humedal",genero,"verde",3)
        cls.iguanas+=1
    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        A=Reptil(nombre,edad,"jungla",genero,"blanco",1)
        cls.serpientes+=1
    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)