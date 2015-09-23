import numpy as np
from read_data import read, find_segments


data=read("data.xlsx")
t=find_segments(data[:,:2])
p=data[:,2]
d=data[:,3]
e=data[:,4]
l=data[:,5]
T=data[:,6]
m=2
n=20
Tmax=230
Q=50

p=np.array([[0,5,16,6,13,21],[0,12,9,3,4,21]])

class Solution:
    
    def __reset(self):
        self.x=np.full((n+2,n+2,m),np.nan)
        self.y=np.full((n+2,m),np.nan)
        self.pi=np.full((n+2,m),np.nan)
        self.a=np.full((n+2,m),np.nan)
        self.pi[0]=0
    
    def update(self,R):
        self.R=R
        self.__reset()
        for i in range(m):
            for j in range (len(R[i])-1):
                self.x[R[i][j],R[i][j+1],i]=1
                self.y[R[i][j],i]=1
                self.a[R[i][j+1],i]=self.pi[R[i][j],i]+T[R[i][j]]+t[R[i][j],R[i][j+1]]
                self.pi[R[i][j+1],i]=max(self.a[R[i][j+1],i],e[R[i][j+1]])
            self.y[R[i][-1],i]=1    
    
    def __init__(self,R=np.zeros((m,2),dtype=int)):
        self.R=R
        if np.sum(R!=0):
           self.update(R)
        else:
            self.__reset()

sol=Solution(p)



