def language():
    if num==1:
        a="english"
    else:
        b="telugu"
    return num
num=int(input("choose your language,1.english,2.telugu"))
def pin_code():
    if num==1:
        i=0
        while i<3:
            pin=int(input("enter num"))
            if pin==2429:
                print("your pin is correct")
                break
            else:
                print("youe pin is incorrect")
            i=i+1
        else:
            print("card will block")
    else:
        i=0
        while i<3:
            pin=int(input("meeru pin cheyagalaru"))
            if pin_code==2429:
                print("mee pin correct")
                break
            else:
                print("medi invalid pin")
            i=i+1
    return pin
code=pin_code()
def options():
    if num==1:
        if code==2429:
            amount=5000
            print("press 1 for balance enquiry")
            print("press 2 for withdraw")
            print("press 3 for deposite")
            print("press 4 for exit")
            option=int(input("choose any option"))
            if option==1:
                c=amount,"your total amount"
            elif option==2:
                withdraw=int(input("enter your withdraw money"))
                c=amount-withdraw,"your total amount"
            elif option==3:
                deposite=int(input("enter your desposite money"))
                c=amount+deposite,"your total amount"
            else:
                c="please collect your card"
                print("tnq for visiting sir or madam")
            return c
    else:
        if code==2429:
            amount=5000
            print("total money koraku 1 press cheyandi")
            print("money withdraw koraku 2 press cheyandi")
            print("money veyataniki 3 press cheyandi")
            print("card tisukogalaru 4 press cheyandui")
            option=int(input("option enter cheyandi"))
            if option==1:
                c=amount,"mee total amount"
            elif option==2:
                withdraw=int(input("money withdraw cheyandi"))
                c=amount-withdraw,"mee total amount"
            elif option==3:
                deposite=int(input("mee deposite money enter cheyandi"))
                c=amount+deposite,"mee total amont"
            else:
                c="card enter cheyagalaru"
                print("dhanyavadamulu")
            return c
            
def main():
    print(language())
    print(options())
main()