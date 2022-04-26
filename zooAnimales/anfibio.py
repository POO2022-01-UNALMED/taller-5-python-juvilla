from zooAnimales.animal import Animal
class Anfibio (Animal):
    ranas=0
    salamandras=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,cpi):
        self._colorPiel=cpi
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self,v):
        self._venenoso=v
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        A=Anfibio(nombre,edad,"selva",genero,"rojo",True)
        cls.ranas+=1
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        A=Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        cls.salamandras+=1
    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio._listado)