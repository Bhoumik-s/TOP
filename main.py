from data_class import Data
from constraints import status
from heuristic import heu1
from variables_class import Solution
from metaheuristic import metaN1,metaN2,metaN3
import time
import numpy as np
start_time=time.time()



file="data.xlsx"
d=Data(file,1,230,50)

print ("- %s seconds xlsx -" % (time.time()-start_time))
empty_route=np.array([[0,d.n+1]]*d.m)
rmvd=[[]]*d.m

sol=Solution(empty_route,d)
new_sol= heu1(sol,rmvd,d)
best_sol=new_sol
best_p=status(new_sol,d)[1]
iterations=0
while iterations<40:
	#print iterations
	metaheu=1
	while(metaheu<=3):
		if metaheu==1:
			meta=metaN1(new_sol.R)
		if metaheu==2:
			meta=metaN2(new_sol.R)
		if metaheu==3:
			meta=metaN3(new_sol.R)
		sol=Solution(meta[0],d)
		rmvd=meta[1]
		new_sol=heu1(sol,rmvd,d)
		new_p=status(new_sol,d)[1]
		if new_p>best_p:
			best_p=new_p
			best_sol=new_sol
			metaheu=1
		else:
			metaheu=metaheu+1
	iterations=iterations+1
print best_sol.R
print best_p 
print ("- %s seconds -" % (time.time()-start_time))
#print best_sol.pi-best_sol.a
#print sol.a[p[:][0],0]
#print sol.pi[p[:][0],0]


