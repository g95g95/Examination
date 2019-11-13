# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:06:57 2019

@author: Giulio
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:01:39 2019
@author: Jonathan Frassineti
"""
import numpy as np
from numpy.random import rand
import random as rd
import math

class Ising:
	
	def __init__(self,dimension,temperature=1):
		self.lattice     = np.array([[0.5*rd.choice([-1,1])for j in range(dimension)]for i in range(dimension)])
		self.dimension   = dimension
		self.temperature = temperature
	
	def __str__(self):
		for i in range(self.dimension):
			for j in range(self.dimension):
				if(self.lattice[i,j])<0:
					print('1',end='  ')
				elif(self.lattice[i,j]>0):
					print('0',end='  ')
			print('\n')
			
	def Tot_Magn(self):
		return sum(sum(self.lattice))

	def Make_Metropolis_Move(self):
		x,y                = np.array([rd.choice(list(range(self.dimension))),rd.choice(list(range(self.dimension)))])
		neighbouring_sites = self.lattice[(x+1)%self.dimension,y]+self.lattice[x,(y+1)%self.dimension]+self.lattice[(x-1)%self.dimension,y]+self.lattice[x,(y-1)%self.dimension]
		energy_change 	   = 2.*self.lattice[x,y]*neighbouring_sites
		if(energy_change<0):
			self.lattice[x,y]*=-1
		elif(rand()<math.exp(-energy_change)/self.temperature):
			self.lattice[x,y]*=-1
		return self.lattice

	def Montecarlo_Simulation(self,Nsteps):
		for i in range(Nsteps):
			self.Make_Metropolis_Move()
			if((i%10000==0)):
				self.__str__()
				print(self.Tot_Magn())



ising = Ising(20)

ising.Montecarlo_Simulation(100000)


