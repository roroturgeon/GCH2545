# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:29:41 2022

@author: Rosalie
"""
import numpy as np
import matplotlib.pyplot as plt
from Fonction_solution import *

"""Définition des paramètres du problème"""
class parametres():
    
    Cp = 1000           # Capacité thermique massique [J/(kg*K)]
    k = 0.9             # Conductivité thermique [W/(m*K)]   
    n = 11               # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/(m^3)]
    h = 10              # Coefficient de convection [W/(m^2*K)]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti=60               # Temps initial [s]
    tf=180              # Temps final [s]
    dt = 0.1            # Discrétisation du temps [s]
    Tair= 22            # Température de l'air ambient [C]
    N = 30              # Nombre de valeurs dans les domaines de Cp et de k

prm = parametres()
"""Génération des espaces-solutions pour la méthode d'Euler explicite et la méthode d'Euler implicite"""
espace_cp = np.linspace(1000,1200,prm.N)
espace_k = np.linspace(0.9,1.9,prm.N)

espace_solution_exp = np.zeros([len(espace_cp),len(espace_k)])
espace_solution_imp = np.zeros([len(espace_cp),len(espace_k)])

"""Évaluation de la fonction-objectif pour chaque couple Cp-k""" 
for i in range(0,len(espace_cp)):
    prm.Cp = espace_cp[i]
    for j in range(0,len(espace_k)):
        prm.k = espace_k[j]
        espace_solution_exp[i,j] = fonction_solution_exp(prm)
        espace_solution_imp[i,j] = fonction_solution_imp(prm)
        
"""Création du graphique décrivant l'évolution des couples Cp-k pour la méthode d'Euler explicite"""
plt.figure(1)

ax = plt.axes(projection='3d')
X,Y = np.meshgrid(espace_k,espace_cp)
ax.plot_surface(X,Y,espace_solution_exp,cmap='viridis',edgecolor='none')
ax.set_title('Fonction-objectif en fonction de Cp et de k \n avec la méthode d\'Euler explicite')
ax.set_ylabel('Capacité thermique massique (Cp)')
ax.set_xlabel('Conductivité thermique (k)')
ax.set_zlabel('Fonction-objectif')
plt.savefig("Fonction_objectif_exp.png", dpi=300)

"""Création du graphique décrivant l'évolution des couples Cp-k pour la méthode d'Euler implicite"""
plt.figure(2)

ax = plt.axes(projection='3d')
X,Y = np.meshgrid(espace_k, espace_cp)
ax.plot_surface(X,Y,espace_solution_imp, cmap='viridis', edgecolor='none')
ax.set_title('Fonction-objectif en fonction de Cp et de k \n avec la méthode d\'Euler implicite')
ax.set_ylabel('Capacité thermique massique (Cp)')
ax.set_xlabel('Conductivité thermique (k)')
ax.set_zlabel('Fonction-objectif')
plt.savefig("Fonction_objectif_imp.png", dpi=300)

"""Affichage des valeurs minimales"""
E = espace_solution_exp[0,0]
ind_1_exp = 0
ind_2_exp = 0
for i in range(0,len(espace_cp)):
    for j in range(0,len(espace_k)):
        if espace_solution_exp[i,j] < E:
            E = espace_solution_exp[i,j]
            ind_1_exp = i
            ind_2_exp = j
            
I = espace_solution_imp[0,0]
ind_1_imp = 0
ind_2_imp = 0
for i in range(0,len(espace_cp)):
    for j in range(0,len(espace_k)):
        if espace_solution_imp[i,j] < I:
            I = espace_solution_imp[i,j]
            ind_1_imp = i
            ind_2_imp = j

Cp_exp = espace_cp[ind_1_exp]
k_exp = espace_k[ind_2_exp]

Cp_imp = espace_cp[ind_1_imp]
k_imp = espace_k[ind_2_imp]

print("Pour la méthode d'Euler explicite, la capacité thermique massique est de",Cp_exp,"J/(kg*K) et la conductivité thermique est de",k_exp,"W/(m*K).")
print("Pour la méthode d'euler implicite, la capacité thermique massique est de",Cp_imp,"J/(kg*k) et la conductivité thermique est de",k_imp,"W/(m*K).")