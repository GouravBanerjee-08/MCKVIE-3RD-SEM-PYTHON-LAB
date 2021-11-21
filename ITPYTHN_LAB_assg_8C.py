def rotatelist(l,k):
    for i in range(k):
        b=l.pop()
        l.insert(0,b)
    print(l)
l=list(input("Enter the list : "))
k=int(input("Enter the number of rotations - "))
rotatelist(l,k)