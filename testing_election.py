# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:03:10 2019

@author: Giulio
"""


import numpy as np


Results2018={'Movimento 5 stelle':0.327,'Centrosinistra':0.22,'Centrodestra':0.37,'LeU':0.03}
ResultsHyp ={'Movimento 5 stelle':0.18,'Centrosinistra':0.20,'Lega':0.35,'Centrodestra':0.15}


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
