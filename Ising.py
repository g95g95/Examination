# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:06:57 2019

@author: Giulio
"""

# -*- coding: utf-8 -*-

import random as rd
import numpy as np
from numpy.random import rand
from tkinter import *

class Ising:
	
	
	def __init__(self,dimension,T=.1):
		self.dimension = dimension
		self.lattice  = np.array([[rd.choice([-1,1]) for i in range(dimension)]for j in range(dimension)])
		self.T = T
		"""we simply defined the main features an Ising object should have: its dimension, the matrix		
		describing the lattice and the temperature the system is at"""	
		
	def Make_move(self):
		x,y = [rd.choice([i for i in range(self.dimension)]),rd.choice([i for i  in range(self.dimension)])]
		neighbours = self.lattice[(x+1)%self.dimension,y]+self.lattice[x,(y+1)%self.dimension]+self.lattice[(x-1)%self.dimension,y]+self.lattice[x,(y-1)%self.dimension]
		delta_energy_spot = 2*self.lattice[x,y]*neighbours
		"""This is the algorythm to compute the energy change if we flip the randomly chosen spot. The term
		%self.dimension underlines the Periodical Boundary Condition otherwise we would have to specify case by case"""
		if(delta_energy_spot<0):#If the energy decreases due to the flipping we'll always accept
			self.lattice[x,y]*=-1
		elif(rand()<np.exp(-delta_energy_spot/self.T)):#otherwise we accept with this exponential statistical  weight
			self.lattice[x,y]*=-1
		
		
	def print_lattice(self):
		"""This method is only useful to check at the first execution of the code if 
		the system is "graphically" evolving correctly"""
		Lattice = [['' for i in range (self.dimension)]for j in range (self.dimension)]
		for i in range(self.dimension):
			for j in range(self.dimension):
				if self.lattice[i,j]<=0:
					Lattice[i][j] = '0' 
				elif self.lattice[i,j]>0:
					Lattice[i][j] = '1'
		for i in range(self.dimension):
			print(' '.join(Lattice[i]))
		
					
	def print_lattice_GUI(self): #This method is used for the graphic representation of the evolution

		root = Tk()
		Lattice = [['' for i in range(self.dimension)]for j in range(self.dimension)]			
		for i in range(self.dimension):
			for j in range(self.dimension):
				if self.lattice[i,j]<0:
					Lattice[i][j]=Label(bg='white',width=2,height=2)
					Lattice[i][j].grid(row=i,column=j)
				if self.lattice[i,j]>0:
					Lattice[i][j]=Label(bg='black',width=2,height=2)
					Lattice[i][j].grid(row=i,column=j)
		mainloop()
			
	def show_evolution(self): #This method runs a simulation over 10001 Make_move
		#and displays the final situation for a fixed temperature(0.1K in our case)
		for i in range(10001):
			self.Make_move()
			if (i%2000 == 0):
				self.print_lattice_GUI()
				
	def Abs_Tot_Magn(self):#This method computes the absolute Total Magnetization
		return np.abs(sum(sum(self.lattice))/(self.dimension*self.dimension))
	
	def Tot_Energy(self): #This method computes the absolute Total Energy
		#it exploits the same algorythm of Make_move()
		Tot_Energy = 0
		for x in range(self.dimension):
			for y in range(self.dimension):
				single_spot_energy = self.lattice[(x+1)%self.dimension,y]+self.lattice[x,(y+1)%self.dimension]+self.lattice[(x-1)%self.dimension,y]+self.lattice[x,(y-1)%self.dimension]
				Tot_Energy        += single_spot_energy
		return abs(Tot_Energy/4.)		
				
	def MontSim (self,Nsteps=2000):
		for i in range(Nsteps):
			self.Make_move()
			"""This is the core of the program. We run a simulation over a suffi
			ciently high number of iteration of Make_move and it will be used to
			estimate the Critical Temperature Tc
			"""
				