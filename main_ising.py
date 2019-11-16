# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:46:09 2019

@author: Giulio
"""

import Ising
import matplotlib.pylab as plt
import numpy as np
import random as rd


ising = Ising.Ising(20)
ising.show_evolution()#this shows the graphic evolution of the system at temperature 0.1 K


Temperature    = [1.5+(0.025*i)for i in range(60)]
Magnetizations = [] #The array where all magnetization record are stored
Energies       = [] #The array where all energy records are stored
for i in range(len(Temperature)):
	
	ising = Ising.Ising(15,Temperature[i])
	ising.MontSim()#We run a Montecarlo simulation for a specific temperature
	Magnetizations.append(ising.Abs_Tot_Magn())#we fill the Magnetizations array
	Energies.append(np.abs(ising.Tot_Energy()))#We fill the Energies array
	
"""The graphics are plotted below: at first we take a glance at the magnetization
vs temperature graphic from which we can roughly harvest an estimation for Tc.
The same can be done for the energy-temperature relationship."""
plt.scatter(Temperature,Magnetizations)
plt.title("Magnetization vs Temperature")
plt.xlabel("Temperature(K)")
plt.ylabel("Absolute Magnetization(Tesla)")
plt.savefig('Magnetization_vs_Temperature.png')
plt.close()
plt.scatter(Temperature,Energies)
plt.title('Energy vs Temperature')
plt.xlabel('Temperature(K)')
plt.ylabel('Energy')
plt.savefig('Energy_vs_Temperature.png')
plt.close()