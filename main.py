from read_data import read, find_segments
from constraints import status
from heuristic import heu1
from variables_class import Solution
import time
import numpy as np

data=read("data.xlsx")
t=find_segments(data[:,:2])
p=data[:,2]
d=data[:,3]
e=data[:,4]
l=data[:,5]
T=data[:,6]
n=data.shape[0]-2
m=2
M=10000
Tmax=230
Q=50

rmvd=[]
start_time=time.time()
sol=Solution()
rmvd=np.array([[0,21],[0,21]])

new_sol= heu1(sol,rmvd)

print status(new_sol,t,p,m,n,d,l,T,M,Q,Tmax)
print ("- %s seconds -" % (time.time()-start_time))
#print len(sol.R[0])
#print sol.a[p[:][0],0]
#print sol.pi[p[:][0],0]


