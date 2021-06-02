list = [[1,2,3], [5,3,8,9], [4,3,77,521,31,311]]
i=0
j=0
c=[]
max=0
while i<len(list):
    if list[i][j]>max:
        max=list[i][j]
        while j<len(list[i]):
            if list[i][j]>max:
                max=list[i][j]
            j+=1
        i+=1
        c.append(max)
    print(max)
        
        
        
        
