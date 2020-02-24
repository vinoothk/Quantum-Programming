h_count = 0
cx_count = 0
u1_count = 0
u2_count = 0
u3_count = 0
one_qbit_fid = 0.99 
two_qbit_fid = 0.95
read_out_fid_avg = 0.85
one_qbit_delay = 0.060 #microsec
two_qbit_delay = 0.323 
coherence_time = 20
#T1: energy relaxation time
#T2: dephasing time
#T1 = 1.2 #coherence time of each qbit. longer sequences of 
#T2 = 640 #323 ns. (2-Qubit) gate delays #~60 ns. 

with open('Qft3.txt') as f:
	datafile = f.readlines()
	for line in datafile:
		if '//' in line:
			continue
		if 'h' in line:
			h_count+=1
		if 'cx' in line:
			cx_count += 1
		if 'u1' in line:
			u1_count+=1
		if 'u2' in line:
			u2_count+=1
		if 'u3' in line:
			u3_count+=1

one_qbit_count = h_count + u1_count + u2_count + u3_count
two_qbit_count = cx_count
all_gate = one_qbit_count + two_qbit_count
correct_result =  ( one_qbit_fid ** (one_qbit_count) ) + (two_qbit_fid ** two_qbit_count ) + ( read_out_fid_avg ** all_gate )	

exec_time = (one_qbit_count * one_qbit_delay) + (two_qbit_count * two_qbit_delay)

if (exec_time < coherence_time):
	
	print("exec_time in microsec", exec_time)	
	print("coherence_time in microsec", coherence_time)
	print("successufully finished execution with probability:", correct_result)

else:
	print("exec_time in microsec", exec_time)	
	print("coherence_time in microsec", coherence_time)
	print("execution time execeed coherence time:", correct_result)




#print(h_count,cx_count,u1_count,correct_result)