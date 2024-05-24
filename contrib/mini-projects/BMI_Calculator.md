# BMI Calculator

## Overview
This Python script calculates and interprets the Body Mass Index (BMI) based on user input for weight and height. The BMI is calculated using the formula: 
$BMI = \frac{weight \: (kg)}{(height \: (m))^2}$


## Functions

### `calculate_bmi(weight, height)`
Calculates the BMI based on the provided weight and height.

- **Parameters:**
  - `weight` (float): The weight in kilograms.
  - `height` (float): The height in meters.

- **Returns:**
  - `bmi` (float): The calculated BMI.

### `interpret_bmi(bmi)`
Interprets the BMI value and returns the corresponding category.

- **Parameters:**
  - `bmi` (float): The calculated BMI.

- **Returns:**
  - `interpretation` (str): The BMI category, which can be:
    - "Underweight" for BMI < 18.5
    - "Normal weight" for 18.5 ≤ BMI < 24.9
    - "Overweight" for 25 ≤ BMI < 29.9
    - "Obesity" for BMI ≥ 30

## Main Script

### Description
The main part of the script prompts the user for their weight and height, calculates the BMI, displays the result, and provides an interpretation of the BMI.

### Steps
1. Prompt the user to enter their weight in kilograms.
2. Prompt the user to enter their height in meters.
3. Call the `calculate_bmi` function to compute the BMI.
4. Print the calculated BMI.
5. Call the `interpret_bmi` function to get the BMI interpretation.
6. Print the interpretation.
7. Handle any `ValueError` exceptions if the user enters invalid input.

## Usage
To run the script,save the file as ```bmi_calculator.py``` and execute the following command in your terminal or command prompt:

```sh
python bmi_calculator.py
```

## Example
```
Enter your weight in kilograms: 70
Enter your height in meters: 1.75
Your BMI is: 22.86
Interpretation: Normal weight
```

## Python Code

```python
def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    # Interpret BMI
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    # Prompt user for weight and height
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Display calculated BMI
        print(f"Your BMI is: {bmi:.2f}")
        
        # Display BMI interpretation
        interpretation = interpret_bmi(bmi)
        print(f"Interpretation: {interpretation}")
        
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
```
