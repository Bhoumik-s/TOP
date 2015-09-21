import numpy as np
from read_data import read, find_segments
#source:http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6887433

data=read("data.xlsx")  # read data
segments=find_segments(data[:,:2]) # calculates each segment time

n=data.shape[0] # number of points
k=4 # no. of days for visit
x=np.zeros((k,n,n), dtype=bool)
print x

