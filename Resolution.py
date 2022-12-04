# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:47:33 2022

@author: dessi
"""
import numpy as np
import matplotlib.pyplot as plt
from Euler_explicite import *
from Euler_implicite import *
from CI import *

"""Résolution numérique de l'équation"""

"""Définition des paramètres"""

class parametres():
    Cp = 1117.24          # Capacité thermique massique [J/(kg*K)]
    k = 0.9            # Conductivité thermique 
    n = 9               # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/m^3]
    h = 10           # Coefficient de convection [W/m^2*K]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)         # Discrétisation dans l'espace [m]
    ti=60               # Temps initial [s]
    tf=180               # Temps final[s]
    dt = 0.1         # Discrétisation en temps [s]
    Tair= 22              # Température de l'air [C]

prm = parametres()
"""Appel des conditions initiales"""
T_i = CI(prm)
T_f = CFI(prm)

"""Résolution numérique avec la méthode d'Euler explicite"""
T_f_exp = Euler_exp(T_i,T_f,prm)

"""Résolution numérique avec la méthode d'Euler implicite"""
T_f_imp = Euler_imp(T_i,T_f,prm)

"""Création de l'espace dt explicite"""
t = np.linspace(prm.ti,prm.tf,len(T_f_exp))

"""Figure de la Résolution numérique avec la méthode d'Euler explicite"""
fig,ax=plt.subplots(2,3)

ax[0,0].plot(t,T_f_exp[:,0])
ax[0,0].set_title('Méthode d\'Euler explicite ; z = 0')
ax[0,0].set_ylabel('Température (C)')
ax[0,0].set_xlabel('Temps (s)')
ax[0,0].plot(t[0],27.92,'rx')
ax[0,0].plot(t[-1],31.73,'rx')

ax[0,1].plot(t,T_f_exp[:,4])
ax[0,1].set_title('Méthode d\'Euler explicite ; z = 22.5 mm')
ax[0,1].set_ylabel('Température (C)')
ax[0,1].set_xlabel('Temps (s)')
ax[0,1].plot(t[0],24.01,'rx')
ax[0,1].plot(t[-1],25.19,'rx')

ax[0,2].plot(t,T_f_exp[:,-1])
ax[0,2].set_title('Méthode d\'Euler explicite ; z = 45 mm')
ax[0,2].set_ylabel('Température (C)')
ax[0,2].set_xlabel('Temps (s)')
ax[0,2].plot(t[0],23.12,'rx')
ax[0,2].plot(t[-1],23.69,'rx')

ax[1,0].plot(t,T_f_imp[:,0])
ax[1,0].set_title('Méthode d\'Euler implicite ; z = 0')
ax[1,0].set_ylabel('Température (C)')
ax[1,0].set_xlabel('Temps (s)')
ax[1,0].plot(t[0],27.92,'rx')
ax[1,0].plot(t[-1],31.73,'rx')

ax[1,1].plot(t,T_f_imp[:,4])
ax[1,1].set_title('Méthode d\'Euler implicite ; z = 22.5 mm')
ax[1,1].set_ylabel('Température (C)')
ax[1,1].set_xlabel('Temps (s)')
ax[1,1].plot(t[0],24.01,'rx')
ax[1,1].plot(t[-1],25.19,'rx')

ax[1,2].plot(t,T_f_imp[:,-1])
ax[1,2].set_title('Méthode d\'Euler implicite ; z = 45 mm')
ax[1,2].set_ylabel('Température (C)')
ax[1,2].set_xlabel('Temps (s)')
ax[1,2].plot(t[0],23.12,'rx')
ax[1,2].plot(t[-1],23.69,'rx')