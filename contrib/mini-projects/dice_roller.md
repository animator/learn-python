## Dice Roller

The aim of this project is to replicate a dice and generate a random number from the numbers 1 to 6.

For this first we will import the random library which will help make random choices.

```
import random
def dice():
  dice_no = random.choice([1,2,3,4,5,6])
  return "You got " + str(dice_no)
```

The above snippet of code defines a function called `dice()` which makes the random choice and returns the number that is generated.

```
def roll_dice():
  print("Hey Guys, you will now roll a single dice using Python!")
  while True:
    start=input("Type \'k\' to roll the dice: ").lower()
    if start != 'k':
      print("Invalid input. Please try again.")
      continue
    print(dice())
    roll_again = input("Do you want to reroll? (Yes/No): ").lower()
    if roll_again != 'yes':
      break
  print("Thanks for rolling the dice.")
roll_dice()
```

The above code defines a function called `roll_dice()` which interacts with the user.

It prompts the user to give an input and if the input is `k`,the code proceeds further to generate a random number or gives the message of invalid input and asks the user to try again.

After the dice has been rolled once, the function asks the user whether they want a reroll in the form of a `yes` or `no` question. The dice is rolled again if the user gives `yes` as an answer and exits the code if the user replies with anything other than yes.
