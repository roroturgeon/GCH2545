# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:29:41 2022

@author: Rosalie
"""

import numpy as np
try:
    from CI import *
except:
    pass

class parametres():
    Cp = 0          # Longueur du catalyseur [cm]
    K = 0           # Nombre de noeuds
    n = 3
    rho = 1.703*10**3   # Coefficient de diffusion du CO [cm^2/s]
    h = 10           # Vitesse du gaz qui traverse le catalyseur [cm/s]
    H = 0.045           # Constante de réaction [L/(mol*s)]
    dz = H/(n-1)         # Discrétisation dans l'espace [cm]
    dt = 0.01          # Discrétisation en temps [s]

prm = parametres()

Ti=CI(prm)