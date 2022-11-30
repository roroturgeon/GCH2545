# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:29:19 2022

@author: Rosalie
"""

import numpy as np

def Euler_imp(Ti,Tinf, prm):
    """Fonction 
    
    Entrées:
        - T : Vecteur (array) des conditions initiales à chaque noeud
        - T : Vecteur (array) des conditions frontières à chaque noeud
        - prm : Objet class parametres()
            -Cp :Capacité thermique massique (J/K)
            -K :Conductivié thermique (W/m*K)
            - n : Nombre de points [-]
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dt : Discrétisation en temps [s]
            - ti : Temps initial [s]
            - tf : Temps final [s]
            - dz : Discrétisation en espace [m]
            -Tair : Température de l'air [C]

    Sortie:
        - Vecteur (array) contenant les valeurs numériques du résidu
        """
        
    "Initialisation des matrices"
    A=np.zeros([prm.n, prm.n])
    b=np.zeros(prm.n)
    j=0

   
    "Condition Dirichlet à gauche"
    
    A[0,0]=1
 
    "Méthode arrière ordre 2 à droite"
    
    A[-1,-3]=prm.k/(2*prm.h*prm.dz)
    A[-1,-2]=-2*prm.k/(prm.h*prm.dz)
    A[-1,-1]=1+3*prm.k/(2*prm.h*prm.dz)
    b[-1]=prm.Tair
    
    "Construction matrice"
    for i in range(1, prm.n-1):
       A[i,i]=1+2*prm.k*prm.dt/(prm.rho*prm.Cp*prm.dz**2)
       A[i,i-1]=-prm.k*prm.dt/(prm.rho*prm.Cp*prm.dz**2)
       A[i,i+1]=-prm.k*prm.dt/(prm.rho*prm.Cp*prm.dz**2)


    
    "Résolution et termes du vecteur b dépendant du temps "
    t=prm.ti
    Tdt=np.copy(Ti)
    T=np.copy(Ti)

    while t<prm.tf:
        "Condition frontière dépendante du temps"
        b[0]=Tinf[j]
        for i in range(1, prm.n-1):
            b[i]=Tdt[i]
        Tdt=np.linalg.solve(A,b)
        t=t+prm.dt
        T=np.vstack((T, Tdt))
        j=j+1
    return T
        
    
