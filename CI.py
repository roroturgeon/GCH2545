# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:42:40 2022

@author: Rosalie
"""
import numpy as np

def CI(prm):
    """Fonction qui génère les conditions initiales 
    
    Entrées:
        - prm : Objets de la classe parametres()
            - Cp : Capacité thermique massique (J/K)
            - k : Conductivié thermique (W/m*K)
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dz : Discrétisation en hauteur [m]
            - ti : Temps initial [s]
            - tf : Temps final [s]
            - dt : Discrétisation en temps [s]
            -Tair: Température de l'air [C]

    
    Sortie:
        - Vecteur (array) composée de la température initiale (t= 1 min) selon le nombre de points
    """
    dz=prm.dz
    H=prm.H
    n=prm.n
    z=np.linspace(0,H,n)
    Ti=np.zeros(n)
    Ti[:]=27.92 - 240.89*z[:] + 2982.72*z[:]**2   
    
    return Ti

def CFI(prm):
    """Condition de Dirichlet pour z = 0
    
    Entrées:
        - prm : Objets de la classe parametres()
            - Cp : Capacité thermique massique (J/K)
            - k : Conductivié thermique (W/m*K)
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dz : Discrétisation en hauteur [m]
            - ti : Temps initial [s]
            - tf : Temps final [s]
            - dt : Discrétisation en temps [s]
            -Tair: Température de l'air [C]

    
    Sortie:
        - Vecteur (array) composée de la température inférieure (z = 0 m) selon le nombre de points
    """
    dt=prm.dt
    ti=prm.ti
    tf=prm.tf
    n=prm.n
    t=np.linspace(ti,tf,int((tf-ti)/dt+1))
    Tiinf=np.zeros(int((tf-ti)/dt+1))
    Tiinf[:]=0.03175*t[:] + 26.015   
    
    return Tiinf