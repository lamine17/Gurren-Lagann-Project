from Vecteur import *

#operations sur les vecteurs
v2=Vecteur(1,0,0)
v1=Vecteur(3,0,23)
print("v1 = {}, v2 = {}".format(v1, v2))
print("v1 + v2 = {}".format(v1+v2))
print("v1 * v2 = {}".format(v1*v2))
print("v1 ^ v2 = {}".format(v1**v2))

#rotation
n=8
teta=2*pi/n
horizontale=Vecteur(1,0,0)
diff=v1.diffAngle2D(horizontale)
print("angle : {} radians / {} degres ".format(diff,int(diff*360/(2*pi))))
print("v1 = {}".format(v1))

print("{} rotation de {} radians/ {} degres de v1 = {}".format(n,teta, int(teta*360/(2*pi)), v1))

for i in range(0, n):
    print("|v1|= |{}| = {}".format(v1,v1.getNorme()))
    print("rotation de v1...")
    v1.rotation2D(teta)
    print("|v1|= |{}| = {}".format(v1,v1.getNorme()))
    diff=v1.diffAngle2D(horizontale)
    print("angle : {} radians / {} degres ".format(diff,int(diff*360/(2*pi))))


