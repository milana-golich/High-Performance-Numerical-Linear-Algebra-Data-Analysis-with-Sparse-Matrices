import numpy as np
from numpy import loadtxt
from scipy import sparse
from scipy.sparse.linalg import splu
from scipy.linalg import logm

#A = np.zeros((27565,27565),dtype=int)
#print(A)

#C = np.zeros((27565,27565),dtype=int)
#print(C)

#f1 = open('149_5s.txt', 'r')
#data1 = f1.read()

#D = np.array(data1)
#print(D)
#print(data1)

f2 = open('149_6s.txt', 'r')
data2 = f2.read()
#print(data2)
#np.savetxt('test1.txt', data1, fmt='%d')
#B = np.loadtxt('test1.txt', dtype=int)
#print(B)
#print(B)
#np.save('data_149_5s.npy', np.array(data))
#D = np.load('data_149_5s.npy')
#data['data1']
#print(data)
B = np.array(data2);
type(B)
#print(len(B))
#print(len(D))

i=0
while i<len(B):
    A[i][B[i][0]-1]=-1
    A[i][B[i][1]-1]=-1
    A[i][B[i][2]-1]=-1
    A[i][B[i][3]-1]=-1
    A[i][B[i][4]-1]=-1
    A[i][B[i][5]-1]=-1
    i=i+1
print(A)
tr = A.trace()
print(tr)

i=0
while i<len(D):
    C[i][D[i][0]-1]=1
    C[i][D[i][1]-1]=1
    C[i][D[i][2]-1]=1
    C[i][D[i][3]-1]=1
    C[i][D[i][4]-1]=1
    i=i+1
print(C)
tr = C.trace()
print(tr)

M = A+C
print(M)
