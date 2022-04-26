class Zona:
    def __init__(self,nombre,zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre
    def getZoo(self):
        return self._zoo
    def setZoo(self,zoo):
        return self._zoo
    def agregarAnimales(self,animales):
        self._animales.append(animales)
    def cantidadAnimales(self):
        return len(self._animales)
    