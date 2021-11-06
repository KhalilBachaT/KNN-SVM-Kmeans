from math import *
from random import *
import matplotlib.pyplot as plt


def init():
    donnees = {}
    barycentes = {}
    k = 6
    for i in range(5):
        donnees.update(
            {i: [round(uniform(0, 10), 1), round(uniform(0, 10), 1)]})
        if i > 2:
            donnees.update(
                {i: [round(uniform(0, 10), 1), round(uniform(0, 10), 1)]})
    while i <= k:
        barycentes.update(
            {i: [round(uniform(0, 10), 1), round(uniform(0, 10), 1)]})
        i += 1
    return donnees, barycentes

##############################################################################################################
def K_means(donnees, barycentes):
    distance_point = {}
    for d in donnees.keys():
        for b in barycentes.keys():
            distance_point[b] = sqrt(
                pow(barycentes[b][0]-donnees[d][0], 2) + pow(barycentes[b][1]-donnees[d][1], 2))
        min_dis = sorted(distance_point.items(), key=lambda x: x[1])
        barycentes[min_dis[0][0]].append(({d: donnees[d]}))
    # repeter jusqu'à ya pas de changement !
    oldbarycentes = {}
    while oldbarycentes != barycentes:
        for b in barycentes:
            oldbarycentes.update({b: barycentes[b]})
        for b in barycentes:
            moyenne = [0, 0]
            ind = 2
            while ind < len(barycentes[b]):
                for cle in barycentes[b][ind]:
                    moyenne[0] = moyenne[0]+barycentes[b][ind][cle][0]
                    moyenne[1] = moyenne[1]+barycentes[b][ind][cle][1]
                ind += 1
            if moyenne[0] != 0 and moyenne[1] != 0:
                barycentes[b][0] = moyenne[0]/(len(barycentes[b])-2)
                barycentes[b][1] = moyenne[1]/(len(barycentes[b])-2)
    return barycentes

################################################# Execution #####################################################
d, b = init()
print("----------------------------------------")
print("----------------------------------------")
print("les données :")
for dd in d:
    print(d[dd])
print("----------------------------------------")
print("----------------------------------------")
print("les barycentes :")
for bb in b:
    print(b[bb])
print("----------------------------------------")
print("----------------------------------------")
nb=K_means(d, b)
for n in nb:
    print("le barycente : x={}, y={} ".format(nb[n][0],nb[n][1]))
    if len(nb[n])>2 :
        print("Les points pour ce barycente : ",nb[n][2])
    print("--------------***************--------------------------")