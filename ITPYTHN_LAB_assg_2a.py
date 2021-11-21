'''SWAPPING OF NUMBERS'''
a=float(input("Enter the value for a:"))
b=float(input("Enter the value for b:"))

c=a
a=b
b=c
print("The number after swapping with a variable")
print("value of a :",a,"value of b :",b )

a=a+b
b=a-b
a=a-b
print("The number after swapping without variable")
print("value of a :",a,"value of b :",b )