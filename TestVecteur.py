from Vecteur import *

#operations sur les vecteurs
v1=Vecteur(1,0,0)
v2=Vecteur(3,646,23)
print("v1 = {}, v2 = {}".format(v1, v2))
print("v1 + v2 = {}".format(v1+v2))
print("v1 * v2 = {}".format(v1*v2))
print("v1 ^ v2 = {}".format(v1**v2))

#rotation
n=8
teta=2*pi/n
for i in range(0, n):
    v1.rotation2D(teta)
print("{} rotation de {} radians de v1 = {}".format(n,teta, v1))
