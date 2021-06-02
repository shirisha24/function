print("welcome")
print("insert card")
print("1=english")
print("2=hindhi")
print("3=telugu")
lang=int(input("select lang"))
pin=2429
money=4000
if lang==1:
    print("english")
elif lang==2:
    print("hindhi")
elif lang==3:
    print("telugu")
trans=("withdraw,balance,deposite,pinchange,quit")
pin=int(input("enter pin"))
if pin==2429:
    print("1=withdraw")
    print("2=balance")
    print("3=deposite")
    print("4=pin change")
    print("5=quit")
    trans=input("select transaction")
    if trans=="1":
        amount=int(input("enter your amount"))
        if amount<=money:
            print("collect your cash")
            mny=money-amount
            print(mny)
        else:
            print("enter valid amount")
    elif trans=="2":
        slip=input("do u want receipt")
        if slip=="yes":
            print("here is your receipt")
        else:
            print("thank you")
    elif trans=="3":
        dep=int(input("enter your deposite money"))
        if dep>0:
            print("succesfully your amount is deposited")
            money=money+dep
            print(money)
        else:
            print("enter valid amount")
    elif trans=="4":
        pinchange=int(input("enter new pin"))
        if pinchange>=0:
            print("pin changed succesfully")
        else:
            print("enter valid num")
    elif trans=="5":
        q=input("do u want quit")
        if q=="yes":
            print("quit")
        else:
            print("enter any transaction")
else:
    print("wrong pin")