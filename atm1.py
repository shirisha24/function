transaction=["withdraw","balance enquiry","deposite","quit"]
balance=5000
pin=int(input("enter pin"))
def main_fun():
    print("welcome")
    print("insert card")
def opt_fun():
    i=0
    while i<len(transaction):
        print(i+1,transaction[i])
        i=i+1
def option_fun(opt):
    if opt==1:
        withdraw_fun()
    elif opt==2:
        deposite_fun()
    elif opt==3:
        balance_fun()
    elif opt==4:
        quit_fun()
def withdraw_fun():
    amount=int(input("enter amount"))
    # pin=int(input("enter pin"))
    if pin==2429:
        a=balance-amount
        print("collect your cash")
        print("in your bank",a,"is left")
    else:
        print("wrong pin")
def deposite_fun():
    amount1=int(input("how much money u want ,u deposite"))
    pin=int(input("enter pin"))
    if pin==2429:
        b=balance+amount1
        print("ur deposite is succesfull")
        print("now your balanceis",b)
    else:
        print("wrong pin")
def balance_fun():
    pin=int(input("enter pin"))
    if pin==2429:
        print("ur balanceis",balance)
    else:
        print("wrong pin")
def quit_fun():
    print("quit")
main_fun()
lan=input("enter lang")
opt=int(input("enter option"))
option_fun(opt)