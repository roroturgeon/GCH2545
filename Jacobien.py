# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:29:08 2022

@author: Rosalie
"""

import numpy as np

def mdf_exp(c,prm,tf):
    """Fonction 
    
    Entrées:
        - c : Vecteur (array) des conditions initiales à chaque noeud
              (incluant la condition à la frontière)
        - prm : Objet class parametres()
            -Lx :Longueur (cm)
            -n :Nombre de noeuds
            - D : Coefficient de diffusion du CO dans le filtre [cm^2/s]
            - v : Vitesse du gaz qui traverse le catalyseur [cm/s]
            - k : Constante de réaction [L/(mol*s)]
            - dx : Discrétisation en espace [cm]
            - dt : Discrétisation en temps [s]
        - tf : temps de simulation [s]
    
    Sortie:
        - Vecteur (array) composée de la concentration en CO selon la position [mol/L]
            à la fin du temps de simulation
    """

    t=0
    D=prm.D
    v=prm.v
    k=prm.k
    dx=prm.dx
    dt=prm.dt
    n=prm.n
    c_tdt=np.zeros(n)
    c_t=np.copy(c)
    while t<tf:
        c_tdt[0]=np.copy(c[0])
        for i in range(1,n-1):
            c_tdt[i]=np.copy(c_t[i])-k*dt*np.copy(c_t[i])**2+(D*dt/(dx**2))*(np.copy(c_t[i+1])-2*np.copy(c_t[i])+np.copy(c_t[i-1]))-(v*dt/(2*dx))*(np.copy(c_t[i+1])-np.copy(c_t[i-1]))
        c_tdt[-1]=(4/3)*np.copy(c_tdt[n-2])-(1/3)*np.copy(c_tdt[n-3])
        t=t+dt
        c_t=np.copy(c_tdt)
        
        
    
    return c_t