# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:28:47 2022

@author: Rosalie
"""

import numpy as np

def res(T, Ti, prm):
    """Fonction 
    
    Entrées:
        - T : Vecteur (array) de température
        -Ti : Vecteur des conditions initiales 
        - prm : Objet class parametres()
            -Cp :Capacité thermique (J/K)
            -K :Conductivié thermique (W/m*K)
            - n : Nombre de points [-]
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dz : Discrétisation en espace [m]
            - dt : Discrétisation en temps [s]
            - ti : Temps initial [s]
            - tf : Temps final [s]

    Sortie:
        - Vecteur (array) contenant les valeurs numériques du résidu
    """

    R=np.zeros(len(T))
    
    for i in range(1,len(T)-1):
        R[i]=Ti[i]+T[i+1]*(prm.dt*prm.K/(prm.rho*prm.Cp))-T[i]*(1+2*prm.dt*prm.K/(prm.rho*prm.Cp*prm.dz**2))+T[i-1]*(prm.K*prm.dt/(prm.rho*prm.Cp*prm.dz**2))
         
    R[0]=Ti[i]+T[i]*(-1-3*prm.K*prm.dt/(2*prm.rho*prm.Cp*prm.dz))+T[i+1]*(4*prm.dt*prm.K/(2*prm.rho*prm.Cp*prm.dz))+T[i+2]*(-prm.K*prm.dt/(2*prm.rho*prm.Cp*prm.dz))
    R[-1]=Ti[i]+T[i]*(-1+3*prm.K*prm.dt/(2*prm.rho*prm.Cp*prm.dz))+T[i-1]*(-2*prm.K*prm.dt/(prm.rho*prm.Cp*prm.dz))+T[i-2]*(prm.K*prm.dt/(2*prm.rho*prm.Cp*prm.dz))
    
    return R

def newton_numerique(T,tol,prm):
    """Fonction résolvant le système d'équations avec la méthode de Newton et un jacobien numérique
    
    Entrées:
        - T : Vecteur (array) de température
        - tol : critère d'arrêt
        - prm : Objet class parametres()
            -Cp :Capacité thermique (J/K)
            -K :Conductivié thermique (W/m*K)
            - n : Nombre de points [-]
            - rho : Masse volumique [kg/m^3]
            - h : Coefficient de convection [W/m^2*K]
            - H : Hauteur de la pâte [m]
            - dz : Discrétisation en espace [m]
            - dt : Discrétisation en temps [s]
            - ti : Temps initial [s]
            - tf : Temps final [s]
    
    Sortie:
        - Vecteur (array) contenant les solutions
    """
    
    deltaz=np.ones(len(T))
    Ti=np.copy(T)
    J=np.zeros([len(T), len(T)])
    n=0
    t=prm.ti
    
    while t<prm.tf:
        T_tdt=np.copy(T)
        while np.linalg.norm(deltaz)>tol:
            R=res(T, Ti, prm)
            for i in range(len(T)):
                pert=np.zeros(len(T))
                pert[i]=T[i]*tol
                zp=np.copy(T)+pert
                zpi=np.copy(zp)
                Rp=res(zp, prm)
                J[:,i]=(Rp-R)/(T[i]*tol)
            deltaT=np.linalg.solve(J, -R)  
            T=T+np.array(deltaT)
            n=n+1
        t=t+prm.dt
        
    return 