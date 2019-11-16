# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:12:33 2019

@author: Giulio
"""


import numpy as np
Results2018={'Movimento 5 stelle':0.327,'Centrosinistra':0.22,'Centrodestra':0.37,'LeU':0.03}
ResultsHyp1 ={'Movimento 5 stelle':0.18,'Centrosinistra':0.20,'Lega':0.35,'Centrodestra':0.15}
ResultsHyp2 ={'Centrosinistra':0.38,'Centrodestra':0.52}
Seats2018  ={'Movimento 5 stelle':221,'Centrosinistra':109,'Centrodestra':260,'LeU':22} #excluding abroad seats



    
def max_key(d):#this method returns the key with the highest value of a dictionary
    max_key = ''
    max_value = 0
    for key in list(d.keys()):
        if d[key]>max_value:
            max_key = key
            max_value = d[key]    
    return max_key    
        

        
def Fill_Seats(weight_maj = 0.37,weight_prop = 0.61,Results = Results2018): 
	"""This method runs the Montecarlo's algorythm for each collegium. It can be
	performed using different weights according to the electoral law we are considering"""
	seats = {key:int(Results[key]*635*weight_prop)+int(Results[key]*(1-sum(list(Results.values())))) for key in list(Results.keys())}
	for i in range (int(635*weight_maj)):
		Resultscopy = Results.copy()
		Resultscopy = {key:Results[key]*np.random.rand() for key in Results.keys()}#this is the core of the program
		seats[max_key(Resultscopy)]+=1
	return seats

def Complete_Simulation(weight_maj = 0.37,weight_prop = 0.61,Results = Results2018):
	seats = {key:0 for key in list(Results)}
	"""This function provides a valid estimation for the assigned number of seats
	by averaging over 10000 simulation. This result will be used for confrontation
	with real data"""
	for i in range(10000):
		for key in list(Results):
			seats[key]+=Fill_Seats(weight_maj,weight_prop,Results)[key]
	average_seats = {key:int(seats[key]/10000.) for key in list(Results.keys()) }
	return average_seats

def winning_min_seats(Party,min_seats = 310,Results = Results2018):
	wins = 0
	"""This method returns how many times a certain party can obtain more than
    a specified number of seats"""
	for i in range(10000):
		current_situation = Fill_Seats(0.61,0.37,Results)
		if (current_situation[Party]>min_seats):
			wins +=1
			print(Party,"got",current_situation[Party],"seats")
	return wins
    

def Possible_Results(N,weight_maj = 0.37,weight_prop = 0.61,Results = Results2018):
	"""This function returns a dicionary having the parties has keys and each value
	is a list of all the results obtained all over an N iteration of Fill_Seats()"""
	possible_results = {key:[Fill_Seats(weight_maj,weight_prop,Results)[key]for i in range(N)]for key in list(Results)}
	return possible_results




