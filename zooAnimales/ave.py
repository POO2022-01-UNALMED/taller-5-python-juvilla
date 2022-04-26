from zooAnimales.animal import Animal
class Ave (Animal):
    halcones=0
    aguilas=0
    _listado=[]
    def __init__(self, nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,cpl):
        self._colorPlumas=cpl
    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        A=Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        cls.halcones+=1
    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        A=Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        cls.aguilas+=1

    @classmethod
    def cantidadAves(cls):
        return len(Ave._listado)