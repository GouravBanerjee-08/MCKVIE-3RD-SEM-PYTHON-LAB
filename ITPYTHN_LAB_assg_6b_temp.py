import numpy as np

P=np.zeros((6),dtype='int')
for i in range(6):
  P[i]=eval(input("Enter the element of P:"))
print("The array P is:",P)

Q=np.zeros((4),dtype='int')
for i in range(4):
  Q[i]=eval(input("Enter the element of Q:"))
print("The array Q is:",Q)
Res=np.zeros((10),dtype='int')
for i in range(0,6):
  Res[i]=P[i]
for i in range(0,4):
  Res[6+i]=Q[i]
print("The resultant array is:",Res)