# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:27:40 2022

@author: Rosalie
"""

import numpy as np

def mdf_exp(T,prm):
    """Fonction de la méthode d'Euler explicite
    
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
            -Tair: Température de l'air [C]
    
    Sortie:
        - Vecteur (array) composée de la concentration en CO selon la position [mol/L]
            à la fin du temps de simulation
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