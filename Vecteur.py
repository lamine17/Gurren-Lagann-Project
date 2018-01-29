from Point import *
from math import *
class Vecteur(Point):
    """Defini des methodes de calcul sur les vecteurs """
    def __mul__(self, vecteur):
        """ produit scalaire"""
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return self._x*vecteur._x+self._y*vecteur._y+self._z*vecteur._z

    def __pow__(self, vecteur):
        """produit vectoriel """
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return Vecteur(self._y*vecteur._z-self._z*vecteur._y, self._z*vecteur._x-self._x*vecteur._z, self._x*vecteur._y-self._y*vecteur._x)

    def __add__(self, vecteur):
        """ addition"""
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return Vecteur(self._x+vecteur._x, self._y+vecteur._y, self._z+vecteur._z)
    
    def rotation2D(self, teta):
        """tourne le vecteur d'un angle teta"""
        x=self._x
        self._x=(int)(x*cos(teta)-self._y*sin(teta))
        self._y=(int)(x*sin(teta)+self._y*cos(teta))
        
