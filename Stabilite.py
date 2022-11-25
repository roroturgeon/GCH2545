# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:30:05 2022

@author: Rosalie
"""

import numpy as np
import matplotlib.pyplot as plt
from CI import *
from Fonctions import *

"""L'analyse de stabilité ne s'applique qu'à la méthode d'Euler explicite"""

"""Définition des paramètres du problème"""
class parametres():
    
    Cp = 1000           # Capacité thermique massique [J/(kg*K)]
    k = 1.9             # Conductivité thermique [W/(m*K)]
    
    n = 3               # Nombre de noeuds
    rho = 1.703*10**3   # Masse volumique [kg/(m^3)]
    h = 10              # Coefficient de convection [W/(m^2*K)]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti = 60               # Temps initial [s]
    tf = 180              # Temps final [s]
    dt = 0.1            # Discrétisation du temps [s]
    Tair = 22            # Température de l'air ambient [C]

prm = parametres()
"""Calcul du critère de stabilité"""
critere_t = (prm.rho*prm.Cp*prm.dz**2)/prm.k

"""Création de l'espace de valeurs de dt"""
valeur_dt = 100
nombre_valeur_dt = 100
espace_critere_dt = np.linspace(critere_t - valeur_dt, critere_t + valeur_dt, nombre_valeur_dt)

"""Création de l'espace des valeurs de dz"""
valeur_dz = 5
nombre_valeur_dz = 10
espace_critère_dz = np.linspace(prm.dz/valeur_dz, prm.dz*valeur_dz, nombre_valeur_dz)

"""Calcul de l'évolution du profil de température pour chaque méthode"""
T_i=CI(prm)
critere_exp = np.zeros(nombre_valeur_dt)
for i in range(0,nombre_valeur_dt):
    prm.dt = espace_critere_dt[i]
    critere_exp_1 = Euler_exp(T_i,prm)
    critere_exp = np.vstack([critere_exp, critere_exp_1])