# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:27:50 2019

@author: Giulio
"""

import Ising
import numpy as np
import random as rd


def test_lattice(ising = Ising.Ising(15)):
	"""This testing method proves that the lattice of an ising object is 
	correctly initialized in a matrix of -1 and 1"""
	for i in range(len(ising.lattice[0])):
		
		assert set(ising.lattice[i]) == {1,-1}


def test_Mont_Move(ising = Ising.Ising(15)):
	"""This method tests the Montecarlo move. At the end of a Simulation we expect
	the abs total magnetization to be larger than the initial one for a starting
	configuration and so the energy."""
	initial_magnetization = ising.Abs_Tot_Magn()
	initial_energy        = ising.Tot_Energy()
	ising.MontSim()
	assert (ising.Abs_Tot_Magn()>=initial_magnetization and ising.Tot_Energy()>=initial_energy)


def test_Simulation(ising = Ising.Ising(15,.1)):
	"""This routine test is used to verify wether a very low temperature system
	is going to reach the magnetic order after a significant number of iterations"""
	ising.MontSim()
	assert ising.Abs_Tot_Magn() == 1

