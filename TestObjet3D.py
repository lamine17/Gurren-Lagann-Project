from Objet3D import *

<<<<<<< HEAD
#ici, in se sert d'un point a la place d'un vecteur
#Creation d'un carre de cote 1 et deplacement de celui-ci du vecteur v
v=Point(1,1,1)
=======
#Creation d'un carre de cote 1 et deplacement de celui-ci du vecteur v
v=Vecteur(1,1,1)
>>>>>>> 17ca1a8265940d4f81a5a05f54bce69bda0918fc
o = Objet3D()

#creation
o.addSommet(Point(0,0,0))
o.addSommet(Point(1,0,0))
o.addSommet(Point(0,1,0))
o.addSommet(Point(1,1,0))
o.setCentre(Point(0,0,0))
print(o)

#deplacement puis affichage
print("deplacement de {}".format(v))
o.deplacer(v)
print(o)

#Acces aux attributs
print("Acces a la liste de sommets")
l=o.getSommets()
print(l)

