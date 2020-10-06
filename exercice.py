#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math, turtle


# TODO: Définissez vos fonction ici
def ellipsoide(demi_axes, masse_volumique):
    x, *y, z = demi_axes
    volume = 4/3*math.pi()*x*y*z
    masse = masse_volumique * volume
    return (volume, masse)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
