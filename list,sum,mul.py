list1=[[1,2,3,4],[2,3,4]]
i=0
sum=0
mul=1
while i<len(list1):
    j=0
    while j<len(list1[i]):                    
        if i==0:
            sum=sum+list1[i][j]
        elif i==1:
            mul=mul*list1[i][j]
        j=j+1
    i=i+1
print(sum)
print(mul)
        