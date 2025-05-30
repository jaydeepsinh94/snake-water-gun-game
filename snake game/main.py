import random
def snake():
    computer = random.choice([-1,0,1])
    youchoice =input("enter your choice :")
    yourdict = {"s":1,"w":-1,"g":0}
    reversedict = {1:"snake",-1:"water",0:"gun"}

    you =yourdict[youchoice]

    print(f"you chose {reversedict[you]} \ncomputer chose {reversedict[computer]}")

    if(computer == you):
        print("its a draw !")

    else:
        if(computer ==-1 and you == 1):
            print("you win!")  

        elif(computer ==-1 and you ==0):
            print("you lose !")

        elif(computer ==1 and you ==-1):
            print("you lose !")

        elif(computer ==1 and you ==0):
            print("you win !")

        elif(computer ==0 and you ==-1):
            print("you win !")
    
        elif(computer ==0 and you ==1):
            print("you lose !")

        else:
            print("something went wrong !")   

snake()             
   

