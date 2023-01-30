# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:58:51 2023

@author: Rosalie
"""

import math
import numpy as np
import matplotlib.pyplot as plt

class parametres():
    
    n = 8        # Nombre de panneaux
    R=1         #Rayon du cylindre
prm = parametres()
X=np.zeros([prm.n+1,2])


distance=(2*np.pi/prm.n)
angle=np.linspace(np.pi+(distance/2),-np.pi+(distance/2),prm.n+1)
phi=np.zeros([prm.n,1])
phi[0]=np.pi/2
k=1
while k<=prm.n-1:
    phi[k]=phi[k-1]-((2*np.pi)/prm.n)
    if phi[k]<0:
        phi[k]=phi[k]+2*np.pi
    k=k+1
      
for i in range(prm.n+1):
    X[i,0]=prm.R*np.cos(angle[i])
    X[i,1]=prm.R*np.sin(angle[i])
Sj=np.sqrt((X[0,0]-X[1,0])**2+(X[0,1]-X[1,1])**2)

x=np.zeros([prm.n,2])
for i in range(prm.n):
    x[i,0]=(X[i,0]+X[i+1,0])/2
    x[i,1]=(X[i,1]+X[i+1,1])/2

# t=np.linspace(0,2*np.pi,1000)
# plt.plot(np.cos(t),np.sin(t))
# plt.plot(X[:,0],X[:,1])
# plt.scatter(x[:,0],x[:,1])

Iij=np.zeros([prm.n,prm.n])
for i in range(prm.n):
    for j in range(prm.n):
        if i==j:
            Iij[i,j]=np.pi
        else:
            A=-(x[i,0]-X[j,0])*np.cos(phi[j])-(x[i,1]-X[j,1])*np.sin(phi[j])
            B=(x[i,0]-X[j,0])**2+(x[i,1]-X[j,1])**2
            C=np.sin(phi[i]-phi[j])
            D=(x[i,1]-X[j,1])*np.cos(phi[i])-(x[i,0]-X[j,0])*np.sin(phi[i])
            E=np.sqrt(B-A**2)
            Iij[i,j]=(C/2)*np.log((Sj**2+2*A*Sj+B)/B)+((D-A*C)/E)*(np.arctan((Sj+A)/E)-np.arctan(A/E))
            
beta=phi+(np.pi/2)
W=-np.cos(beta)
labda=np.linalg.solve(Iij,W)

V=np.zeros([prm.n,1])
somme=0
for i in range(prm.n):
    for j in range(prm.n):
        if i==j:
            somme=somme                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        else:
            A=-(x[i,0]-X[j,0])*np.cos(phi[j])-(x[i,1]-X[j,1])*np.sin(phi[j])
            B=(x[i,0]-X[j,0])**2+(x[i,1]-X[j,1])**2
            C=np.sin(phi[i]-phi[j])
            D=(x[i,1]-X[j,1])*np.cos(phi[i])-(x[i,0]-X[j,0])*np.sin(phi[i])
            E=np.sqrt(B-A**2)
            IT=(D-A*C)/(2*E)*np.log((Sj**2+2*A*Sj+B)/B)-C*(np.arctan((Sj+A)/E)-np.arctan(A/E))
            somme=somme+labda[j]*IT
    V[i]=np.sin(beta[i])+somme
    somme=0

Cp=1-V**2
t1=np.linspace(0,2*np.pi,prm.n)

#Cp théorique
Cp_th=1-4*np.sin(beta)**2

plt.plot(t1,Cp_th, label='Théorique')
plt.plot(t1,Cp, label='analytique')
plt.scatter(t1,Cp)
plt.legend()
plt.show()
    
#Calcul     
 
force=Cp*Sj

P=0
T=0        
                              
for i in range(prm.n):
    P=P+force[i]*np.sin(beta[i])
    T=T+force[i]*np.cos(beta[i])

