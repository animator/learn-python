# Password Generator
## Code

```
import random

import random
import string

def generate_password(length, complexity):
    """
    Generate a random password.

    Parameters:
    length (int): Length of the password.
    complexity (int): Complexity of the password. (1: Only letters, 2: Letters and digits, 3: Letters, digits, and punctuation)

    Returns:
    str: Generated password.
    """
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity must be 1, 2, or 3.")
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    """
    Main function to get user input and generate password.
    """
    try:
        length = int(input("Enter the desired password length: "))
        complexity = int(input("Enter the password complexity (1: Letters, 2: Letters and digits, 3: Letters, digits, and punctuation): "))
        
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length, complexity)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
```

## Code Explanation
