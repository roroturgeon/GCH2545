# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:00:48 2022

@author: Rosalie
"""
import numpy as np
import matplotlib.pyplot as plt
from CI import *
from Euler_explicite import *
from Euler_implicite import *


class parametres():

    Cp = 1.07*10**(-3)           # Capacité thermique massique [J/(kg*K)]
    k = 1.07**2             # Conductivité thermique [W/(m*K)]
    n = 5                # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/(m^3)]
    h = 0              # Coefficient de convection [W/(m^2*K)]
    H = 1           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti = 0               # Temps initial [s]
    tf = 0.1              # Temps final [s]
    dt = 0.1*dz**2          # Discrétisation du temps [s]
    Tair = 0            # Température de l'air ambient [C]


prm = parametres()

class parametres2():

    Cp = 1.07*10**(-3)           # Capacité thermique massique [J/(kg*K)]
    k = 1.07**2             # Conductivité thermique [W/(m*K)]
    n = 10               # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/(m^3)]
    h = 0              # Coefficient de convection [W/(m^2*K)]
    H = 1           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti = 0               # Temps initial [s]
    tf = 0.1              # Temps final [s]
    dt = 0.1*dz**2          # Discrétisation du temps [s]
    Tair = 0            # Température de l'air ambient [C]


prm2 = parametres2()

class parametres3():

    Cp = 1.07*10**(-3)           # Capacité thermique massique [J/(kg*K)]
    k = 1.07**2             # Conductivité thermique [W/(m*K)]
    n = 20               # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/(m^3)]
    h = 0              # Coefficient de convection [W/(m^2*K)]
    H = 1           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti = 0               # Temps initial [s]
    tf = 0.1              # Temps final [s]
    dt = 0.1*dz**2          # Discrétisation du temps [s]
    Tair = 0            # Température de l'air ambient [C]


prm3 = parametres3()

N=np.array([5, 10, 20])

T = np.zeros(prm.n)
Tinf = np.zeros(int((prm.tf-prm.ti)/prm.dt+1))+50
pos = np.linspace(0, prm.H, prm.n)
T2 = np.zeros(prm2.n)
Tinf2 = np.zeros(int((prm2.tf-prm2.ti)/prm2.dt+1))+50
pos2 = np.linspace(0, prm2.H, prm2.n)
T3 = np.zeros(prm3.n)
Tinf3 = np.zeros(int((prm3.tf-prm3.ti)/prm3.dt+1))+50
pos3 = np.linspace(0, prm3.H, prm3.n)

mdfe = Euler_exp(T, Tinf, prm) 
mdfe2 = Euler_exp(T2, Tinf2, prm2) 
mdfe3 = Euler_exp(T3, Tinf3, prm3) 

plt.plot(pos, mdfe[-1, :], label='5') 
plt.plot(pos2, mdfe2[-1, :], label='n=10') 
plt.plot(pos3, mdfe3[-1, :], label='n=20')  
plt.ylabel('Température [C]')
plt.xlabel('Position [m]')
plt.legend()
plt.savefig('Verif_graphe', dpi=500)


# for i in range(len(N)):
#     setattr(prm, "n", N[i])
#     print(prm.n)
#     T = np.zeros(prm.n)
#     Tinf = np.zeros(int((prm.tf-prm.ti)/prm.dt+1))+50
#     pos = np.linspace(0, prm.H, prm.n)
#     mdfe = Euler_exp(T, Tinf, prm)
#     print(mdfe[-1, :])
#     plt.plot(pos, mdfe[-1,:])


