import random
import math
import copy

max_iter = 25000

#Cooling function for simulated annealing
def T(iter):
	return (10**10) * ((0.8)**math.floor(iter/300))

#RANDOM MOVE
#Generate random sequence S
def gen_sol_rm(n):
	S=[]
	for i in range(n):
		if random.random() < 0.5:
			S.append(1)
		else:
			S.append(-1)
	return S

#Find neighbor
def neighbor_rm(S):
	i,j=0,0
	while i==j:
		i,j=random.randint(0,len(S)-1),random.randint(0,len(S)-1)
	S[i]*=-1
	if random.random()<0.5:
		S[j]*=-1
	return S

#Calculate residue given input A and coefficient S
def res_rm(S,A):
	return abs(sum([(x*y) for x,y in zip(S,A)]))

#Repeated random
def repeat_rand_rm(A):
	S=gen_sol_rm(len(A))
	for i in range(max_iter):
		S_0=gen_sol_rm(len(A))
		if res_rm(S_0,A)<res_rm(S,A):
			S=copy.deepcopy(S_0)
	return S

#Hill climbing
def hill_climb_rm(A):
	S=gen_sol_rm(len(A))
	for i in range(max_iter):
		S_0=neighbor_rm(copy.deepcopy(S))
		if res_rm(S_0,A)<res_rm(S,A):
			S=copy.deepcopy(S_0)
	return S

#Simulated annealing
def simul_anneal_rm(A):
	S=gen_sol_rm(len(A))
	S_1=copy.deepcopy(S)
	for i in range(max_iter):
		S_0=random_move(copy.deepcopy(S))
		if res_rm(S_0,A)<res_rm(S,A):
			S=S_0
		elif random.random<math.exp(-(res_rm(S_0,A)-res_rm(S,A))/T(iter)):
			S=S_0
		if res_rm(S,A)<res_rm(S_1,A):
			S_1=S
	return S_1

#PRE-PARTITIONING
#Generate random sequence S
def gen_sol_p(n):
	S=[]
	for i in range(n):
		S.append(random.randint(1,n-1))
	return S

#Find neighbor
def neighbor_p(S):
	

#Calculate residue given input A and coefficient S

#Repeated random

#Hill climbing

#Simulated annealing

