import numpy as np
from read_data import read, find_segments
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



#R=np.array([[0,5,16,6,13,21],[0,12,9,3,4,21]])




class Solution:
    
    def reset(self):
        self.x=np.zeros((n+2,n+2,m))
        self.y=np.zeros((n+2,m))
        self.pi=np.zeros((n+2,m))
        self.a=np.zeros((n+2,m))
        self.not_visited=np.array(range(1,n+1))
    
    def update(self,R):
        self.R=R
        self.reset()
        for i in range(m):
            self.not_visited=np.setdiff1d(self.not_visited,R[i])
            for j in range (len(R[i])-1):
                self.x[R[i][j],R[i][j+1],i]=1
                self.y[R[i][j],i]=1
                self.a[R[i][j+1],i]=self.pi[R[i][j],i]+T[R[i][j]]+t[R[i][j],R[i][j+1]]
                self.pi[R[i][j+1],i]=max(self.a[R[i][j+1],i],e[R[i][j+1]])
            self.y[R[i][-1],i]=1
    
    def __init__(self,R=np.array([[0,n+1],[0,n+1]])):
        self.R=R
        if np.sum(R!=0):
           self.update(R)
        else:
            self.reset()

