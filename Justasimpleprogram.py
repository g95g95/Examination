# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:13:32 2019

@author: Giulio
"""

import numpy as np
import scipy as sp
import random as rd

class Matrix:
	
	def __init__(self,dimension):
		
		self.dimension = dimension
		self.matrix    = np.array([['' for i in range(self.dimension)]for j in range(self.dimension)])
	
	def __add__(self,b):
		return [[self.matrix[i,j]+b.matrix[i,j]for i in range(self.dimension)]for j in range(self.dimension)]
	def mol(self,b):
		return (np.dot(self.matrix,b.matrix))
		
	def fill_Matrix_byfile(self,file_path):
		
		lines_file  = [line.strip() for line in open(file_path)]
		self.matrix = np.array([[eval(lines_file[i]) for i in range(self.dimension)]for j in range(self.dimension)])
		
		
	def fill_Matrix_bystandard_input(self,file_path):
		self.matrix = np.array([eval(input("Insert the elementh of the ",i,"th row")) for i in range(self.dimension)])
		
	def fill_Matrix_with_already_existing_array(self,array):
		self.matrix = np.array(array.copy())
		
		
	def Eigenvalues(self):
		return np.linalg.eig(self.matrix)[0]
	
	def Eigenfunctions(self):
		return np.linalg.eig(self.matrix)[1]		


	def Diagonal(self):
		return np.diag(self.Eigenvalues())
	
matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
matrix2 = [[4,5,6],[4,5,6],[4,5,6]]

m1 = Matrix(3)
m2 = Matrix(3)



