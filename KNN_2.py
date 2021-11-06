from math import *
from random import *
import keyboard
import pickle
import matplotlib.pyplot as plt


def ReadMe():
    donnees = {}
    donnee = []
    m_chaine = ""
    cle = 0
    m_file = open("dataset_iris.txt", "r")
    for line in m_file:
        for c in line:
            m_chaine = m_chaine + c
            if c == "," or c == "\n":
                m_chaine=m_chaine[0:len(m_chaine)-1]+""
                donnee.append(m_chaine)
                m_chaine=""
        donnees.update({cle: donnee})
        donnee=[]
        cle += 1
    m_file.close()
    return donnees

##############################################################################################################
def Random_test():
    teste = {}
    for i in range(25):
        teste.update({i: [round(uniform(0, 9), 1), round(
            uniform(0, 9), 1), round(uniform(0, 9), 1), round(uniform(0, 9), 1),"non"]})
    return teste

##############################################################################################################
def KNN_2(donnees, teste, k):
    cpt1 = 0
    cpt2 = 0
    cpt3 = 0
    i = 1
    distance = {}
    for cle in donnees.keys():
        distance[cle] = sqrt(pow(float(donnees[cle][0])-teste[0], 2) + pow(float(donnees[cle][1]) -
                                                                    teste[1], 2))
    newdistance = sorted(distance.items(), key=lambda x: x[1])
    for cle in newdistance:
        if donnees[cle[0]][4] == "Iris-setosa":
            cpt1 += 1
        elif donnees[cle[0]][4] == "Iris-versicolor":
            cpt2 += 1
        else:
            cpt3 += 1
        if i > k:
            if cpt1 > cpt2 and cpt1 > cpt3:
                teste[4]="Iris-setosa"
            elif cpt2 > cpt1 and cpt2 > cpt3:
                teste[4]="Iris-versicolor"
            elif cpt3 > cpt1 and cpt3 > cpt2:
                teste[4]="Iris-virginica"
            else:
                teste[4]="aucune classe"
            break
        i += 1
################################################# Execution #####################################################
t = Random_test()
data = ReadMe()
print("les données de teste : ")
Fdata = plt.figure(1)
Fdata.suptitle('les données de teste', fontsize=16)
for p in t:
    print(t[p])
    Fdata = plt.plot(t[p][0], t[p][1], '+b')
k = 3
while k<=10:
    Ftest = plt.figure(2)
    Ftest.suptitle(
            'Pour k = {} : "Iris-setosa" en Jaune | "Iris-versicolor" en Vert | "Iris-virginica" en Bleu | "aucune classe" en Bleu'.format(k), fontsize=10)
    for cle in t:
        KNN_2(data, t[cle], k)
    for i in t:
        if t[i][4] == "Iris-setosa":
            Ftest = plt.plot(t[i][0], t[i][1], '-yo')
        elif t[i][4] == "Iris-versicolor":
            Ftest = plt.plot(t[i][0], t[i][1], 'sg')
        elif t[i][4] == "Iris-virginica":
            Ftest = plt.plot(t[i][0], t[i][1], '+b')
        else:
            Ftest = plt.plot(t[i][0], t[i][1], 'black')
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    k+=1
if keyboard.is_pressed('q'):
    plt.close()