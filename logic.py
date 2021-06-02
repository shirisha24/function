def calculatesum(num):
    if num:
        return num+calculatesum(num-1)
    else:
        return 0
res=calculatesum(5)
print(res)


# square
def sqr(num):
    num_sqr=num**2
    return num_sqr
my_sqrs=[]
for i in  range (0,5):
    my_sqrs.append(sqr(i))
print(my_sqrs)
