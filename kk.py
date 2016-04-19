import random
import math

max_iter = 25000

#Cooling function for simulated annealing
def T(iter):
	return (10**10) * ((0.8)**math.floor(iter/300))

#RANDOM MOVE
#Generate random sequence S
def gen_sol_rm(n):
	S=[]
	for i in range(n):
		#50-50 chance of appending 1 or -1
		if random.random() < 0.5:
			S.append(1)
		else:
			S.append(-1)
	return S

#Find neighbor
def neighbor_rm(S):
	i,j=random.randint(0,len(S)-1),random.randint(0,len(S)-1)
	#ensures i and j are different
	while i==j:
		i,j=random.randint(0,len(S)-1),random.randint(0,len(S)-1)
	S[i]*=-1
	#50% chance of multiplying just S[i] by -1
	#50% chance of multiplying S[i] and S[j] by -1
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
		#generate random solution S
		S_0=gen_sol_rm(len(A))
		#compare residues, replace if lower
		if res_rm(S_0,A)<res_rm(S,A):
			S=S_0
	return S

#Hill climbing
def hill_climb_rm(A):
	S=gen_sol_rm(len(A))
	for i in range(max_iter):
		#generate random neighbor
		S_0=neighbor_rm(S)
		#compare residues, replace if lower
		if res_rm(S_0,A)<res_rm(S,A):
			S=S_0
	return S

#Simulated annealing
def simul_anneal_rm(A):
	S=gen_sol_rm(len(A))
	S_1=S
	for i in range(max_iter):
		S_0=neighbor_rm(S)
		if res_rm(S_0,A)<res_rm(S,A):
			S=S_0
		#replace w/ probability e^((res(S_0)-res(S))/T(i))
		elif random.random<math.exp(-(res_rm(S_0,A)-res_rm(S,A))/T(i)):
			S=S_0
		if res_rm(S,A)<res_rm(S_1,A):
			S_1=S
	return S_1

#PRE-PARTITIONING
#Generate random sequence S
def gen_sol_p(n):
	S=[]
	for i in range(n):
		#append random value 1<=x<=n
		S.append(random.randint(1,n))
	return S

#Find neighbor
def neighbor_p(S):
	i,j=random.randint(0,len(S)-1),random.randint(0,len(S)-1)

#Calculate residue given input A and coefficient S
def res_p(S,A):
	A_0=[]
	for i in range(len(A)):
		A_0.append(0)
	for j in range(len(A)):
		A_0[j] += A[j]

#Repeated random
def repeat_rand_p(A):
	S=gen_sol_p(len(A))
	for i in range(max_iter):
		S_0 = gen_sol_p(len(A))
		if res_p(S_0,A)<res_p(S,A):
			S=S_0
	return S

#Hill climbing
def hill_climb_p(A):
	S=gen_sol_p(len(A))
	for i in range(max_iter):
		S_0=neighbor_p(S)
		if res_p(S_0,A)<res_p(S,A):
			S=S_0
	return S

#Simulated annealing
def simul_anneal_p(A):
	S=gen_sol_p(len(A))
	S_1=S
	for i in range(max_iter):
		S_0=neighbor_p(S)
		if res_p(S_0,A)<res_p(S,A):
			S=S_0
		#replace w/ probability e^((res(S_0)-res(S))/T(i))
		elif random.random<math.exp(-(res_p(S_0,A)-res_p(S,A))/T(i)):
			S=S_0
		if res_p(S,A)<res_p(S_1,A):
			S_1=S
	return S_1


#Karmarkar-Karp Algorithm
def kk(A):
	A.sort():

