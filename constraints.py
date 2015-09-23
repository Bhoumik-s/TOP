import numpy as np

def objective(p,y,m,n):
    f=0
    for i in range(m):
        for j in range (1,n+1):
            f=f+p[j]*y[j,i]
    return f

def constraint1(x,m,n):
    sum1=np.sum(x[0,1:n+1,:])
    sum2=np.sum(x[1:n+1,n+1,:])
    return ((sum1==sum2) and (sum1==m))
            
def constraint2(x,y,m,n):
    boolean=True
    for i in range(1,n+1):
        for k in (m):
            sum1=np.sum(x[0:n+1,i,k])
            sum2=np.sum(x[i,1:n+2,k])
            boolean=(boolean and ((sum1==sum2) and (sum1==y[l,k])))
    return boolean

def constraint3(x,pi,m,n,M):
    boolean=True
    for i in range(n+2):
        for j in range(n+2):
            for k in range (m):
                boolean=(boolean and (pi(i,k)+T[i]+t[i,j]-pi[j,k]<=M(1-x[i,j,k])))
    return boolean

def constraint4(y,m,n):
    boolean=True
    for h in range(1:n+1):
        boolean=(boolean and (np.sum(y[h,:])<=1))
    return boolean

def constraint5(d,y,m,n,Q):
    boolean=True
    for k in range(m):
        sum1=0
        for i in range(1,n+1):
            sum1=sum1+d[i]*y[i,k]
        boolean=(boolean and (sum1<=Q))
    return boolean

def constraint6(x,y,m,n,T,t):
    boolean=True
    for k in range(m):
        sum1=0
        for i in range(0:n+1):
            sum2=0
            for j in range(1:n+2):
                sum2=sum2+t[i,j]*x[i,j,k]
            sum1=sum1+T[i]*y[i,k]+sum2
        boolean=(boolean and (sum1<=Tmax))
    return boolean

def constraint7(pi,l,m):
    boolean=True
    for k in range(m):
        for i in range (n+2):
            boolean=(boolena and (pi(i,k)<=l[i]))
    return boolean

def status(m,n,x,y,p,T,t,pi,d,l,M,Q,Tmax):
    obj=objective(p,y,m,n)
    boolean=(constraint1(x,m,n) and constraint2(x,y,m,n) and constraint3(x,pi,m,n,M) and constraint4(y,m,n))
    boolean=(boolean and constraint5(d,y,m,n,Q) and constraint6(x,y,m,n,T,t) and constraint7(pi,l,m))
    return (obj,boolean)
    
