#Clase de los juegos
class Juego:
    def __init__(self,id,nombre,minJugadores,maxJugadores,limiteEdad,pais,precio):
        self.id=id
        self.nombre=nombre
        self.minJugadores=minJugadores
        self.maxJugadores=maxJugadores
        self.limiteEdad=limiteEdad
        self.pais=pais
        self.precio=precio
    
    def toDbCollection(self):
        return{ 
        'id':self.id,
        'nombre':self.nombre,
        'minJugadores':self.minJugadores,
        'maxJugadores':self.maxJugadores,
        'limiteEdad':self.limiteEdad,
        'pais':self.pais,
        'precio':self.precio
        } 