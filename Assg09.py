import calculator as cal 
while(True):
    print("Menu :\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Modulo\n")
    c=int(input("Enter your choice : "))
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b : "))
    if c==1:
        print(a," + ",b," = ",end=' ')
        print(cal.sum(a,b))
    elif c==2:
        print(a," - ",b," = ",end=' ')
        print(cal.subtract(a,b))
    elif c==3:
        print(a," * ",b," = ",end=' ')
        print(cal.multiply(a,b))
    elif c==4:
        print(a," / ",b," = ",end=' ')
        print(cal.divide(a,b))
    elif c==5:
        print(a," ^ ",b," = ",end=' ')
        print(cal.exp(a,b))
    elif c==6:
        print(a," % ",b," = ",end=' ')
        print(cal.mod(a,b))
    else:
        print("Wrong choice.")
    choice=int(input("Do you want to continue? IF 'YES' press 1 : "))
    if(choice!=1):
        break
