from math import *

class Vecteur(object):
    """Classe definissant un vecteur (x,y,z) tres similaire a la classe Point"""
    def __init__(self, x, y, z):
        """Constructeur du vecteur"""
        self._x=x
        self._y=y
        self._z=z

    def getCoordonnees(self):
        """Accesseur sur les coordonnees"""
        return self._x, self._y, self._z
    
    def __getattr__(self, nom):
        """Permet d'acceder a un attribut. si ce n'est pas possible:"""
        print("L'attribut {} n'est pas accessible dans Vecteur !".format(nom))

    def __repr__(self):
        """Quand on entre un objet3D dans l'interpreteur"""
        return "Vecteur: (x={}, y={}, z={})".format(self._x, self._y, self._z)

    def __eq__(self, vecteur):
        if issubclass(type(vecteur), Vecteur) and vecteur:
            if self._x==vecteur._x and self._y==vecteur._y and self._z==vecteur._z:
                return True
        return False

    def getNorme(self):
        return sqrt(pow(self._x,2)+pow(self._y,2)+pow(self._z,2))            
