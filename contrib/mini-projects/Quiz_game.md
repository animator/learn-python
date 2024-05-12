# Basic Quiz Game

This is a simple Python script for a basic quiz game. It allows users to choose from different genres of quizzes including Sports, Entertainment, Physics, Chemistry, and Biology. The user selects a genre, and then answers multiple-choice questions related to that genre. After answering all the questions, the user's score is displayed.

```python

import time

print("******************WELCOME TO ULTIMATE QUIZ GAME******************")

flag = 0

while flag == 0:

    print("Select your genre of quiz")

    print('''

    1 .Sports

    2. Entertainment

    3. Physics

    4. Chemistry

    5. Biology

    6. Exit

    ''')

    genre = input("")

    if genre == "1":

        # Sports Quiz

        print("Lets start the quiz.....")

        time.sleep(1.5)

        print("3")

        time.sleep(1.5)

        print("2")

        time.sleep(1.5)

        print("1")

        print("Welcome to the Sports Quiz!")

        score = 0

        # Question 1

        print("\nQuestion 1: In which sport would you perform a 'slam dunk'?")

        print("1. Basketball")

        print("2. Soccer")

        print("3. Tennis")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "1":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Question 2

        print("\nQuestion 2: Which sport is known as the 'king of sports' or 'king of games'?")

        print("1. Soccer")

        print("2. Tennis")

        print("3. Cricket")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "3":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Question 3

        print("\nQuestion 3: How many players are there on a baseball team?")

        print("1. 9")

        print("2. 11")

        print("3. 7")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "1":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Question 4

        print("\nQuestion 4: Who holds the record for the most Grand Slam titles in tennis (men's singles)?")

        print("1. Roger Federer")

        print("2. Rafael Nadal")

        print("3. Novak Djokovic")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "1":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Question 5

        print("\nQuestion 5: How many rings are there on the Olympic flag?")

        print("1. 6")

        print("2. 5")

        print("3. 7")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "2":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Print score

        print("\nYour score is: {}/5".format(score))

        time.sleep(2)

    elif genre == "2":

        # Entertainment Quiz

        print("Let's start the Entertainment.....")

        time.sleep(1.5)

        print("3")

        time.sleep(1.5)

        print("2")

        time.sleep(1.5)

        print("1")

        print("Welcome to the Mixed Quiz!")

        score = 0

        # Question 1 (Marvel)

        print("\nQuestion 1: What is the real name of Iron Man?")

        print("1. Tony Stark")

        print("2. Steve Rogers")

        print("3. Bruce Banner")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "1":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Question 2 (Bollywood)

        print("\nQuestion 2: Who played the lead role in the Bollywood movie 'Dangal'?")

        print("1. Aamir Khan")

        print("2. Salman Khan")

        print("3. Shah Rukh Khan")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "1":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Question 3 (Marvel)

        print("\nQuestion 3: What is the real name of Captain America?")

        print("1. Tony Stark")

        print("2. Steve Rogers")

        print("3. Bruce Banner")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "2":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Question 4 (Bollywood)

        print("\nQuestion 4: Who directed the Bollywood movie 'Gully Boy'?")

        print("1. Karan Johar")

        print("2. Zoya Akhtar")

        print("3. Anurag Kashyap")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "2":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Question 5 (Mixed)

        print("\nQuestion 5: What is the name of the actor who played the character 'Wolverine' in the X-Men movies?")

        print("1. Hugh Jackman")

        print("2. Robert Downey Jr.")

        print("3. Chris Evans")

        user_answer = input("Your answer (Enter 1, 2, or 3): ")

        if user_answer == "1":

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")

        # Print score

        print("\nYour score is: {}/5".format(score))

        time.sleep(2)

    elif genre == "6":

        flag = 1

```