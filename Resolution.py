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
    Cp = 1021          # Capacité thermique massique [J/(kg*K)]
    k = 1.52            # Conductivité thermique 
    n = 90         # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/m^3]
    h = 10           # Coefficient de convection [W/m^2*K]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)         # Discrétisation dans l'espace [m]
    ti=60               # Temps initial [s]
    tf=180               # Temps final[s]
    dt = 10         # Discrétisation en temps [s]
    Tair= 22              # Température de l'air [C]

prm = parametres()
a = int(prm.n / 2)
"""Appel des conditions initiales"""
T_i = CI(prm)
T_f = CFI(prm)

"""Résolution numérique avec la méthode d'Euler explicite"""
T_f_exp = Euler_exp(T_i,T_f,prm)

"""Résolution numérique avec la méthode d'Euler implicite"""
T_f_imp = Euler_imp(T_i,T_f,prm)

"""Création de l'espace dt"""
t = np.linspace(prm.ti,prm.tf,len(T_f_exp))

"""Création de l'espace dx"""
x = np.linspace(0,prm.H,prm.n)

"""Figure du profil de température selon chaque méthode au temps t = 3 min (n = 100 ; dt = 0.1 s)"""
fig,ax_1= plt.subplots(2)

ax_1[0].plot(x,T_f_exp[-1,:])
ax_1[0].set_title('Profil de température selon les méthodes d\'Euler \n explicite et implicite (t = 3 min)')
#x_1[0].set_xlabel('Hauteur (m)')
ax_1[0].set_ylabel('Température (C)')
ax_1[0].plot(x[0],31.73,'rx')
ax_1[0].plot(x[a],25.19,'rx')
ax_1[0].plot(x[-1],23.69,'rx')

ax_1[1].plot(x,T_f_imp[-1,:])
#x_1[1].set_title('Profil de température selon la méthode d\'Euler implicite')
ax_1[1].set_xlabel('Hauteur (m)')
ax_1[1].set_ylabel('Température (C)')
ax_1[1].plot(x[0],31.73,'rx')
ax_1[1].plot(x[a],25.19,'rx')
ax_1[1].plot(x[-1],23.69,'rx')

plt.savefig('profil_température.png', dpi=300)
