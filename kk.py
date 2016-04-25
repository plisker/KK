# ///////////////////////////////////////
# /*								   */
# /*  CS124 Programming Assignment 3   */
# /*     Curren Iyer & Paul Lisker     */
# /*		 April 25, 2016		       */
# /*	   							   */
# ///////////////////////////////////////

import random
import math
import bisect as b
import timeit
import csv

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
	S_1=list(S)
	for i in range(max_iter):
		S_0=neighbor_rm(S)
		if res_rm(S_0,A)<res_rm(S,A):
			S=S_0
		#replace w/ probability e^((res(S_0)-res(S))/T(i))
		elif float(random.random())<math.exp(-(res_rm(S_0,A)-res_rm(S,A))/T(i)):
			S=S_0
		if res_rm(S,A)<res_rm(S_1,A):
			S_1=list(S)
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
	S_1=list(S)
	for i in range(max_iter):
		S_0=neighbor_p(S)
		if res_p(S_0,A)<res_p(S,A):
			S=S_0
		#replace w/ probability e^((res(S_0)-res(S))/T(i))
		elif float(random.random())<math.exp(-(res_p(S_0,A)-res_p(S,A))/T(i)):
			S=S_0
		if res_p(S,A)<res_p(S_1,A):
			S_1=list(S)
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

# A sequence 100 long, for testing... same as inputfile.txt for C file
# B=[663624386304, 735830574803, 22056186970, 853703990905, 349224180521, 164289210369, 497823485316, 844689263757, 319727052244, 53583990916, 962428736619, 777603587687, 327979757846, 280637398266, 809397082800, 208709837888, 516283718133, 659688397998, 408107813985, 545382835743, 594223555753, 593778949830, 355300410404, 518437831638, 181434342633, 703445799093, 520399603289, 96514483053, 651258852771, 32743173307, 287222936258, 669717692465, 671041948515, 634532994101, 154708529520, 300850114682, 595802788087, 873507915545, 95909992886, 78162405935, 340450165516, 491489767680, 904890415352, 377225522896, 494389471110, 447246199378, 770997288386, 346654933830, 628330352221, 217686196136, 471292578501, 906435672272, 176003188152, 508942767356, 489322563863, 809051268956, 289667615584, 60282328411, 16456585202, 997620946374, 841655551891, 850594162370, 571214504524, 215684474250, 52180017333, 145758398896, 644013928606, 651979024238, 222278737721, 594385028721, 296773323744, 114679028421, 277837702345, 307940293345, 797198941126, 270205231989, 913618911988, 370913659874, 794763057040, 445145673719, 116695737852, 957228714061, 262765287200, 962766391759, 323139841133, 958431515716, 967920254653, 224514464463, 1898767134, 201476872152, 418154413843, 494081317546, 677582285269, 371489604400, 797685290795, 186824592442, 469409602634, 549322326239, 96516781307, 342394558103]
# print(kk(B))

Residues=[["KK", "Repeated Random R", "Repeated Random P", "Hill Climbing R", "Hill Climbing P", "Simulated Annealing R", "Simulated Annealing P"]]
Times=[["KK", "Repeated Random R", "Repeated Random P", "Hill Climbing R", "Hill Climbing P", "Simulated Annealing R", "Simulated Annealing P"]]

A=create50()
for i in range(50):
	print("This is loop number {}".format(i+1))

	start_t=timeit.default_timer()
	a_kk=kk(A[i])
	end_t=timeit.default_timer()
	kk_time=end_t-start_t

	start_t1=timeit.default_timer()
	rrr=repeat_rand_rm(A[i])
	end_t1=timeit.default_timer()
	rrr_time=end_t1-start_t1

	start_t2=timeit.default_timer()
	rrp=repeat_rand_p(A[i])
	end_t2 = timeit.default_timer()
	rrp_time=end_t2-start_t2


	start_t1=timeit.default_timer()	
	hcr=hill_climb_rm(A[i])
	end_t1=timeit.default_timer()
	hcr_time = end_t1-start_t1

	start_t2=timeit.default_timer()
	hcp=hill_climb_p(A[i])
	end_t2=timeit.default_timer()
	hcp_time = end_t2-start_t2


	start_t1=timeit.default_timer()
	sar=simul_anneal_rm(A[i])
	end_t1=timeit.default_timer()
	sar_time = end_t1-start_t1


	start_t2=timeit.default_timer()
	sap=simul_anneal_p(A[i])
	end_t2=timeit.default_timer()
	sap_time = end_t2-start_t2

	Residues.append([a_kk, rrr, rrp, hcr, hcp, sar, sap])
	Times.append([kk_time, rrr_time, rrp_time, hcr_time, hcp_time, sar_time, sap_time])


with open('Residues.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    data = Residues
    a.writerows(data)

with open('Times.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    data = Times
    a.writerows(data)
