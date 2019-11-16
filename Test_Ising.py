# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:27:50 2019

@author: Giulio
"""

import Ising
import numpy as np
import random as rd


def test_lattice(ising = Ising.Ising(15)):
	
	for i in range(len(ising.lattice[0])):
		
		assert set(ising.lattice[i]) == {1,-1}


def test_Mont_Move(ising = Ising.Ising(15)):
	initial_magnetization = ising.Abs_Tot_Magn()
	initial_energy        = ising.Tot_Energy()
	ising.MontSim()
	assert (ising.Abs_Tot_Magn()>=initial_magnetization and ising.Tot_Energy()>=initial_energy)


def test_Simulation(ising = Ising.Ising(15,.1)):
	ising.MontSim()
	assert ising.Abs_Tot_Magn() == 1

