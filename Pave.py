from Arene import Objet3D

class Pave(Objet3D):
    """permet de creer des paves """
    def __init__(self, longueur, largeur, hauteur):
        Objet3D.__init__(self)
        #face du bas
        self.addSommet(Point(0,0,0))
        self.addSommet(Point(longueur,largeur,0))
        self.addSommet(Point(longueur,0,0))
        self.addSommet(Point(0,largeur,0))
        #face du haut
        self.addSommet(Point(0,0,hauteur))
        self.addSommet(Point(longueur,largeur,hauteur))
        self.addSommet(Point(longueur,0,hauteur))
        self.addSommet(Point(0,largeur,hauteur))
        
    def __getattr__(self, nom):
        """Permet d'acceder a un attribut. si ce n'est pas possible:"""
        print("L'attribut {} n'est pas accessible dans Pave !".format(nom))
