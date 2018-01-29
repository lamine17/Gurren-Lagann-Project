from Vecteur import *

#operations sur les vecteurs
v1=Vecteur(3,2,1)
v2=Vecteur(1,6,2)
print("v1 = {}, v2 = {}".format(v1, v2))
print("v1 + v2 = {}".format(v1+v2))
print("v1 * v2 = {}".format(v1*v2))
print("v1 ^ v2 = {}".format(v1**v2))

#rotation
teta=pi
v1.rotation2D(teta)
print("rotation de {} radiand de v1 = {}".format(teta, v1))
