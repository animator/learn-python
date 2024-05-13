```
import random
def dice():
  dice_no = random.choice([1,2,3,4,5,6])
  return "You got " + str(dice_no)
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
