# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:30:13 2019

@author: Giulio
"""
import numpy as np
import Electoral_Montecarlo
import matplotlib.pylab as plt

data = (Electoral_Montecarlo.Complete_Simulation())


bins = np.linspace(0,300,100)

plt.hist(data['Movimento 5 stelle'], bins, alpha=0.5, label='M5S-sim.')
plt.hist(data['Centrodestra'], bins, alpha=0.5, label='Cdx-sim.')
plt.hist(data['Centrosinistra'],bins,alpha= 0.5,label = 'Csx-sim.')
plt.hist(Electoral_Montecarlo.Seats2018['Movimento 5 stelle'],bins,alpha = 0.5,label ='M5sReal')
plt.hist(Electoral_Montecarlo.Seats2018['Centrodestra'],bins,alpha = 0.5,label ='CdxReal')
plt.hist(Electoral_Montecarlo.Seats2018['Centrosinistra'],bins,alpha = 0.5,label ='CsxReal')
plt.xlabel('Seats')
plt.legend(loc='upper left')
plt.savefig("Histogram-Confrontation.png")
plt.close()

data = Electoral_Montecarlo.Possible_Results(10000)
plt.hist(data['Movimento 5 stelle'],bins,label = 'M5S')
plt.hist(data['Centrodestra'], bins, label='Cdx')
plt.hist(data['Centrosinistra'],bins,label = 'Csx')
plt.xlabel('Seats')
plt.legend(loc='upper left')
plt.savefig("Possible_outcome.png")
plt.close()

