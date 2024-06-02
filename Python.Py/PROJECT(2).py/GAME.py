'''                            Project 2: The Perfect Guess
We are going to write a program that generates a random number and asks the user to guess it.
If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly,
if the user’s guess is too low, the program prints “higher number please”.When the user guesses the correct number, 
the program displays the number of guesses the player used to arrive at the number.
                                Hint: Use the random module'''
import random
randNumber = random.randint(1,100)
userGuess=None
guesses=0
while(userGuess!= randNumber):
    userGuess = int(input("Enter Your Guess : "))
    guesses +=1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guesed it wrong! Enter a samller number")
        else:
            print("You guessed it wrong! Enter a larger number")
    
print(f"You guessed the number in {guesses} guesses")