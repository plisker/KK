import random
import math
import copy

max_iter = 25000

#Cooling function for simulated annealing
def T(iter):
	return (10**10) * ((0.8)**math.floor(iter/300))

#Generate random sequence S
def gen_sol(n):
	S=[]
	for i in range(n):
		if random.random() < 0.5:
			S.append(1)
		else:
			S.append(-1)

	return S

#Move to a neighbor at random
def random_move(S):
	i,j=0,0
	while i==j:
		i,j=random.randint(0,len(S)-1),random.randint(0,len(S)-1)
	S[i]*=-1
	if random.random()<0.5:
		S[j]*=-1
	return S

#Calculate residue given input array A and coefficient array S
def residue(S,A):
	return abs(sum([(x*y) for x,y in zip(S,A)]))

#Repeated random
def repeat_rand(A):
	S = gen_sol(len(A))
	for i in range(max_iter):
		S_0 = gen_sol(len(A))
		if residue(S_0,A) < residue(S,A):
			S=copy.deepcopy(S_0)
	return S

#Hill climbing
def hill_climb(A):
	S = gen_sol(len(A))
	for i in range(max_iter):
		S_0 = random_move(copy.deepcopy(S))
		if reside(S_0,A) < reside(S,A):
			S=copy.deepcopy(S_0)
	return S

#Simulated annealing
def simul_anneal(A):
	S = gen_sol(len(A))
	S_1 = copy.deepcopy(S)
	for i in range(max_iter):
		S_0 = random_move(copy.deepcopy(S))
		if residue(S_0,A) < residue(S,A):
			S=S_0
		if residue(S,A) < residue(S_1,A):
			S_1=S
	return S_1


