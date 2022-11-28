# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:57:27 2022

@author: dessi
"""

import numpy as np

"""Méthode d'Euler explicite"""
def Euler_exp(T,prm):
    """
    Entrées:
        - T : Vecteur (array) des conditions initiales à chaque noeud
              (incluant les condition aux frontières)
        - prm : Objets de la classe parametres()
            - Cp : Capacité thermique (J/K)
            - k : Conductivié thermique (W/m*K)
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dt : Discrétisation en temps [s]
            - dz : Discrétisation en hauteur [m]
            - ti : Temps initial [s]
            - tf : Temps final [s]
            - Tair : Température de l'air [C]
    
    Sortie:
        - Vecteur (array) composée de la température final à chaque noeud
    """
    """Création des vecteurs"""
    T_t = T
    T_exp = T
    T_tdt = np.zeros(prm.n)
    
    """Boucle contenant l'équation de récurence de la méthode d'Euler explicite"""
    t = prm.ti
    while t < prm.tf:
        
        "Premier élément du vecteur T_tdt varie linéairement en fonction du temps "
        T_tdt[0]=0.03175*t+26.015
        
        for i in range(1,prm.n-1):
            T_tdt[i]= T_t[i] +((prm.dt*prm.k)/(prm.rho*prm.Cp*prm.dz**2))*(T_t[i+1]-2*T_t[i]+T_t[i-1])
        
        T_tdt[-1]=(1/(3+((2*prm.dz*prm.h)/prm.k)))*(4*np.copy(T_tdt[prm.n-2])-np.copy(T_tdt[prm.n-3])+((2*prm.h*prm.dz)/prm.k)*prm.Tair)
        
        t=t+prm.dt
        
        T_t= T_tdt
        
        T_exp=np.vstack((T_exp,T_t))
        
    return T_exp


"""Méthode d'Euler implicite"""
def Euler_imp(T,prm):
    """ 
    Entrées:
        - T : Vecteur (array) des conditions initiales à chaque noeud 
              (incluant les conditions aux frontières)
        - prm : Objet class parametres()
            - Cp :Capacité thermique (J/K)
            - k :Conductivié thermique (W/m*K)
            - n : Nombre de points [-]
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dz : Discrétisation en espace [m]
            - dt : Discrétisation en temps [s]
            - ti : Temps initial [s]
            - tf : Temps final [s]
            - Tair : Température de l'air [C]

    Sortie:
        - Vecteur (array) composée de la température finale à chaque noeud
        """
        
    "Initialisation des matrices"
    A=np.zeros([prm.n, prm.n])
    b=np.zeros(prm.n)

   
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
    Tdt=np.copy(T)
    T=np.copy(T)

    while t<prm.tf:
        "Condition frontière dépendante du temps"
        b[0]=0.03175*t+26.02
        for i in range(1, prm.n-1):
            b[i]=Tdt[i]
        Tdt=np.linalg.solve(A,b)
        t=t+prm.dt
        T=np.vstack((T, Tdt))

    return T