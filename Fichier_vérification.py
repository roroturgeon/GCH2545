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

###Vérification que les droites et la fonction quadratique passent bien par les points expériementaux
class parametres4():
    
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

prm4 = parametres4()

###Condition initiale quadratique
z=np.linspace(0,prm4.H,prm4.n)
Ti=np.zeros(prm4.n)
Ti[:]=27.92 - 240.89*z[:] + 2982.72*z[:]**2 
plt.plot(z,Ti,label="CI")
plt.axhline(27.92,color='k',linestyle='--')
plt.axhline(24.01,color='r',linestyle='--')
plt.axhline(23.12,color='y',linestyle='--')
plt.axvline(0,color='k',linestyle='--')
plt.axvline(0.0225,color='r',linestyle='--')
plt.axvline(0.045,color='y',linestyle='--')
plt.legend()
plt.xlabel('Position (m)')
plt.ylabel('Température')
plt.title('Température à 1 minute en fonction de la hauteur')
plt.savefig('CI', dpi=500)
plt.show()

###Condition frontière inférieure (linéaire)
t=np.linspace(prm4.ti,prm4.tf,int((prm4.tf-prm4.ti)/prm4.dt+1))
Tiinf=np.zeros(int((prm4.tf-prm4.ti)/prm4.dt+1))
Tiinf[:]=0.03175*t[:] + 26.015 
plt.plot(t,Tiinf,label="CFI")
plt.axhline(27.92,color='k',linestyle='--')
plt.axhline(31.73,color='r',linestyle='--')
plt.axvline(60,color='k',linestyle='--')
plt.axvline(180,color='r',linestyle='--')
plt.legend()
plt.xlabel('Temps (s)')
plt.ylabel('Température')
plt.title('Température à z=0 en fonction du temps')
plt.savefig('CFI', dpi=500)



###Vérification graphique avec une exemple de notes de cours.
###Profil de température dans une tige 1D en régime transitoire.

###Initialisation des paramètres 
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

###Intialisation des conditions frontières
T = np.zeros(prm.n)
Tinf = np.zeros(int((prm.tf-prm.ti)/prm.dt+1))+50
pos = np.linspace(0, prm.H, prm.n)
T2 = np.zeros(prm2.n)
Tinf2 = np.zeros(int((prm2.tf-prm2.ti)/prm2.dt+1))+50
pos2 = np.linspace(0, prm2.H, prm2.n)
T3 = np.zeros(prm3.n)
Tinf3 = np.zeros(int((prm3.tf-prm3.ti)/prm3.dt+1))+50
pos3 = np.linspace(0, prm3.H, prm3.n)

###Utilisation de nos fonctions pour faire le calcul
mdfe = Euler_exp(T, Tinf, prm) 
mdfe2 = Euler_exp(T2, Tinf2, prm2) 
mdfe3 = Euler_exp(T3, Tinf3, prm3) 

###Graphique pour les différents noeuds
plt.show()
plt.plot(pos, mdfe[-1, :],marker='D', label='5') 
plt.plot(pos2, mdfe2[-1, :],marker='o', label='n=10') 
plt.plot(pos3, mdfe3[-1, :], label='n=20')  
plt.ylabel('Température [C]')
plt.xlabel('Position [m]')
plt.title('Profil de température en fonction du nombre de noeuds')
plt.legend()
plt.savefig('Verif_graphe', dpi=500)






