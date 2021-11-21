def stringapp(s1,s2):
    m=(len(s1))//2
    s=s1[0:m]+s2+s1[m:]
    print("The resulting string will be =",s)
st1=input("Enter the 1st string = ")
st2=input("Enter the 2nd string = ")
stringapp(st1,st2)