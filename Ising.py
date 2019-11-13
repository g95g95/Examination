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
import random as rd
import numpy as np
from numpy.random import rand
from tkinter import *

class Ising:
	
	
	def __init__(self,dimension,T=.1):
		self.dimension = dimension
		self.lattice  = np.array([[rd.choice([-0.5,0.5]) for i in range(dimension)]for j in range(dimension)])
		self.T = T

	def Make_move(self):
		x,y = [rd.choice([i for i in range(self.dimension)]),rd.choice([i for i  in range(self.dimension)])]
		neighbours = self.lattice[(x+1)%self.dimension,y]+self.lattice[x,(y+1)%self.dimension]+self.lattice[(x-1)%self.dimension,y]+self.lattice[x,(y-1)%self.dimension]
		delta_energy_spot = 2*self.lattice[x,y]*neighbours
		
		if(delta_energy_spot<0):
			self.lattice[x,y]*=-1
			
		elif(rand()<np.exp(-delta_energy_spot/self.T))	:
			self.lattice[x,y]*=-1
		
		
	def print_lattice(self):
		Lattice = [['' for i in range (self.dimension)]for j in range (self.dimension)]
		for i in range(self.dimension):
			for j in range(self.dimension):
				if self.lattice[i,j]<=0:
					Lattice[i][j] = '0' 
				elif self.lattice[i,j]>0:
					Lattice[i][j] = '1'
		for i in range(self.dimension):
			print(' '.join(Lattice[i]))
		
					
	def print_lattice_GUI(self):
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
				
	def Abs_Tot_Magn(self):
		return np.abs(2*sum(sum(self.lattice))/(self.dimension*self.dimension))
	
	def Tot_Energy(self):
		Tot_Energy = 0
		for x in range(self.dimension):
			for y in range(self.dimension):
				single_spot_energy = self.lattice[(x+1)%self.dimension,y]+self.lattice[x,(y+1)%self.dimension]+self.lattice[(x-1)%self.dimension,y]+self.lattice[x,(y-1)%self.dimension]
				Tot_Energy        += single_spot_energy
		return Tot_Energy/4.		
				
	def MontSim (self,Nsteps=100000):
		for i in range(Nsteps):
			self.Make_move()
			
			procedure = Nsteps/(i+1)	
			if procedure  in list(range(100)):
				print(self.Abs_Tot_Magn())
				print("{:.2f}".format(float(i/Nsteps)*100),'%\n')
				



















				