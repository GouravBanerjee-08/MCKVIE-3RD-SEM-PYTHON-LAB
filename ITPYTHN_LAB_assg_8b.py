import math
def sumofsquares(m):
    k=int(math.sqrt(m))
    t=False
    for i in range (1,k+1):
        for j in range (1,k):
            if(pow(i,2) + pow(j,2)==m):
                t=True
    return(t)
b=int(input("Enter a positive number = "))
if(b<0):
    print("Wrong number")
else:
    print(sumofsquares(b))