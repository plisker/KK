import random
import math
import bisect as b

#TODO: NEED to increase Max_Iter
max_iter = 25000
seq_length = 100

#Karmarkar-Karp Algorithm
def kk(B):
	A=list(B)
	A.sort()
	while len(A) > 1:
		x=A.pop()-A.pop()
		b.insort(A, x)
	return A[0]

#Cooling function for simulated annealing
def T(iter):
	return (10**10) * ((0.8)**math.floor(iter/300))

#RANDOM MOVE
#Generate random sequence S
def gen_sol_rm(n):
	S=[]
	for i in range(n):
		#50-50 chance of appending -1 or 1
		if random.random() < 0.5:
			S.append(-1)
		else:
			S.append(1)
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
	n=len(A)
	S=gen_sol_rm(n)
	for i in range(max_iter):
		#generate random solution S
		S_0=gen_sol_rm(n)
		#compare residues, replace if lower
		if res_rm(S_0,A)<res_rm(S,A):
			S=S_0
	return res_rm(S,A)

#Hill climbing
def hill_climb_rm(A):
	S=gen_sol_rm(len(A))
	for i in range(max_iter):
		#generate random neighbor
		S_0=neighbor_rm(S)
		#compare residues, replace if lower
		if res_rm(S_0,A)<res_rm(S,A):
			S=S_0
	return res_rm(S,A)

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
	return res_rm(S_1,A)

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
	while S[i]==j:
		i,j=random.randint(0,len(S)-1),random.randint(0,len(S)-1)
	S[i]=j
	return S

#Calculate residue given input A and coefficient S (by creating intermediary A')
def res_p(S,A):
	n=len(A)
	A_0=[]
	for i in range(n):
		A_0.append(0)
	for j in range(n):
		A_0[S[j]-1] += A[j]
	return kk(A_0)	

#Repeated random
def repeat_rand_p(A):
	n=len(A)
	S=gen_sol_p(n)
	for i in range(max_iter):
		S_0 = gen_sol_p(n)
		if res_p(S_0,A)<res_p(S,A):
			S=S_0
	return res_p(S,A)

#Hill climbing
def hill_climb_p(A):
	S=gen_sol_p(len(A))
	for i in range(max_iter):
		S_0=neighbor_p(S)
		if res_p(S_0,A)<res_p(S,A):
			S=S_0
	return res_p(S,A)

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
	return res_p(S_1,A)

def create_sequence(n):
	A=[]
	for i in range(n):
		A.append(random.randint(1,10**12))
	return A

def create50():
	A=[]
	for i in range(50):
		A.append(create_sequence(seq_length))
	return A



A=create50()
for i in range(50):
	print("This is loop number {}".format(i+1))
	a_kk=kk(A[i])
	print("KK:", a_kk)

	rrr=repeat_rand_rm(A[i])
	rrp=repeat_rand_p(A[i])
	print("RRR:", rrr, "RRP", rrp)

	hcr=hill_climb_rm(A[i])
	hcp=hill_climb_p(A[i])
	print("HCR", hcr, "HCP", hcp)

	sar=simul_anneal_rm(A[i])
	sap=simul_anneal_p(A[i])
	print("SAR", sar, "SAP", sap)






