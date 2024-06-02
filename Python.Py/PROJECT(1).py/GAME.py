#                          Project 1
#       Snake, Water, Gun Game We all have played snake, water gun game in our childhood.
#               If you haven’t, google the rules of this game and
#            write a Python program capable of playing this game with the user.

import random
def game(comp,you):
    if comp==you:
        return None
    
    elif comp==1:
        if you==2:
            return False
        else:
            return True
        
    elif comp==2:
        if you==3:
            return False
        else:
            return True
        
    elif comp==3:
        if you==1:
            return False
        else:
            return True
    

print("computer's Turn : sanke(1) , water(2) , gun(3)")
comp=random.randint(1,3)

you=int(input("Enter snake(1) , water(2) , gun(3)"))
a=game(comp,you)

print(f"Computer's choice : {comp}")
print(f"your's choice :{you}")

if a==None:
    print("Game is Tie")
elif a:
    print("Congratulation You Won !")
else:
    print("Computer won this time")
    