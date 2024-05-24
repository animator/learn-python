# Password Generator
This Python script generates a random password based on user-defined criteria such as length and complexity. The code uses the `random` module to select characters and the `string` module to provide sets of characters (letters, digits, punctuation).

### Python Code

```python
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

## Key Components

### Imports

- `random`: For selecting random characters.
- `string`: For accessing predefined sets of characters.

### `generate_password` Function

- **Purpose**: Generates a random password.
- **Parameters**:
  - `length` (int): The length of the password.
  - `complexity` (int): Determines the types of characters included:
    - `1`: Letters only.
    - `2`: Letters and digits.
    - `3`: Letters, digits, and punctuation.
- **Logic**: Based on the complexity level, it creates a pool of characters and generates the password by randomly selecting characters from this pool.

### `main` Function

- **Purpose**: Handles user input and generates the password.
- **User Input**: Prompts the user to input the desired password length and complexity.
- **Validation**: Ensures the input is valid (length must be positive and complexity must be 1, 2, or 3).
- **Password Generation**: Calls the `generate_password` function with the user's inputs and prints the generated password.

### Script Execution

The `if __name__ == "__main__":` block ensures that the `main` function is executed only when the script is run directly, not when it is imported as a module.

## How the Code Works

1. **User Input**:
    - The user is asked to enter the desired length and complexity of the password.
    
2. **Password Generation**:
    - The script validates the input values.
    - Based on the complexity level, it selects the appropriate set of characters:
        - `1`: Uses only letters (`string.ascii_letters`).
        - `2`: Uses letters and digits (`string.ascii_letters + string.digits`).
        - `3`: Uses letters, digits, and punctuation (`string.ascii_letters + string.digits + string.punctuation`).
    - The `generate_password` function creates a password by randomly choosing characters from the selected set until the desired length is reached.
    
3. **Output**:
    - The generated password is printed to the console.

## Error Handling

- The script includes basic error handling to ensure the length is a positive integer and the complexity is within the acceptable range (1, 2, or 3).
- If invalid input is provided, an error message is displayed.

## Example Usage

When running the script, a user might see the following:

```plaintext
Enter the desired password length: 12
Enter the password complexity (1: Letters, 2: Letters and digits, 3: Letters, digits, and punctuation): 3
Generated Password: aB9!vX@2pQ1&
```
