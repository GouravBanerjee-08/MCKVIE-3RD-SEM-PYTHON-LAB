r=eval(input("Enter the Number of Rows : "))
for i in range(r):
    k=1
    for s in range ( r-i-1):
        print(" ",end='')
    for j in range(i+1):
        print(k,end='')
        k+=1
    print()