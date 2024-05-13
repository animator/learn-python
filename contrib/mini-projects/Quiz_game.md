# Basic Quiz Game

This is a simple quiz game where players can choose from different genres of quizzes such as Sports, Entertainment, Physics, Chemistry, and Biology. Each genre contains five questions related to the chosen category. Players input their answers, and the program provides feedback on whether the answer is correct or incorrect along with the final score.

## Prerequisite
1. Basic Python
2. Decision Control
3. Nested Loops
4. List data structure
## Source Code

### Importing necessary libraries

```python

import time

```

### Main Code

```python

print("******************WELCOME TO ULTIMATE QUIZ GAME******************")

flag = 0
while flag == 0:
    # Display menu for selecting quiz genre
    print("Select your genre of quiz")
    print('''
    1. Sports
    2. Entertainment
    3. Physics
    4. Chemistry
    5. Biology
    6. Exit
    ''')
    genre = input("")

    # If user chooses to exit
    if genre == "6":
        flag = 1
    # If user chooses a quiz genre
    elif genre in ["1", "2", "3", "4", "5"]:
        print(f"Let's start the {['Sports', 'Entertainment', 'Physics', 'Chemistry', 'Biology'][int(genre) - 1]} Quiz.....")
        time.sleep(1.5)
        print("3")
        time.sleep(1.5)
        print("2")
        time.sleep(1.5)
        print("1")
        print(f"Welcome to the {['Sports', 'Entertainment', 'Physics', 'Chemistry', 'Biology'][int(genre) - 1]} Quiz!")

        score = 0

```

### Creating list of questions, options and correct answer
```python
        # Questions, options, and answers for each genre
        quiz_data = [
            # Sports
            [("In which sport would you perform a 'slam dunk'?", ["1. Basketball", "2. Soccer", "3. Tennis"], "1"),
             ("Which sport is known as the 'king of sports' or 'king of games'?", ["1. Soccer", "2. Tennis", "3. Cricket"], "3"),
             ("How many players are there on a baseball team?", ["1. 9", "2. 11", "3. 7"], "1"),
             ("Who holds the record for the most Grand Slam titles in tennis (men's singles)?", ["1. Roger Federer", "2. Rafael Nadal", "3. Novak Djokovic"], "1"),
             ("How many rings are there on the Olympic flag?", ["1. 6", "2. 5", "3. 7"], "2")],

            # Entertainment
            [("What is the real name of Iron Man?", ["1. Tony Stark", "2. Steve Rogers", "3. Bruce Banner"], "1"),
             ("Who played the lead role in the Bollywood movie 'Dangal'?", ["1. Aamir Khan", "2. Salman Khan", "3. Shah Rukh Khan"], "1"),
             ("What is the real name of Captain America?", ["1. Tony Stark", "2. Steve Rogers", "3. Bruce Banner"], "2"),
             ("Who directed the Bollywood movie 'Gully Boy'?", ["1. Karan Johar", "2. Zoya Akhtar", "3. Anurag Kashyap"], "2"),
             ("What is the name of the actor who played the character 'Wolverine' in the X-Men movies?", ["1. Hugh Jackman", "2. Robert Downey Jr.", "3. Chris Evans"], "1")],

            # Physics
            [("What is the SI unit of force?", ["1. Newton", "2. Joule", "3. Watt"], "1"),
             ("What is the speed of light in a vacuum?", ["1. 299,792,458 m/s", "2. 3.00 × 10^8 m/s", "3. Both options are correct"], "3"),
             ("What is the acceleration due to gravity on the surface of the Earth?", ["1. 9.8 m/s^2", "2. 10 m/s^2", "3. 9.81 m/s^2"], "3"),
             ("What is the unit of electric current?", ["1. Ampere", "2. Volt", "3. Ohm"], "1"),
             ("What is the SI unit of power?", ["1. Watt", "2. Joule", "3. Newton"], "1")],

            # Chemistry
            [("What is the chemical symbol for oxygen?", ["1. O", "2. Ox", "3. Os"], "1"),
             ("What is the pH value of pure water at room temperature?", ["1. 6", "2. 7", "3. 8"], "2"),
             ("Which element has the atomic number 6?", ["1. Nitrogen", "2. Carbon", "3. Oxygen"], "2"),
             ("What is the chemical formula for table salt?", ["1. NaCl", "2. HCl", "3. NaOH"], "1"),
             ("What is the process called when a gas turns into a liquid?", ["1. Evaporation", "2. Condensation", "3. Sublimation"], "2")],

            # Biology
            [("What is the powerhouse of the cell?", ["1. Nucleus", "2. Mitochondria", "3. Ribosome"], "2"),
             ("Which gas do plants use in photosynthesis?", ["1. Oxygen", "2. Carbon Dioxide", "3. Nitrogen"], "2"),
             ("Which organ produces insulin in the human body?", ["1. Liver", "2. Kidneys", "3. Pancreas"], "3"),
             ("What is the largest organ in the human body?", ["1. Liver", "2. Skin", "3. Heart"], "2"),
             ("What is the basic unit of heredity?", ["1. Chromosome", "2. Gene", "3. Allele"], "2")]
        ]

```

### Iterating over each item in the list above based on selected genre

```pyhton

        # Iterate over each question, display options, and check answers
        for question, options, answer in quiz_data[int(genre) - 1]:
            print(f"\nQuestion: {question}")
            for option in options:
                print(option)
            user_answer = input("Your answer (Enter 1, 2, or 3): ")
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
```
### Giving the final score

```python
        # Print final score
        print(f"\nYour score is: {score}/5")
        time.sleep(2)  # Pause for 2 seconds before returning to the menu


```
