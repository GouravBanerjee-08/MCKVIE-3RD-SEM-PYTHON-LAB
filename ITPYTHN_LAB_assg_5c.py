while(1):
    print(" press 1 for pattern 1\n press 2 for pattern 2\n press 3 for pattern 3\n press 4 to exit")
    char=input("Enter a character to choose a type of pattern: ")


    if(char=='1'):
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

    elif(char=='2'):

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

    elif(char=='3'):
        r=eval(input("Enter the Number of Rows : "))
        for i in range(r):
            k=1
            for s in range ( r-i-1):
                print(" ",end='')
            for j in range(i+1):
                print(k,end='')
                k+=1
            print()

    elif(char=='4'):
        exit()

    else:
        print("enter a valid choice")