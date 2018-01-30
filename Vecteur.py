from Point import *
from math import *
from fonctions import atan2

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

    def getAngle2D(self):
        """ Retourne l'angle du vecteur par rapport a la verticale, dans le sens trigo"""
        return atan2(self._y,self._x)
    
    def diffAngle2D(self, vecteur):
        """retourne la difference d'angle entre 2 vecteurs dans le repere (x, y) """
        if issubclass(type(vecteur), Vecteur) and vecteur:
            v=self**vecteur
            if self._y != 0 and vecteur._x != 0:
                if v._z<0:
                    return -acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
                elif v._z>0:
                    return acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
                else:
                    return 0
            return vecteur.getAngle2D()-self.getAngle2D()
                
    def getNorme(self):
        """Retourne la norme du vecteur """
        return sqrt(pow(self._x,2)+pow(self._y,2)+pow(self._z,2))
    
    def rotation2D(self, teta):
        """tourne le vecteur d'un angle teta"""
        x=self._x
        self._x=(int)(x*cos(teta)-self._y*sin(teta))
        self._y=(int)(x*sin(teta)+self._y*cos(teta))
        
        
