import random

words=[['Animals','lion','tiger','zebra','giraffe','elephant','monkey','dolphin','penguin','kangaroo','hippopotamus'],
       ['Fruits','apple','banana','orange','grape','pineapple','watermelon','kiwi','mango','strawberry','cherry'],
       ['Countries','india','france','japan','brazil','australia','egypt','canada','germany','mexico','italy','cuba'],
       ['Sports','football','cricket','hockey','tennis','badminton','basketball','golf','volleyball','rugby'],
       ['Colours','purple','black','red','blue','green','orange','yellow','pink','brown','white','violet']]          #making a list of words with themes

def update_clue(guessed_letter, secret_word, secret):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:     
            secret[index] = guessed_letter         #updating the question marks with the guessed letter
        index = index + 1

heart=u'\u2764'     #creating a heart shaped symbol to denote the lives
score=0

print("Welcome to the Word Guessing Game.\nYou have three chances to guess a word based upon the theme given.\n"
      "Each correct guess give you one point. If you fail to guess a word, the game will end there.\n")

while True:
    lis=random.choice(words)
    secret_word=random.choice(lis[1::])      #selecting a random word from a theme
    secret=list('?'*len(secret_word))
    lives=3
    correct=False
    while lives!=0:
        print("Theme Chosen: {}\nThe secret word is {}.\nLives: {}\n".format(lis[0],secret,heart*lives))
        guess=input("Guess the whole word or a letter: ")
        if guess==secret_word:
            score+=1      #updating score for every correct guess
            correct=True
            break
        elif guess in secret_word:
            update_clue(guess,secret_word,secret)
        else:
            print("Incorrect! You lose a life.\n")      #subtracting a life for every incorrect guess
            lives-=1
        
    if correct:
        print("You guessed correctly! The Word is: {}\n".format(secret_word))
    else:
        print(("You could not guess correctly! The Word is: {}\n".format(secret_word)))
        print("Your final score is {}.".format(score))      #showing the score after a wrong guessed word
        break
