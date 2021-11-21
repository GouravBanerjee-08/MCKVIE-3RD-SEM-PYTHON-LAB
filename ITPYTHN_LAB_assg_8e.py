s=input("Enter String:")
print("Original string is: ",s)
if(len(s)>7 and len(s)%2==1):
    mid=len(s)//2
    print("Middle three chars are:",s[mid-1:mid+2])
else:
    print("Invalid String")