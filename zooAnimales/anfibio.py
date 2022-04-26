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
    def crearRana(nombre,edad,genero):
        A=Anfibio(nombre,edad,"selva",genero,"rojo",True)
        ranas+=1
    @classmethod
    def crearSalamandra(nombre,edad,genero):
        A=Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        salamandras+=1
    @classmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)