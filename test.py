# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:34:51 2022

@author: Rosalie
"""
import numpy as np
import matplotlib.pyplot as plt
from CI import *
from Euler_explicite import *
from Euler_implicite import *

class parametres():
    
    Cp = 1150           # Capacité thermique massique [J/(kg*K)]
    k = 1.9             # Conductivité thermique [W/(m*K)]
    n = 9               # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/(m^3)]
    h = 10              # Coefficient de convection [W/(m^2*K)]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti=60               # Temps initial [s]
    tf=180              # Temps final [s]
    dt = 0.1            # Discrétisation du temps [s]
    Tair= 22            # Température de l'air ambient [C]

prm = parametres()

T=CI(prm)
Tinf=CFI(prm)
mdfe=Euler_exp(T,Tinf, prm)
mdfi=Euler_imp(T,Tinf, prm)


z=np.linspace(0,prm.H,10)
Ti=np.zeros(10)
Ti[:]=27.92 - 240.89*z[:] + 2982.72*z[:]**2 
plt.plot(z,Ti)