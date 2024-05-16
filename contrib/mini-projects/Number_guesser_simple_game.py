nl=[]
print('Welcome to Guess the Number\n')
print("How to play?")
print()
print("1.Player inputs number of digits and a random number with those many digits is generated. The digits DO NOT repeat.")
print("2.Player has to keep entering guesses(what they think the number might be) while the computer confirms whether the entered digits match the generated number or not until they input the rigt number")
print("3.No. of chances is 3 times the number of digits the number and initial score is 10 times the number of chances(ex: 2 digit no.:6 chances:60 points, 3 digit no.:9 chances:90 points) but with each guess you take your score down by 10.")
print("4.To exit at any point press 'e' when guess is asked but the game will be considered lost and score will be 0 for exiting midway")
print()
import random
x=int(input("Enter number of digits you want the number to be(between 1 to 10): "))
while x<1 or x>10:
    print("Sorry input a number between 1 to 10")
    x=int(input("Enter number of digits you want the number to be(between 1 to 10): "))
while True:
    n=str(random.randint(10**(x-1),(10**x)-1))
    for i in n:
         if n.count(i)!=1:
             break
    else:
        break
count=0;g9=(x*30)
print("Initial score: ",g9)
print("No. of chances: ",x*3)
print()
for i in range(x*3):
    while True:
        gn=input("Enter your guess: ")
        if gn not in nl:
            break
        else:
            print("Number already inputed.Please re-enter")
    nl.append(gn)
    count+=1
    if gn==n:
        print("Congrats you guessed the number!")
        print("No. of turns taken: ",count)
        print("Coins: ",g9,'\n\nGAME OVER')
        break
    else:
        if gn=='e':
             score=0
             break
        else:
            for i in range (len(n)):
                if gn[i] in n:
                    if gn[i]==n[i]:
                        print(gn[i],": Correct digit, Correct place")
                    else:
                        print(gn[i],": Correct digit, Wrong place")
                else:
                    print(gn[i],": Wrong digit")
            print("Chances left: ",(x*3)-count)
            print()
            g9-=10
if g9==0:
    print("The number was",n)
    print("You lost")
    print("You get 0 coins\n\nGAME OVER")

