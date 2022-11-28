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

# T=np.zeros(prm.n)+10
# Tinf=np.zeros(int((prm.tf-prm.ti)/prm.dt+1))+50
# mdfe=Euler_exp(T,Tinf, prm)



###Condition initiale quadratique
z=np.linspace(0,prm.H,prm.n)
Ti=np.zeros(prm.n)
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

###Condition frontière inférieure
t=np.linspace(prm.ti,prm.tf,int((prm.tf-prm.ti)/prm.dt+1))
Tiinf=np.zeros(int((prm.tf-prm.ti)/prm.dt+1))
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





