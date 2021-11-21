
a=(input("Enter List Elements:")).split()
l=list(map(int,a))
print("Original List:",l)
d=dict()
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("Printing count of each item:",d)