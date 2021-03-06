class Animal:
    _totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        Animal._totalAnimales+=1
    def getNombre(self):
        return self._nombre
    def setNombre (self,n):
        self._nombre=n
    def getEdad(self):
        return self._edad
    def setEdad (self,e):
        self._nombre=e
    def getHabitat(self):
        return self._habitat
    def setHabitat (self,h):
        self._habitat=h
    def getGenero(self):
        return self._genero
    def setGenero (self,g):
        self._genero=g
    def getZona(self):
        return self._zona
    def setZona (self,z):
        self._zona=z
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.reptil import Reptil
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\nAves : " + str(Ave.cantidadAves()) + "\nReptiles : "+ str(Reptil.cantidadReptiles()) + "\nPeces : " + str(Pez.cantidadPeces()) +"\nAnfibios : " + str(Anfibio.cantidadAnfibios())
    def toString(self):
        if self._zona==None:
            return "Mi nombre es "+ self._nombre +", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero
        return "Mi nombre es "+ self._nombre +", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero+", la zona en la que me ubico es "+self._zona+", en el "+self._zona._zoo
