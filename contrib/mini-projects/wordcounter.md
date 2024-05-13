# Word Counter
This project counts the number of words entered in the input sentence and give the number (count) of words in output. 
Each element present in the text will be considered a letter, and a group of letters with a space will be considered a word. 
It takes string as input from user, and counts the total number of words in the string. This count is displayed as output.<br>
Sample Input:- Harry likes Open Source<br>
Sample Output:- 4<br>
Explaination:- The above sentence contain 4 words.<br>

# Components of the code:
The provided code defines a Python function count_words(sentence) aimed at counting the number of words in a given sentence. Here's a step-by-step description:

- ### Function Definition:

  The code begins with the definition of a function named count_words.
  It takes a single parameter sentence, representing the input string whose words are to be counted.
- ### Splitting the Sentence:

  Within the function, the input sentence is split into individual words using the split() method.
  The split() method divides the string into substrings based on whitespace characters (spaces, tabs, and newline characters) by default.
- ### Counting Words:

  The code determines the number of words in the sentence by calculating the length of the list generated from splitting the sentence.
  The len() function is utilized to compute the length of the list, which corresponds to the number of words in the sentence.
- ### Returning the Count:

  After determining the word count, the function returns this value.
- ### Example Usage:

  The script prompts the user to input a sentence using the input() function.
  It then calls the count_words function, passing the user's input as an argument, and stores the returned word count in the variable number_of_words.
  Finally, it prints out the number of words in the sentence.

        def count_words(sentence):
        # Split the sentence into words
        words = sentence.split()
    
        # Count the number of words
        word_count = len(words)
    
        return word_count
    
        # Example usage:
        sentence = input("Enter a sentence: ")
        number_of_words = count_words(sentence)
        print("Number of words:", number_of_words)
