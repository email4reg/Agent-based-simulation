import numpy as np
def price_design(sigma_volume,current_price,function = 1,tao = 20):
	'''This is a fuction which takes in the parameter sigma_volume,
	and a function para since we have made two systems of the price 
	change. It will return the price change.'''
	if function == 1:
		ratio = (np.exp(sigma_volume/tao)/(1+np.exp(sigma_volume/tao))-0.5)*0.2
		# as you can see the function is very clever that it 
		# automatically controls the price of the stock in a range
		# -10% to 10%
	else:
		ratio = sigma_volume/tao
		if ratio >  0.1:
			ratio = 0.1
		elif ratio < -0.1:
			ratio = -0.1
	delta_price = ratio*current_price
	price = delta_price+current_price
	return delta_price,price 


