# coding: utf-8
""" programme à compléter du kPPV"""
import csv
import math as m

import numpy as np

nbExParClasse = 50
nbApprent = 25
nbCaract = 4
nbClasse = 3


def lectureFichierCSV():
    with open("iris.data", 'r')as fic:
        lines = csv.reader(fic)
        dataset = list(lines)
    # print(dataset[0], len(dataset))
    for i in range(len(dataset)):
        for j in range(nbCaract):
            dataset[i][j] = float(dataset[i][j])
    # print(dataset[0])
    return dataset


def calculDistances(data, dataset):
    """ retourne les distances entre data et la partie apprentissage de dataset"""
    distances = []
    for i in range(25):
        sum = 0
        for j in range(4):
            sum += (data[j]-dataset[i][j])**2
        distances.append(m.sqrt(sum))

    for i in range(50, 75):
        sum = 0
        for j in range(4):
            sum += (data[j] - dataset[i][j]) ** 2
        distances.append(m.sqrt(sum))

    for i in range(100, 125):
        sum = 0
        for j in range(4):
            sum += (data[j] - dataset[i][j]) ** 2
        distances.append(m.sqrt(sum))

    return distances


def calculClasse(distances):
    """ retourne le numéro de la classe déterminé à partir des distances """

    index = distances.index(min(distances))

    return int(index/25)

def calcul_taux_reco(confusion):
    """ retourne le taux de reconnaissance d'une matrice de confusion"""

    return float(sum([confusion[i][i] for i in range(len(confusion))])) / sum([confusion[i][j] for i in range(len(confusion)) for j in range(len(confusion))])


if __name__ == "__main__":
    print("Début programme kPPV")
    dataset = lectureFichierCSV()
    confu = np.zeros(shape=(3,3))

    for i in range(25, 50) :
        classe = calculClasse(calculDistances(dataset[i], dataset))
        if classe == 0:
            confu[0][0] = confu[0][0] + 1
        elif classe == 1:
            confu[0][1] = confu[0][1] + 1
        elif classe == 2:
            confu[0][2] = confu[0][2] + 1

    for i in range(75, 100) :
        classe = calculClasse(calculDistances(dataset[i], dataset))
        if classe == 1:
            confu[1][1] = confu[1][1] + 1
        elif classe == 0:
            confu[1][0] = confu[1][0] + 1
        elif classe == 2:
            confu[1][2] = confu[1][2] + 1

    for i in range(125, 150):
        classe = calculClasse(calculDistances(dataset[i], dataset))
        if classe == 2:
            confu[2][2] = confu[2][2] + 1
        elif classe == 0:
            confu[2][0] = confu[2][0] + 1
        elif classe == 1:
            confu[2][1] = confu[2][1] + 1

    print(confu)


# --------------------------------- Fin kPPV -----------------------------------
