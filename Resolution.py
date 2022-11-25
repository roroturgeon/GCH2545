# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:47:33 2022

@author: dessi
"""
import numpy as np
from Fonctions import *
from CI import *
from CFI import *

"""Résolution numérique de l'équation"""

"""Définition des paramètres"""

class parametres():
    Cp = 1000          # Capacité thermique massique [J/(kg*K)]
    k = 1.9            # Conductivité thermique 
    n = 3               # Nombre de noeuds
    rho = 1.703*10**3   # Masse volumique [kg/m^3]
    h = 10           # Coefficient de convection [W/m^2*K]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)         # Discrétisation dans l'espace [m]
    ti=60               # Temps initial [s]
    tf=180               # Temps final[s]
    dt = 0.1         # Discrétisation en temps [s]
    Tair= 22              # Température de l'air [C]
    
"""Appel des conditions initiales"""
T_i = CI(parametres())

"""Résolution numérique avec la méthode d'Euler explicite"""
T_f_exp = Euler_exp(T_i,parametres())

"""Résolution numérique avec la méthode d'Euler implicite"""
T_f_imp = Euler_imp(T_i,parametres())