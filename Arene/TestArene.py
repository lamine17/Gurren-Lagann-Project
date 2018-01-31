from Arene import *

#Creation d'une arene et ajout de n objets
a=Arene()
n=3

for i in range(0,n):
    a.add(Objet3D())
print(a)

#on vide l'arene 
a.vider()
print(a)
