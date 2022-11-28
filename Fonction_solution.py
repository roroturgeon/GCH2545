# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:30:37 2022

@author: dessi
"""

"""Fonctions-solutions utilisées pour trouver les valeurs optimales de Cp et k"""

import numpy as np
from Euler_explicite import *
from Euler_implicite import *
from CI import *

"""Fonction-solution dans le cas explicite"""
def fonction_solution_exp(prm):
    
    T_i = CI(prm)
    T_exp = np.array([31.73, 25.19, 23.69])
    
    T_simu_explicite = Euler_exp(T_i,prm)[-1,:]
    
    f_obj_explicite = 0

    for i in range(0,len(T_simu_explicite)):
        f_obj_explicite_1 = np.abs((T_exp[i]-T_simu_explicite[i])/T_simu_explicite[i])
        f_obj_explicite = f_obj_explicite + f_obj_explicite_1
        
    return f_obj_explicite

"""Fonction-solution dans le cas implicite"""
def fonction_solution_imp(prm):
    
    T_i = CI(prm)
    T_exp = np.array([31.73, 25.19, 23.69])
    
    T_simu_implicite = Euler_imp(T_i,prm)[-1,:]
    
    f_obj_implicite = 0

    for i in range(0,len(T_simu_implicite)):
        f_obj_implicite_1 = np.abs((T_exp[i]-T_simu_implicite[i])/T_simu_implicite[i])
        f_obf_implicite = f_obj_implicite + f_obj_implicite_1
        
    return f_obj_implicite