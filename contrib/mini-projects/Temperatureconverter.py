import tkinter as tk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to handle conversion
def convert_temperature():
    if var.get() == "Celsius to Fahrenheit":
        try:
            celsius = float(entry.get())
            fahrenheit = celsius_to_fahrenheit(celsius)
            result_label.config(text=f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit")
        except ValueError:
            result_label.config(text="Please enter a valid number.")
    elif var.get() == "Fahrenheit to Celsius":
        try:
            fahrenheit = float(entry.get())
            celsius = fahrenheit_to_celsius(fahrenheit)
            result_label.config(text=f"{fahrenheit} Fahrenheit = {celsius:.2f} Celsius")
        except ValueError:
            result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create a label for the entry
entry_label = tk.Label(root, text="Enter temperature:")
entry_label.pack()

# Create an entry for temperature input
entry = tk.Entry(root)
entry.pack()

# Create a radio button for selecting conversion type
var = tk.StringVar()
var.set("Celsius to Fahrenheit")  # Default selection
radio_c_to_f = tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value="Celsius to Fahrenheit")
radio_c_to_f.pack()
radio_f_to_c = tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value="Fahrenheit to Celsius")
radio_f_to_c.pack()

# Create a button to trigger conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
