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
