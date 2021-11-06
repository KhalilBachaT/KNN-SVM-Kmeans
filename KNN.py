"""              KNN                    """

from math import *
from random import *
import keyboard
import matplotlib.pyplot as plt
import mpld3


def init():
    print("Entrer les coordonées de centre du circle")
    centre = []
    test = {}
    donnees = {}
    x = input("x = ")
    y = input("y = ")
    R1 = input("R1 = ")
    R2 = input("R2 = ")
    R1 = float(R1)
    R2 = float(R2)
    centre.append(float(x))
    centre.append(float(y))
    for i in range(100):
        donnees.update(
            {i: [round(uniform(0, 100), 2), round(uniform(0, 100), 2)]})
    for i in donnees.keys():
        if sqrt(pow(donnees[i][0]-centre[0], 2)+pow(donnees[i][1]-centre[1], 2)) <= R1:
            donnees[i].append("et1")
        elif sqrt(pow(donnees[i][0]-centre[0], 2)+pow(donnees[i][1]-centre[1], 2)) >= R2:
            donnees[i].append("et2")
        else:
            donnees[i].append("no")
            test.update({i: donnees[i]})
    return donnees, test, x, y, R1, R2

#######################################################################################################


def KNN_V1(donnees, teste, k):
    distance = {}
    i = 1
    cpt1 = 0
    cpt2 = 0
    for cle in donnees.keys():
        if donnees[cle][2] == "et1" or donnees[cle][2] == "et2":
            distance[cle] = sqrt(
                pow(donnees[cle][0]-teste[0], 2) + pow(donnees[cle][1]-teste[1], 2))
    newdistance = sorted(distance.items(), key=lambda x: x[1])
    for cle in newdistance:
        if donnees[cle[0]][2] == "et1":
            cpt1 += 1
        elif donnees[cle[0]][2] == "et2":
            cpt2 += 1
        else:
            pass
        if i > k:
            if cpt1 > cpt2:
                teste[2] = "et1"
            else:
                teste[2] = "et2"
            break
        i += 1
    return newdistance

##############################################################################################################


def Affiche(data, tt,Ajour):
    Fdata = plt.figure(1)
    if Ajour==True:
        Fdata.suptitle('Les données en rouge et le teste en bleu Aprés Mise à jour', fontsize=16)    
    else:
        Fdata.suptitle('Les données en rouge et le teste en bleu', fontsize=16)
    k = 3
    print("les donnees d'aprentissage :".center(20))
    for ind in data:
        print("point{} : x={} , y={} ,class={}".format(ind,data[ind][0],data[ind][1],data[ind][2]))
        Fdata = plt.plot(data[ind][0], data[ind][1], '+r')
    for t in tt:
        Fdata = plt.plot(tt[t][0], tt[t][1], '-bo')
    print("*-----------------* KNN *---------------------------*")
    while k <= 20:
        Ftest = plt.figure(2)
        Ftest.suptitle(
            'Pour k = {} : "et1" en Jaune / "et2" en Vert'.format(k), fontsize=16)
        print(
            "Pour k = {} :>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>".format(k))
        print("les donnees de teste :".center(20))      # revoir ca
        for ind in tt:
            print("point{} : x={} , y={}".format(ind,tt[ind][0],tt[ind][1]))
        print("--------------------********** ----------------")
        for cle in tt:
            KNN_V1(data, tt[cle], k)
        print("les donnees de teste apres classification:".center(40))
        for ind in tt:
            print("point{} : x={} , y={} ,class={}".format(ind,tt[ind][0],tt[ind][1],tt[ind][2]))
            if tt[ind][2] == "et1":
                Ftest = plt.plot(tt[ind][0], tt[ind][1], '-yo')
            elif tt[ind][2] == "et2":
                Ftest = plt.plot(tt[ind][0], tt[ind][1], 'sg')
            else:
                pass
        plt.show(block=False)
        plt.pause(3)
        plt.close()
        k += 1
    if keyboard.is_pressed('q'):
        plt.close(2)
    print("--------------------********** ----------------")

##############################################################################################################


def update(donnees):
    et1 = {}
    et2 = {}
    for cle in donnees:
        if donnees[cle][2] == "et1":
            et1.update({cle: donnees[cle]})
        elif donnees[cle][2] == "et2":
            et2.update({cle: donnees[cle]})
        else:
            pass
    if int(len(et1) * 0.05) > 0:
        for i in range(int(len(et1) * 0.05)):
            ind = randint(0, len(et1)-1)
            donnees[ind][2] = "et2"
    if int(len(et2) * 0.05) > 0:
        for i in range(int(len(et2) * 0.05)):
            ind = randint(0, len(et2)-1)
            donnees[ind][2] = "et1"

    return donnees


################################################# Execution #####################################################
data, told, x, y, r1, r2 = init()
Affiche(data, told,False)
print("--------------------------------------------After Update-------------------------------")
data = update(data)
Affiche(data, told,True)
