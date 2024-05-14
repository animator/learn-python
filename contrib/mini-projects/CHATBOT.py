import random

# Define responses for the chatbot
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

# Function to generate a response from the chatbot
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input matches any predefined responses
    for key in responses:
        if user_input in key:
            return random.choice(responses[key])
    
    # If no predefined response matches, return a default response
    return "I'm sorry, I didn't understand that."

# Main function to run the chatbot
def main():
    print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")
    
    # Chat loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
