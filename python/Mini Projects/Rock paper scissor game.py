#Rock-paper-scissor game.
import random
while True:
    print("Rock-paper-scissor game.")
    print("1-Let's play.")
    print("2-Exit.")
    choice=int(input("What would you like to do?"))
    if choice==1:
        print("1.Rock")
        print("2.Paper")
        print("3.Scissor")
        option=int(input("what qould you like to choose?"))
        n=random.randint(1-3)
        if n==1&option==1:
            print("Both were rock.")
        elif n==1&option==2:
            print("you")
