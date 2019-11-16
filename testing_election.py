# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:03:10 2019

@author: Giulio
"""


import numpy as np
import random as rd
import Electoral_Montecarlo

Results2018={'Movimento 5 stelle':0.327,'Centrosinistra':0.22,'Centrodestra':0.37,'Leu':0.03}
ResultsHyp ={'Movimento 5 stelle':0.18,'Centrosinistra':0.20,'Lega':0.35,'Centrodestra':0.15}
Seats2018  ={'Movimento 5 stelle':221,'Centrosinistra':113,'Centrodestra':260,'Leu':14} #excluding abroad seats

def test_Number_iterations(Nsteps = 10000):
	pi = float(4*(sum([1 for i in range(10000) if((np.random.rand()*2-1)**2+(np.random.rand()*2-1)**2<1)])/10000))
	assert (abs(np.pi-pi)/np.pi)<=0.01

def test_max_key(d = Results2018):
    max_key = ''
    max_value = 0
    for key in list(d.keys()):
        if d[key]>max_value:
            max_key = key
            max_value = d[key]
    assert max_key == 'Centrodestra'
	
	
def test_simulation(a = rd.choice(list(Seats2018.keys())),d = Seats2018):
	Simulation = Electoral_Montecarlo.Complete_Simulation()
	assert np.abs(Simulation[a] - Seats2018[a])<10 #There's a little difference because of different method ripartition for the proportional part

def test_winning_seats(d = Results2018):
	for key in (list(d.keys())):
		assert not Electoral_Montecarlo.winning_min_seats(key,500)
		
		
	
	
