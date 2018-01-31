class Point(object):
    """Classe definissant un point dans un espace 3D"""
    def __init__(self, x, y, z):
        """Initialise les coordonnees du point """
        self.__x=x
        self.__y=y
        self.__z=z

    def setPosition(self, point):
        """Modifie les coordonnees du point """
        if issubclass(type(point), Point):
            self.__x=point.__x
            self.__y=point.__y
            self.__z=point.__z
    
    def deplacer(self, vecteur):
        """Deplace le point d'un vecteur (dx, dy, dz)"""
        if issubclass(type(vecteur),Point):
            self.__x=self.__x+vecteur.__x
            self.__y=self.__y+vecteur.__y
            self.__z=self.__z+vecteur.__z

    def getCoord(self):
        """Accesseur sur les coordonneess"""
        return self.__x, self.__y, self.__z

    def __repr__(self):
        """Quand on entre un objet3D dans l'interpreteur"""
        return "({}, {}, {})".format(self.__x, self.__y, self.__z)

    def __getattr__(self, nom):
        """Permet d'acceder a un attribut. si ce n'est pas possible:"""
        print("L'attribut {} n'est pas accessible dans Point !".format(nom))

    def __add__(self, point):
        if issubclass(type(point), Point) and point:
            return Point(self.__x+point.__x, self.__y+point.__y, self.__z+point.__z)
    
        
