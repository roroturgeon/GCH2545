# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:00:48 2022

@author: Rosalie
"""
import numpy as np
from CI import *
from Euler_explicite import *
from Euler_implicite import *


class parametres():
    
    Cp = 1.07*10**(-3)           # Capacité thermique massique [J/(kg*K)]
    k = 1.07**2             # Conductivité thermique [W/(m*K)]
    n = 5               # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/(m^3)]
    h = 0              # Coefficient de convection [W/(m^2*K)]
    H = 1           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti=0               # Temps initial [s]
    tf=0.1              # Temps final [s]
    dt = 0.01            # Discrétisation du temps [s]
    Tair= 0            # Température de l'air ambiant [C]

prm = parametres()

T=np.zeros(prm.n)+10
Tinf=np.zeros(int((prm.tf-prm.ti)/prm.dt+1))+50
mdfe=Euler_exp(T,Tinf, prm)





