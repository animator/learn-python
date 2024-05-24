# about password strength

> This code is a simple password strength checker. 
It evaluates the strength of a user's password based on the presence of 
uppercase letters, lowercase letters, digits, spaces, and special characters. 

### About the code:

- The codebase is break down in two file `password_strength_checker.py` and `main.py`.

`password_strength_checker.py` The function evaluates password strength based on character types (uppercase, lowercase, digits, spaces, special characters) and provides feedback on its security.
and `main.py` contains basic code.

```
import string


class password_checker:
    def __init__(self, password):
        self.password = password

    def check_password_strength(self):
        """This function prompts the user to enter a password and then evaluates its strength."""

        password_strength = 0
        upper_count = 0
        lower_count = 0
        num_count = 0
        space_count = 0
        specialcharacter_count = 0
        review = ""

        for char in list(password):
            if char in string.ascii_uppercase:
                upper_count += 1
            elif char in string.ascii_lowercase:
                lower_count += 1
            elif char in string.digits:
                num_count += 1
            elif char == " ":
                space_count += 1
            else:
                specialcharacter_count += 1

        if upper_count >= 1:
            password_strength += 1
        if lower_count >= 1:
            password_strength += 1
        if num_count >= 1:
            password_strength += 1
        if space_count >= 1:
            password_strength += 1
        if specialcharacter_count >= 1:
            password_strength += 1

        if password_strength == 1:
            review = "That's a very easy password, Not good for use"
        elif password_strength == 2:
            review = (
                "That's a weak password, You should change it to some strong password."
            )
        elif password_strength == 3:
            review = "Your password is just okay, you may change it."
        elif password_strength == 4:
            review = "Your password is hard to guess."
        elif password_strength == 5:
            review = "Its the strong password, No one can guess this password "

        about_password = {
            "uppercase_letters ": upper_count,
            "lowercase_letters": lower_count,
            "space_count": space_count,
            "specialcharacter_count": specialcharacter_count,
            "password_strength": password_strength,
            "about_password_strength": review,
        }
        print(about_password)

    def check_password():
        """This function prompts the user to decide if they want to check their password strength."""

        choice = input("Do you want to check your password's strength? (Y/N): ")
        if choice.upper() == "Y":
            return True
        elif choice.upper() == "N":
            return False
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
            return password_checker.check_password()

```
### Here's the implementation of 'main.py'
```
import password_checker from password_strength_checker

while password_checker.check_password():
    password = input("Enter your password: ")
    p = password_checker(password)
    p.check_password_strength()
```