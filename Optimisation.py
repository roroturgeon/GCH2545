# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:29:41 2022

@author: Rosalie
"""

import numpy as np
try:
    from CI import *
    from Euler_explicite import *
except:
    pass


class parametres():
    Cp = 1000          # Capacité thermique massique [cm]
    k = 0.9             # Conductivité thermique
    n = 3               # Nombre de noeuds
    rho = 1.703*10**3   # Masse volumique [kg/m^3]
    h = 10           # Coefficient de convection [W/m^2*K]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)         # Discrétisation dans l'espace [m]
    dt = 1          # Discrétisation en temps [s]
    ti=60               # Temps initial [s]
    tf=180               # Temps final[s]
    Tair= 22              # Température de l'air [C]

prm = parametres()


Ti=CI(prm)
T=mdf_exp(Ti,prm)

