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
    n = 3               # Nombre de noeuds
    rho = 1.07*10**3   # Masse volumique [kg/(m^3)]
    h = 10              # Coefficient de convection [W/(m^2*K)]
    H = 0.045           # Hauteur de la pâte [m]
    dz = H/(n-1)        # Discrétisation de l'espace [m]
    ti=60               # Temps initial [s]
    tf=180              # Temps final [s]
    dt = 0.1            # Discrétisation du temps [s]
    Tair= 22            # Température de l'air ambient [C]

prm = parametres()

"""Génération des espaces-solutions pour la méthode d'Euler explicite et la méthode d'Euler implicite"""
m = 5
espace_cp = np.linspace(1000,1200,m)
espace_k = np.linspace(0.9,1.9,m)

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

plt.plot(espace_cp,espace_solution_exp[:,0], label='k = 0.90')
plt.plot(espace_cp,espace_solution_exp[:,1], label='k = 1.15')
plt.plot(espace_cp,espace_solution_exp[:,2], label='k = 1.30')
plt.plot(espace_cp,espace_solution_exp[:,3], label='k = 1.65')
plt.plot(espace_cp,espace_solution_exp[:,4], label='k = 1.90')
plt.title('Évolution de la fonction - objectif en fonction de Cp pour \n un paramètre k donné selon la méthode d\'Euler explicite')
plt.xlabel('Capacité thermique massique (Cp)')
plt.ylabel('Fonction-objectif')
plt.legend(loc = 0)

"""Création du graphique décrivant l'évolution des couples Cp-k pour la méthode d'Euler implicite"""
plt.figure(2)

plt.plot(espace_cp,espace_solution_imp[:,0], label='k = 0.90')
plt.plot(espace_cp,espace_solution_imp[:,1], label='k = 1.15')
plt.plot(espace_cp,espace_solution_imp[:,2], label='k = 1.30')
plt.plot(espace_cp,espace_solution_imp[:,3], label='k = 1.65')
plt.plot(espace_cp,espace_solution_imp[:,4], label='k = 1.90')
plt.title('Évolution de la fonction - objectif en fonction de Cp pour \n un paramètre k donné selon la méthode d\'Euler implicite')
plt.xlabel('Capacité thermique massique (Cp)')
plt.ylabel('Fonction-objectif')
plt.legend(loc = 0)
