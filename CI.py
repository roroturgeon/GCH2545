# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:42:40 2022

@author: Rosalie
"""

import numpy as np

def CI(prm):
    """Fonction 
    
    Entrées:
        - prm : Objet class parametres()
            - Cp :Capacité thermique (J/K)
            - K :Conductivié thermique (W/m*K)
            - n : Nombre de points [-]
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dz : Discrétisation en espace [m]
            - dt : Discrétisation en temps [s]

    
    Sortie:
        - Vecteur (array) composée de la température initiale (t= 1min) selon le nombre de points
    """
    dz=prm.dz
    H=prm.H
    n=prm.n
    z=np.linspace(0,H,n)
    Ti=np.zeros(n)
    Ti[:]=27.92-240.89*z[:]+2982.72*z[:]**2   
    
    return Ti