from math import *
from random import *
import matplotlib.pyplot as plt


def init():
    donnees = {}
    test = {}
    for i in range(5):
        donnees.update(
            {i: [round(uniform(0, 10), 1), round(uniform(0, 10), 1), "classA"]})
        if i > 2:
            donnees.update( 
                {i: [round(uniform(0, 10), 1), round(uniform(0, 10), 1), "classB"]})
    for i in range(10):
        test.update({i: [round(uniform(0, 10), 1), round(uniform(0, 10), 1),"non"]})
    return donnees, test

##############################################################################################################
def SVM(donnees, test):
    cl1 = {}
    cl2 = {}
    distance1 = {}
    distance2 = {}
    min_distance1=[]
    min_distance2=[]
    for cle in donnees.keys():
        if donnees[cle][2] == "classA":
            cl1.update({cle: donnees[cle]})
        else:
            cl2.update({cle: donnees[cle]})
    for cle in cl1:
        d1={}
        for cle1 in cl2:
            d1[cle1] = sqrt(pow(cl2[cle1][0]-cl1[cle][0], 2) + pow(cl2[cle1][1] -
                                                                          cl1[cle][1], 2))
        distance1.update({cle:d1})
    for cle in cl2:
        d2={}
        for cle1 in cl1:
            d2[cle1] = sqrt(pow(cl1[cle1][0]-cl2[cle][0], 2) + pow(cl1[cle1][1] -
                                                                          cl2[cle][1], 2))
        distance2.update({cle:d2})
    min_d1n=[]
    min_d2n=[]
    for d in distance1:
        min_d1 = sorted(distance1[d].items(), key=lambda x: x[1])
        min_d1n.append(min_d1[0])
    min_distance1=sorted(min_d1n, key=lambda x: x[1])
    for d in distance2:
        min_d2 = sorted(distance2[d].items(), key=lambda x: x[1])
        min_d2n.append(min_d2[0])
    min_distance2=sorted(min_d2n, key=lambda x: x[1])
    a = cl1.get(min_distance2[0][0])
    b = cl2.get(min_distance1[0][0])
    w = [a[0]-b[0], a[1]-b[1]]  # (x*a,y*a)
    # (xa * xA + ya * yA + w0) class 1
    fw = [w[0]*a[0], w[1]*a[1], w[0]*b[0], w[1]*b[1]]
    # (xa * xB + ya * yB + w0) class 2
    aa = -2/(-fw[0]-fw[1]+fw[2]+fw[3])
    w0 = 1-fw[0]*aa-fw[1]*aa
    fw = [w[0]*aa, w[1]*aa, w0]
    dis_test=fw[0]*float(test[0])+fw[1]*float(test[1])+fw[2]
    equation=[a,b,fw[0],fw[1],fw[2]]
    if dis_test>0:
        test[2]="classA"
    else:
        test[2]="classB"
    return equation
##############################################################################################################
def Affichage():
    data, test = init()
    equ=[]
    for t in test:
        print("Mon Point Avant :",test[t])
    for t in test:
        equ = SVM(data,test[t])
        print("Mon Point Apres :",test[t])
    print("a={},    b={},L'equation : fw= {} * x1 + {} * x2 + {}".format(equ[0],equ[1],equ[2],equ[3],equ[4]))
################################################# Execution #####################################################
Affichage()
