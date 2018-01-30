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

    def diffAngle(self, vecteur):
        if issubclass(type(vecteur), Vecteur) and vecteur:
            if self._y != 0 and vecteur._x != 0:
                s=(self._x*vecteur._y)/(self._y*vecteur._x)
                if s<0:
                    return -acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
                elif s>0:
                    return acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
                else:
                    return 0
            
    def getNorme(self):
        """Retourne la norme du vecteur """
        return sqrt(pow(self._x,2)+pow(self._y,2)+pow(self._z,2))
    
    def rotation2D(self, teta):
        """tourne le vecteur d'un angle teta"""
        x=self._x
        print(self.getNorme())
        self._x=(int)(x*cos(teta)-self._y*sin(teta))
        self._y=(int)(x*sin(teta)+self._y*cos(teta))
        print(self.getNorme())
        
