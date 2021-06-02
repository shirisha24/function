def fizzbuzz(n):
    if n%3==0 and n%5==0:
        return "fb"
    elif n%3==0:
        return "fizz"
    elif n%5==0:
        return "buzz"
    else:
        return "4"
print(fizzbuzz(15))
print(fizzbuzz(3))
print(fizzbuzz(5))