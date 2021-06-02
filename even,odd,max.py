def maximum(num1):
    i=0
    max1=0
    while i<len(num1):
        if num1[i]>max1:
            max1=num1[i]
        i=i+1
    return max1
print(maximum([2,4,6,8,10,12,14,16,18,20]))
def new_list(a,b):
    c=a+b
    j=maximum(c)
    return j
def even_odd(list1):
    even=[]
    odd=[]
    i=0
    while i<len(list1):
        if list1[i]%2==0:
            even.append(list1[i])
        else:
            odd.append(list1[i])
        i=i+1
    print(even)
    print(odd)
    d=new_list(even,odd)
    print(d)
even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,599,670])
