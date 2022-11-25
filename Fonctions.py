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
    """Assignation des paramètres"""
    t=prm.ti
    tf=prm.tf
    Cp=prm.Cp
    K=prm.k
    rho=prm.rho
    dz=prm.dz
    dt=prm.dt
    n=prm.n
    h=prm.h
    T_tdt=np.zeros(n)
    T_t=np.copy(T)
    Te=np.copy(T)
    
    """Boucle contenant l'équation de récurence de la méthode d'Euler explicite"""
    while t<tf:
        
        "Premier élément du vecteur T_tdt varie linéairement en fonction du temps "
        T_tdt[0]=0.03175*t+26.015
        
        for i in range(1,n-1):
            T_tdt[i]=np.copy(T_t[i])+((dt*K)/(rho*Cp*dz**2))*(T_t[i+1]-2*T_t[i]+T_t[i-1])
        
        T_tdt[-1]=(1/(3+((2*dz*h)/K)))*(4*np.copy(T_tdt[n-2])-np.copy(T_tdt[n-3])+((2*h*dz)/K)*prm.Tair)
        
        t=t+dt
        
        T_t=np.copy(T_tdt)
        
        Te=np.vstack((Te,np.copy(T_t)))
        
    return Te


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