import random

MAX_PATTERN_LENGTH = 10

# Generate a random number pattern
def generate_pattern(length):
    return [random.randint(0, 99) for _ in range(length)]

# Display the pattern to the user
def display_pattern(pattern):
    print("Pattern:", " ".join(map(str, pattern)))

# Get the user's input pattern
def get_user_pattern(length):
    user_input = input("Enter the pattern (separate numbers with spaces): ")
    return list(map(int, user_input.split()[:length]))

# Compare the user's pattern with the actual pattern
def compare_patterns(user_pattern, pattern):
    return user_pattern == pattern

def main():
    print("Welcome to the Number Pattern Prediction Game!")

    while True:
        # Generate a random pattern
        pattern = generate_pattern(MAX_PATTERN_LENGTH)
        
        # Display the pattern to the user
        display_pattern(pattern)

        # Get the user's input pattern
        user_pattern = get_user_pattern(MAX_PATTERN_LENGTH)

        # Compare the user's pattern with the actual pattern
        correct = compare_patterns(user_pattern, pattern)

        # Give the user feedback
        if correct:
            print("Correct! You matched the pattern.")
        else:
            print("Incorrect! Your pattern does not match.")

if __name__ == "__main__":
    main()
