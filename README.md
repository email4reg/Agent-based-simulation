# Agent-based-simulation
This is a course-based project working upon the econophysics.

     Author: Yufeng Ma                   
     Fudan University
     Email: ramosma0111@gmail.com
  
  
     Co-author: Chenyang Qian            
     Fudan University
     Email: 13307110047@fudan.edu.cn


##Objective and Background
In this project we are trying to simulate the complex financial system using an agent-based approach. This idea was first sparked by the econophysics course during which Prof Chen Yu(The University of Tokyo) mentioned some very interesting models built to simulate the finacial market. However, many of these models cannot simulate this complexity with the support of market diversity, consisting of only two or three kinds of market members. Thus we are trying to avoid this weakness and to demonstrate the impact brought by the diversity. Also, this project is a course-based project and we wish that if you are going to cite our code and research report, please use this url: https://github.com/yfmaRamos/Agent-based-simulation.

##Abstract
This project breifly introduces 5 kinds of agents and only one stock.The agents include speculators, idoits, intelligencies, rich-people and supervisor.All of the agents should make their decisions at same time, and the sum of their decisions will decide the stock price. They share same attributes while maintain their difference in the behavior and decision process.Some may have little intelligence while others are not. The most intelligent agents will use special techniques in machine learning and reinforcement learning to help themselves to make decisions which is kind of THRILLING!

##Content
###1.Market Members
####    - opportunism
####    - idiots
####    - intellegents
####    - rich people
####    - supervisor

In this chapter, we are first introducing the same attributes of a class MarketMember. They should have their names, their assets, their positions of stocks, their cash, their decisions, their expectations, and their behaviors(policies).As a father class, the menbers should base on the information of the market and find expectations in their possible decision pools. All of the expecatations would derive a price change, which will reflect on agents' next decisions. The system regulates the stock prices will be talked about later in chapter 2. The subclasses, of course, should vary in their decisions, their behaviors, and their expectations. So it's important to specify different systems of making decisions.

1. Two important behaviors of the oppurtunism：

Deciding expectation: It's of vital importance that the opportunism give their expectations (say 1,-1) based on the state of the two bit system(11,10,01,00).Instead of giving their expectations according to their decision pools with certainty, we much prefer the model of epsilon-greedy algorithm. That is, we give the agents a kind of uncertainty when making their decisions. For example, an agent with p1 equals 0.8 means that this agent should have a 0.8 possibility to give an expectation of one, while may also have a 0.2 possibility to give -1. Also it's weird to maintain their possibility as a constant, as we all know that the agents have the ability to learn from the reality,i.e. learn from their decisions and the change of the prices. We tend to use a reward model which means the agent will have a positive reward if he made the right decision according to price change. So we are going to take some time to define a reward function.

How to define the reward function?

We've already known that one agent get a positive reward after a right action and a negative reward after a wrong one. This reward may invoke the change of the possibilities of expectactions at the state. So, this function can be expressed as R(s,a,s') which is quite similar in the reinforcement learning problem and s,s' represent the present and future state, a stands for the action or the expectation. If we are in state s, we make a decision, and of course we will know the price change in state s'. Suppose we have a memory base, we will remember the price change of this transition period, and moreover the sum of the price change with a tag of the state s and action a. For example, at a time ti(with a state s), and the agent gives 1,then he get a price change delat_x. Since every time ti the state s taking action 1, he all get a delta x. Let's say the collection is C. We first introduce a return function:E(a=1,state=s) = sum(p1(state=s,ti)*delta_x)  ,ti belongs to C. Similarly we can define a E(a=-1,state=s) = sum(p-1(state=s,ti)*delta_x), ti belongs to C(different from the C above).
Since we have defined the return function, we can just refresh our possibility.

###2.Stock price and trading rules
###3.Simulation 
###4.Results 
###5.References



