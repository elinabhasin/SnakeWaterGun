import time
import random

def choiceValid():
    while(True):
        print("Enter S for Snake\nW for Water\nG for Gun")
        userChoice=(input("Snake..Water..Gun..SHOOT : ")).lower()
        print("\n")
        if(userChoice!="s" and userChoice!='w' and userChoice!='g'):
            print("Invalid input!")
        else:
            return userChoice

def score(pts):
    ld=open("leaderboard.txt",'w')
    ld.write("Score-Card :".center(30))
    ld.close()
    with open("leaderboard.txt",'a') as ld:
        ld.write(f"\nUsername : {username}\nFinal pts : {pts}")

def round():
    print("Another round?")
    another=(input("Enter Y for yes , N for no : ")).lower()
    print("\n")
    match another:
        case 'y':
            pass
        case 'n':
            print("\n")
            with open("leaderboard.txt",'r') as ld:
                data=ld.read()
            print(data)
            exit()


username=input("Please enter your username : ")
pts=0

t=time.localtime()
hour=time.strftime("%H",t)

if("00"<=hour and hour<"12"):
    print(f"Good Morning {username}!")
    print("Ready to play?")
    ready=(input("Enter Y for yes , N for no : ")).lower()
    print("\n")
elif("12">=hour and hour<"16"):
    print(f"Good Afternoon {username}!")
    print("Ready to play?")
    ready=(input("Enter Y for yes , N for no : ")).lower()
    print("\n")
else:
    print(f"Good Evening {username}!")
    print("Ready to play?")
    ready=(input("Enter Y for yes , N for no : ")).lower()
    print("\n")

initials=["s","w","g"]
choices={"s":"snake","w":"water","g":"gun"}

while(True):
    if(ready!='y'):
        exit()
    else:
        pyChoice=random.choice(initials)
        userChoice=choiceValid()

        if(userChoice==pyChoice):
            print(f"Python chose : {choices[pyChoice]}")
            print(f"You chose : {choices[userChoice]}\n")
            print("Draw Game!\n")
            pts=pts+5
            print("+5 points!!")
            score(pts)
            round()

        elif((userChoice=='g' and pyChoice=='s') or (userChoice=="s" and pyChoice=="w") or (userChoice=="w" and pyChoice=="g")):
            print(f"Python chose : {choices[pyChoice]}")
            print(f"You chose : {choices[userChoice]}\n")
            print("Hurrah! You beat Python!!!\n")
            pts=pts+10
            print("+10 points!!")
            score(pts)
            round()

        else:
            print(f"Python chose : {choices[pyChoice]}")
            print(f"You chose : {choices[userChoice]}\n")
            print("You lose. Better luck next time :)\n")
            pts=pts+0
            print("+0 points!!")
            score(pts)
            round()
            


