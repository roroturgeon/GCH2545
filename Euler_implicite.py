# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:29:19 2022

@author: Rosalie
"""

import numpy as np

def Euler_imp(T, Ti, prm):
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
            -Tair : Température de l'air [C]

    Sortie:
        - Vecteur (array) contenant les valeurs numériques du résidu
        """
        
  A=np.zeros([prm.n, prm.n])
  b=np.zeros(prm.n)
  r=np.linspace(prm.Ri, prm.Re, prm.n)
   
   
  "Condition Dirichlet à gauche"
  A[0,0]=1
  b[0]=prm.Tr
 
  "Méthode arrière ordre 2 à droite"
  A[-1,-3]=prm.K/(2*prm.h*prm.dz)
  A[-1,-2]=-2*prm.K/(prm.h*prm.dz)
  A[-1,-1]=1+3*prm.k/(2*prm.h*prm.dz)
  b[-1]=prm.Tair
   
  for i in range(1, prm.n-1):
      A[i,i]=-2
      A[i,i-1]=-prm.dr/(2*r[i])+1
      A[i,i+1]=prm.dr/(2*r[i])+1
      b[i]=0
  
  T=np.linalg.solve(A,b)


  return r, T
        
    
