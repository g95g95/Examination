# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:46:09 2019

@author: Giulio
"""

import Ising
import matplotlib.pylab as plt
import numpy as np
import random as rd

#ising = Ising.Ising(15)
#ising.MontSim()
#ising.print_lattice_GUI() Something that 'll allow to save different pictures
#of the lattice
Temperature    = [0.1+(0.05*i)for i in range(30)]
Magnetizations = [] 
Energies       = []
for i in range(len(Temperature)):
	
	ising = Ising.Ising(15,Temperature[i])
	ising.MontSim()
	Magnetizations.append(ising.Abs_Tot_Magn())
	Energies.append(ising.Tot_Energy())
	


plt.scatter(Temperature,Magnetizations)
plt.title("Magnetization vs Temperature")
plt.xlabel("Temperature(K)")
plt.ylabel("Absolute Magnetization(Tesla)")
plt.savefig('Magnetization_vs_Temperature.png')
plt.scatter(Temperature,Energies)
plt.title('Energy vs Temperature')
plt.xlabel('Temperature(K)')
plt.ylabel('Energy')
plt.savefig('Energy_vs_Temperature.png')



