def fun():
    n=int(input("enter num"))
    a=[]
    b=[]
    i=1
    while i<=n:
        if i%2!=0:
            a.append(i)
        else:
            b.append(i)
        
            
        i=i+1
    print(a)
    print(b)
fun()