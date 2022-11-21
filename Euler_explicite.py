# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:27:40 2022

@author: Rosalie
"""

import numpy as np

def mdf_exp(T,prm,tf):
    """Fonction 
    
    Entrées:
        - T : Vecteur (array) des conditions initiales à chaque noeud
              (incluant la condition à la frontière)
        - prm : Objet class parametres()
            -Cp :Capacité thermique (J/K)
            -K :Conductivié thermique (W/m*K)
            - n : Nombre de points [-]
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dz : Discrétisation en espace [m]
            - dt : Discrétisation en temps [s]

        - tf : temps de simulation [s]
    
    Sortie:
        - Vecteur (array) composée de la concentration en CO selon la position [mol/L]
            à la fin du temps de simulation
    """

    t=0
    Cp=prm.Cp
    K=prm.K
    rho=prm.rho
    dz=prm.dz
    dt=prm.dt
    n=prm.n
    h=prm.h
    T_tdt=np.zeros(n)
    T_t=np.copy(T)
    while t<tf:
        T_tdt[0]=np.copy(T[0])
        for i in range(1,n-1):
            T_tdt[i]=np.copy(T_t[i])+((dt*K)/(rho*Cp*dz**2))*(T_t[i+1]-2*T_t[i]+T_t[i-1])
        T_tdt[-1]=(1/(3+((2*dz*h)/K)))*(4*np.copy(T_tdt[n-2])-1*np.copy(T_tdt[n-3]))
        t=t+dt
        T_t=np.copy(T_tdt)
        
        
    
    return T_t