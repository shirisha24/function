# global scope:-if we use global keyword,variable belongs to global scope(local)
x="siri"
def fun():
    global x
    x="is a sensitive girl"
fun()
print("chinni",x)

# works on(everyone) outside and inside(global)
x=2
def fun():
    global x
    x=x+x
    print(x)
fun()
print(x)


# another example
x=9
def fun() :
    
    global x
    x=4
    x=x+x
    print(x) 
fun()