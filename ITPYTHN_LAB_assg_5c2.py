n=eval(input("Enter the number of rows : "))
for i in range(n,0,-1):
    for j in range(i):
        print(chr(j+65),end=" ")
    for s in range(0,n-i):
        print(" ",end=" ")
    if i==n:
        for l in range(i-2,-1,-1):
            print(chr(l+65),end=" ")
    else:
        for m in range(n-i,1,-1):
            print(" ",end=" ")
        for k in range(i-1,-1,-1):
            print(chr(k+65),end=" ")
    print()
