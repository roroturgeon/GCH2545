# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:30:05 2022

@author: Rosalie
"""

import numpy as np
import matplotlib.pyplot as plt
from CI import *
from Euler_explicite import *
from Euler_implicite import *

"""Définition des paramètres du problème"""
class parametres():
    
    Cp = 1025        # Capacité thermique massique [J/(kg*K)]
    k = 1.525             # Conductivité thermique [W/(m*K)]
    n = 9               # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/(m^3)]
    h = 10              # Coefficient de convection [W/(m^2*K)]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti = 60             #r Temps initial [s]
    tf = 180            # Temps final [s]
    dt = 1            # Discrétisation du temps [s]
    Tair = 22           # Température de l'air ambient [C]

prm = parametres()

"""Méthode d'Euler explicite"""

"""Création de l'espace des valeurs de dz"""
espace_dz = np.linspace(0,prm.H,prm.n)

"""Création de l'espace des valeurs de dt"""
espace_dt = np.linspace(0,prm.ti,prm.n)

"""Création de l'espace des valeurs de stabilité"""
espace_stabilite = np.zeros([len(espace_dt), len(espace_dz)])
for i in range(0,len(espace_dt)):
    for j in range(0,len(espace_dz)):
        espace_stabilite[i,j] = (2*espace_dt[i]*prm.k)/(prm.rho*prm.Cp*espace_dz[j]**2)
        
"""Plan à z = 1"""
plan_z_1 = np.ones([len(espace_dt),len(espace_dz)])
"""Figure qui représente les sections stables et instables de la méthode d'Euler explicite"""
plt.figure(3)
ax = plt.axes(projection='3d')
X,Y=np.meshgrid(espace_dz,espace_dt)
ax.plot_surface(X,Y,espace_stabilite,cmap='viridis')
ax.plot_surface(X,Y,plan_z_1)
ax.set_title('Stabilité de la méthode d\'Euler explicite')
ax.set_ylabel('Temps discrétisé')
ax.set_xlabel('Espace discrétisé')
ax.set_zlabel('Valeur de stabilité')

