r=eval(input("Enter the Number of Rows : "))
for i in range(0,r):
    for j in range (0,r):
        if(j==i or j==r-i-1):
            print("$",end=' ')
        elif(i==0 and j!=0 and j!=r-1):
            print("*",end=' ')
        elif(i==r-1 and j!=0 and j!=r-1):
            print("*",end=' ')
        elif(j==0 and i!=0 and i!=r-1):
            print("*",end=' ')
        elif(j==r-1 and i!=0 and i!=r-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()