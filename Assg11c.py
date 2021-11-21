fp=open("11c","w")
a=-1
b=1
c=a+b
n=int(input("Enter the value of n : "))
while(c<=n):
    fp.write(str(c))
    fp.write(" ")
    a=b
    b=c
    c=a+b
fp.close()
