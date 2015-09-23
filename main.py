import numpy as np
from read_data import read, find_segments
#source:http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6887433

data=read("data.xlsx")  # read data
t=find_segments(data[:,:2]) # calculates each segment time
print t
p=data[:,2]  # profit associted with each point (Happiness index)
T=data[:,6] # service time
M=1000 # very large number
n=data.shape[0]-2 # number of locations
m=4 # no. of days for visit
x=np.zeros((n+2,n+2,m), dtype=int) #x(i,j,k)=1 if in route k one goes from i to j
y=np.zeros((n+2,m),dtype=int) # y(i,k)=1 if point i is visited in route k
pi=np.zeros

update=status(m,n,x,y,p,T,t,pi,d,l,M,Q,Tmax)

