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
            - ti : Temps initial [s]
            - tf : Temps final [s]
    
    Sortie:
        - Vecteur (array) composée de la concentration en CO selon la position [mol/L]
            à la fin du temps de simulation
    """
    """Assignation des paramètres"""
    t=prm.ti
    T_t=T[1:-1]
    T_tdt=np.zeros(len(T_t))
    dz=prm.H/(len(T_t)-1)
    
    
    """Boucle contenant l'équation de récurence de la méthode d'Euler explicite"""
    while t<prm.tf:
        
        """Condition de Dirichlet"""
        T_tdt[0] = T_t[0]
        
        """Noeuds intermédiaires"""
        for i in range(1,len(T_t)-1):
            T_tdt[i] = T_t[i] + ((prm.dt*prm.k)/(prm.rho*prm.Cp*dz**2))*(T_t[i+1]-2*T_t[i]+T_t[i-1])
        
        """Condition de Robin"""
        T_tdt[-1]=((-3*prm.k/(2*prm.h*dz)*T_tdt[-2])+((-prm.k/(2*prm.h*dz))*T_tdt[-3])+(T[-1]))/(1-(2*prm.k/(prm.h*dz)))
        
        """Incrément temporel"""
        t=t+prm.dt
        
        """Vecteur au temps t+dt"""
        T_t=T_tdt
        
    return T_t