import numpy as np
Results2018={'Movimento 5 stelle':0.327,'Centrosinistra':0.22,'Centrodestra':0.37,'LeU':0.03}
ResultsHyp ={'Movimento 5 stelle':0.18,'Centrosinistra':0.20,'Lega':0.35,'Centrodestra':0.15}




class Electoral_Simulation:
	
	def __init__(self,Results):
		self.Results = Results

	def test_max_key(d=Results2018):
    	max_key = ''
    	max_value = 0
    	for key in list(d.keys()):
        	if d[key]>max_value:
            	max_key = key
            	max_value = d[key]
    	assert max_key == 'Centrodestra'
    
	def max_key(d):
    	max_key = ''
    	max_value = 0
    	for key in list(d.keys()):
        	if d[key]>max_value:
            	max_key = key
            	max_value = d[key]    
    	return max_key    
        
        
	def Fill_Seats(weight_maj = 0.37,weight_prop = 0.61,Results = ResultsHyp):   
    	seats = {key:int(Results[key]*635*weight_prop)+int(Results[key]*(1-sum(list(Results.values())))) for key in list(Results.keys())}
    	for i in range (int(635*weight_maj)):
        	Resultscopy = Results.copy()
        	Resultscopy = {key:Results[key]*np.random.rand() for key in Results.keys()}
        	seats[max_key(Resultscopy)]+=1
    	return seats
		
		
		
		
		
		
		
		
		
		
		
		
