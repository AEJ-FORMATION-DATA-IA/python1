# -*- coding: utf-8 -*-
"""
Spyder Editor
Les operation
"""
A = 15 
B = 4
C = A + B 
 
print(C)

D= A *B 
E= A**B
F=A/B
G= int(A/B)
H= A%B

"""
Les dictionnaires de données
"""


"""les operations sont les clé et les resultats sont les valeurs"""

dict_1= {
    "A + B": C ,
    "A * B":D ,
    "A**B":E ,
    "A/B":F ,
    "A/B":G ,
    "A%B":H 
    }

""" modifier un element dans un dictionnaire """

dict_1['A + B']= 30

"""adjouter un element dans un dictionnaire"""

dict_1['5+5']= 10

"""supprimer un element dans un dictionnaire"""

dict_1.pop('5+5')

"""afficher la liste des clés"""

print(dict_1.keys())

"""afficher la liste des valeur"""

print(dict_1.values())

"""afficher la liste des clés:valeurs"""

print(dict_1)


"""
Les tuples 

"""


tuple_1= (A,B,C)
print(tuple_1)

"""
Premier programme

"""

x=input('veuillez entré un nombre entier ')

if(x.isdigit() == False): 
    print('oups !! , vous avez fait une erreur')
else:
    y= input('Veuillez saisir un deuxieme entier ')
    if(x.isdigit() == False): 
     print('oups !! , vous avez fait une erreur')
    else:
        resultat = int(x) + int(y)
        print(resultat)
        
        

"""
Deuxieme programme

"""
x=input('veuillez entré un nombre entier ')

if(x.isdigit() == False): 
    print('oups !! , vous avez fait une erreur')
else:
    y= input('Veuillez saisir un deuxieme entier ')
    if(x.isdigit() == False): 
     print('oups !! , vous avez fait une erreur')
    else:
        if(int(x) > int(y)):
            print( f'{x} est superieur a {y}')
        elif int(x)  < int(y):
            print( f'{x} est inferieur a {y}')
        elif int(x)  == int(y):
            print( f'{x} est egale a {y}')
            

       
      
    
        
        