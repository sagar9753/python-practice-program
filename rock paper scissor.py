#program for rock,paper,scissor game
import random
print("For rock enter 1 ")
print("For paper enter 2 ")
print("For scissor enter 3 ")

for i in range(6):
    comp=random.randint(1,3)
    plyr=int(input("\nEnter your choice : "))

    if(plyr>3):
        print("\nYou entered wrong choice,enter again :")
        plyr=int(input())

    print("\n--computer choice :",comp,"\n--Your choice : ",plyr)

    if(comp==1 and plyr==2 or comp==1 and plyr==3):
        print("\n ----**> You lose <**---")
    elif(comp==2 and plyr==3):
        print("\n ----**> You won <**----")
    elif(comp==2 and plyr==1 or comp==3 and plyr==1):
        print("\n ----**> You won <**----")
    elif(comp==3 and plyr==2):
        print("\n ----**> You lose <**---")
    else:
        print("\n Draw")


