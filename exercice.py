#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math, turtle


# TODO: Définissez vos fonction ici

# Exercice 1
def ellipsoide(demi_axes, masse_volumique):
    x, *y, z = demi_axes
    volume = 4/3*math.pi()*x*y*z
    masse = masse_volumique * volume
    return (volume, masse)


# Exercice 2
def frequence(sentence: str) -> dict:
    wordcount = {}
    wordlist = list(sentence)
    for elem in wordlist:
        wordcount[elem] = wordlist.count(elem)
    return sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
def plus_haute_frequence(entree):
    la_plus_haute = frequence(entree)
    return la_plus_haute[0]

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
