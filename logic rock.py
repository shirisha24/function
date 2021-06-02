def rps(s1,s2):
    if s1==s2:
        return "TIE"
    elif s1=="rock":
        if s2=="paper":
            return "player 2 wins"
        else:
            return "player 1 wins"
    elif s1=="paper":
        if s2=="scissors":
            return "player 2 wins"
        else:
            return "player 1 wins"
    elif s1=="scissors":
        if s2=="rock":
            return "player 2 wins"
        else:
            return "player 1 wins"
print(rps("rock","paper"))
print(rps("paper","rock"))
print(rps("paper","scissors"))
print(rps("scissors","rock"))
print(rps("scissors","paper"))

# another model
def game(fp,sp):
    if fp==sp:
        print("TIE")
    elif fp=="rock" and sp=="paper":
        print("sp wins")
    elif fp=="paper" and sp=="rock":
        print("fp wins")
    elif fp=="paper" and sp=="scissors":
        print("sp wins")
    elif fp=="scissors" and sp=="paper":
        print("fp wins")
f=input("choose what u want")
s=input("choose what you want")
game(fp,sp)