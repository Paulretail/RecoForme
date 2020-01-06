# coding: utf-8
""" programme à compléter du kPPV"""
import csv
import math as m

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
    return(dataset)


def calculDistances(data, dataset):
    """ retourne les distances entre data et la partie apprentissage de dataset"""
    distances = []
    for i in range(25) + range(50,75) + range(100,125):
        sum = 0
        for j in range(4):
            sum += (data[j]-dataset[i][j])**2
        distances.append(m.sqrt(sum))

    return(distances)


def calculClasse(distances):
    """ retourne le numéro de la classe déterminé à partir des distances """

    index = distances.index(min(distances))

    return int(index / 25)


if __name__ == "__main__":
    print("Début programme kPPV")
    dataset = lectureFichierCSV()

    confusion = []
    for i in range(25,50) + range(75, 100) + range(125, 150):
        classe = calculClasse(calculDistances(dataset[i], dataset))
        if int(i/50) == classe:
            confusion.append([True, classe, int(i/25), i])
        else:
            confusion.append([False, classe, int(i/25), i])

    print(confusion)

# --------------------------------- Fin kPPV -----------------------------------
