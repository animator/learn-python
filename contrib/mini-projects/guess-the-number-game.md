# Guess the Number 
This Python script is a simple number guessing game where a player must guess a randomly generated number within a specified range and limited number of tries.
## Components of the Script: 
- Import Libraries: <br>
 'random' for generating random numbers , 'math' for mathematical calculations.<br>
 
 - Input Range: <br>
 The user is prompted to enter the lower and upper bounds for the game, thereby defining the range from which the random number will be generated.

- Random Number Generation:<br>
A random integer x is generated between the user-defined lower and upper bounds using random.randint(lower, upper).
- Calculate Maximum Guesses:
The script calculates the maximum number of guesses allowed using the formula round(math.log(upper - lower + 1, 2)). This is based on the binary search algorithm, where the logarithm (base 2) of the range size gives the maximum number of guesses needed to guarantee a find.

- Outcome:
If the player fails to guess the number within the allowed attempts, the game reveals the correct number and prints a message encouraging better luck next time.

## Use Case:
The script is straightforward and can be run in any Python environment like an IDE (PyCharm) or a simple terminal session. It’s good for learning basic programming concepts such as loops, conditionals, input/output operations, and using libraries.

 ### Below is the code 
     import random
     import math
    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))

    # Taking Inputs
    upper = int(input("Enter Upper bound:- "))

    # generating random number between
    # the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ", 
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

    # Initializing the number of guesses.
    count = 0

    # for calculation of minimum number of
    # guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

    # Better to use This source Code on pycharm!
