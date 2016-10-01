import random
import numpy as np 

class Market_member:
	'''we first define an abstract class.'''
	
	def __init__(self):
		'''a trader should have a name,and his/her asset, the position of
		of stocks, the cash, his own decision pools, his action and
		his experience.'''
		self.name = "" 
		self.asset = 0.0
		self.asset0 = 0.0
		self.position = 0.0
		self.cash = 0.0
		self.decisions = {}
		self.memory = {}

	def set_name(self,name):
		self.name = name

	def set_decisions(self,decisios):
		slef.decisions = decisions

	def make_decision(self,information):
		'''In this fucntion, we employed some uncertainty into the 
		decision'''
		decision = self.decisions[information]
		p1 = self.memory[information]['p1']
		pminus = 1-p1
		randp = random.random()
		if decision == 1:
			if randp > p1:
				decision = -1
		if decision == -1:
			if randp > 1-p1:
				decision = 1
		return decision 

	def set_asset(self,asset):
		self.asset = asset
		self.asset0 = asset
		'''cause at the first time the cash will equal the asset'''
		self.cash = asset

	def refresh_cash_pos(self,cash,position):
		'''this function refreshes one's cash and position'''
		self.cash = cash
		self.position = position 

	def initialize_memory(self,p1):
		states = [00,01,10,11]#this represents four possible states of the stock
		for state in states:
			self.memory[state] = {}
			self.memory[state]['p1']=p1
			self.memory[state]['p-1']=1-p1
			self.memory[state]['E1']=0
			self.memory[state]['E-1']=0


	def expectation(self,information,current_price):
		'''This is an expectation to demonstrate one's perspective to 
		the information procvided by the market and the price.
		For example : if one's perspective is +1,while his/her cash 
		may not be enough to support this decision, then the hot_degree
		will be 0.
		Vice versa ,if the perspective is -1,while the position is zero,
		then the solution will also be zero.
		''' 
		hot_degree = self.make_decision[inforamtion]
		if self.decisions[information] == 1: 
			if (self.cash == 0 ) :
				hot_degree = 0
		else :
			if ( self.position == 0) : 
				hot_degree = 0
		return hot_degree

	def trade_quantity(self,information,expectation):
		'''this function made clear how much cash should we input in the
		stock,if the expectation is 0,then the agent do nothing,while if
		expectation is one,then he buys.Vice versa.'''
		volume = 0.0
		p1 = self.memory[information]['p1']
		pminus = 1-p1
		cash = self.cash
		position = self.position
		if expectation == 0:
			pass
		elif expectation == 1:
			volume = +cash*Gaussian(p1)
		elif expectation == -1:
			volume = -position*Gaussian(pminus)
		cash = cash - volume
		position = position + volume
		refresh_cash_pos(cash,position)
		return volumn#this volume means the input money of the agent

	def get_reward(self,price_change,state,decision):
		'''Since the agent has made a decision, of course he should 
		get a reward no matter good or bad.'''
		p1 = self.memory[information]['p1']
		pminus = 1-p1
		if decision == 1:
			self.memory[state]['E1'] += p1*price_change
		else :
			self.memory[state]['E-1'] += pminus*price_change
		refresh_possibility()

	def refresh_possibility(self,tao = 2):
		'''this function refreshed the possibility of the people's 
		srategy.'''
		E1 = self.memory[state]['E1'] 
		Eminus = self.memory[state]['E-1']
		p1 = np.exp(E1)/(np.exp(E1/tao)+np.exp(Eminus/tao))
		#tao is a parameter
		pmius = 1-p1
		self.memory[state]['p1'] = p1
		self.memory[state]['p-1'] = pminus 

	def refrsh_asset(self,price_change,price):
		'''this function should be implemented after a trading day.'''
		delta = self.possition*price_change/price
		self.asset += delta
		self.position += delta

	def is_death(self):
		'''when an agent loses all of his asset or wins a lot of money
		,then he will die from the market.'''
		if (slef.asset < self.asset0*0.2) or (self.asset > self.asset0*3):
			return true
		else:
			return false

#end
