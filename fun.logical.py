def fun(a):
    def add(b):
        nonlocal a
        a=a+1
        return a+b
    return add
c=fun(4)
print(c(4))

# even
def even():
    i=0
    n=[]
    while i<len(a):
        if a[i]%2!=0:
            n.append(a[i])
        i=i+1
    print(n)
a=[1,2,3,4,5,6,7,8,9]
even()

# square

def sqr():
    i=1
    l=list()
    while i<21:
        l.append(i**2)
        i=i+1
    print(l)
sqr()
