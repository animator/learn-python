<div align="center">
<h2>Building a Simple Expense Tracker application with Python</h2>
</div>

## Objective
<p>To develop a GUI-based expense tracker application with python to record and categorize daily expenses, storing the data in an SQLite database.
            An expense tracker application with python is a useful tool that allows you to record and categorize your daily expenses in a convenient and organized manner. It provides a user-friendly interface for entering and managing your expenses, making it easier to track your spending habits and financial goals.</p>

## Requirements

<p>1- Sqlite3</p>
<p>2- pip install</p>
<p>3- tkinter</p>

## Steps
## Step1- Initialize SQLite Database in Python
 <p>Create a project folder named “expense-trackerb” and create a python file “expense-tracker.py” inside the folder
Import Tkinter and sqlite3 and create a new SQLite database named expenses.db and for storing expenses.</p>

```python
#expense-tracker/expense-tracker.py
import tkinter as tk
from tkinter import ttk
import sqlite3
conn = sqlite3.connect('expenses.db')
```
## Explaination
1. <p>The line <b>conn = sqlite3.connect('expenses.db')</b>establishes a connection to a SQLite database named expenses.db.</p>
2. <p>If you run this file now then you should have following structure:</p>
3.  expense-tracker
    - `expense-tracker.py`
    -  `expenses.db`


## Step2- Create data table in Python
<p>Check if table 'expenses' exists in the database else create the data table with the columns id, category and date</p>

```python
cursor = conn.cursor()
res = cursor.execute("SELECT name FROM sqlite_master WHERE name='expenses'")
if res.fetchone() is None:
    cursor.execute(
        '''CREATE TABLE expenses (id INTEGER PRIMARY KEY,
        category TEXT,  amount REAL,
        date TEXT)'''
        )
```

## Explaination
1.  `cursor = conn.cursor():` This line creates a cursor object associated with the database connection conn. A cursor allows you to execute SQL queries on the database.
2. `res = cursor.execute("SELECT name FROM sqlite_master WHERE name='expenses'"):` Here, you're executing a SQL query to check if a table named "expenses" exists in the database. The sqlite_master table is a system table that stores metadata about all tables and indexes in the database. This query selects the name of any table in the database where the name is 'expenses'.
3. if `res.fetchone() is None::` After executing the query, <b>res.fetchone() </b>retrieves the next row of the query result set. If there are no rows returned by the query (i.e., fetchone() returns None), it means the table "expenses" does not exist.
4. Inside the if block, you're creating the "expenses" table using the cursor.execute() method. The table has four columns:
    - `id as an INTEGER PRIMARY KEY:` This column serves as the primary key for uniquely identifying each row in the table. It's set to auto-increment, meaning its value is automatically generated for each new row.
   - `amount as REAL:` This column stores the amount of the expense as a real number (floating-point).
   - `date as TEXT:` This column stores the date of the expense as text.

 ## Step3- Create GUI Layout
<p>Create the basic Tkinter layout with entry fields for category, amount, and date.</p>


```python
window = tk.Tk()
window.title("Expense Tracker")frame = ttk.Frame(window, padding="10")

frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))tk.Label(frame, text="Category").grid(row=0, column=0)
tk.Label(frame, text="Amount").grid(row=1, column=0)
tk.Label(frame, text="Date").grid(row=2, column=0)category = tk.StringVar()
amount = tk.DoubleVar()
date = tk.StringVar()category_entry = ttk.Entry(frame, textvariable=category)
amount_entry = ttk.Entry(frame, textvariable=amount)
date_entry = ttk.Entry(frame, textvariable=date)category_entry.grid(row=0, column=1)
amount_entry.grid(row=1, column=1)
date_entry.grid(row=2, column=1)
```

## Explaination
1. `window = tk.Tk():` This line creates the main application window using the Tk() constructor from the Tkinter module. This window will contain all the graphical elements of the application.
2. `window.title("Expense Tracker"):` This line sets the title of the window to "Expense Tracker".
3. `frame =ttk.Frame(window, padding="10"):` This line creates a frame widget within the main window. Frames are used to organize and group other widgets together. The padding="10" argument adds padding of 10 pixels around the frame.
4. `frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S)):` This line specifies the grid layout for the frame within the main window. It places the frame in row 0 and column 0 of the window, and the sticky parameter ensures that the frame expands in all directions (west, east, north, south) to fill the available space
5. The next few lines create labels and entry widgets for entering expense details:
   - `tk.Label(frame, text="Category").grid(row=0, column=0):` Creates a label widget with the text "Category" and places it in row 0, column 0 of the frame.</li>
   - `tk.Label(frame, text="Amount").grid(row=1, column=0):`Creates a label widget with the text "Amount" and places it in row 1, column 0 of the frame.</li>
   - `tk.Label(frame, text="Date").grid(row=2, column=0):` Creates a label widget with the text "Date" and places it in row 2, column 0 of the frame.</li>
6. `category = tk.StringVar(), amount = tk.DoubleVar(), date = tk.StringVar():` These lines create Tkinter variables to store the values entered into the entry widgets. StringVar() is used for text-based input (category and date), while DoubleVar() is used for numerical input (amount).<
7. `category_entry = ttk.Entry(frame, textvariable=category), amount_entry = ttk.Entry(frame, textvariable=amount), date_entry = ttk.Entry(frame, textvariable=date):` These lines create entry widgets (text input fields) associated with the respective variables (category, amount, date) created earlier. The textvariable parameter is used to link the entry widget to the corresponding Tkinter variable
8. `category_entry.grid(row=0, column=1), amount_entry.grid(row=1, column=1), date_entry.grid(row=2, column=1): `These lines place the entry widgets in the second column of the grid layout within the frame, aligned with the respective labels
   
## Step4- Add Functionality
<p>Add the function to add an expense to the database.</p>

```python
def add_expense():
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
    (category.get(), amount.get(), date.get()))
    conn.commit()add_button = ttk.Button(frame, text="Add Expense", command=add_expense)
    add_button.grid(row=3, columnspan=2)
```
## Explaination
1. `def add_expense()::` This line defines a function named add_expense(). This function is intended to handle the addition of expenses to the database when the corresponding button is clicked.
2. `cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)", (category.get(), amount.get(), date.get())):` This line executes an SQL INSERT statement to add a new expense to the "expenses" table in the SQLite database. The values to be inserted are obtained from the respective Tkinter variables (category, amount, date) using their get() methods.
3. `conn.commit():` This line commits the transaction to the database. It ensures that the changes made by the INSERT statement are saved permanently in the database.
4. `add_button = ttk.Button(frame, text="Add Expense", command=add_expense):` This line creates a Tkinter button widget with the text "Add Expense" and associates it with the add_expense() function. So, when the button is clicked, the add_expense() function will be called to add the expense to the database.
5. `add_button.grid(row=3, columnspan=2):` This line specifies the grid layout for the button within the Tkinter frame. It places the button in row 3 and spans it across two columns.

## Step5- Display Expenses
<p>Create a function to display the expenses. It includes a query to fetch the expenses from the table and display on the console.</p>

```python
    def display_expenses():
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(f"ID: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}, Date: {expense[3]}")display_button = ttk.Button(frame, text="Display Expenses", command=display_expenses)
            display_button.grid(row=4, columnspan=2)
```
## Explaination
1. `def display_expenses()::` This line defines a function named display_expenses().
2. `cursor.execute("SELECT * FROM expenses"):` This line executes an SQL SELECT statement to retrieve all columns (*) from all rows in the "expenses" table.
3. `expenses = cursor.fetchall():` This line fetches all the rows returned by the SELECT query and stores them in the variable expenses. Each row is represented as a tuple, where each element corresponds to a column in the table
4. `display_button = ttk.Button(frame, text="Display Expenses", command=display_expenses):` This line creates a Tkinter button widget with the text "Display Expenses" and associates it with the display_expenses() function. So, when the button is clicked, the display_expenses() function will be called to retrieve and display the expenses from the database.
5. `display_button.grid(row=4, columnspan=2):` This line specifies the grid layout for the button within the Tkinter frame. It places the button in row 4 and spans it across two columns.

## Step6- Main Loop           
<p>Add the Tkinter main loop to start the application.</p>

```python
window.mainloop()
```

## Step7- Combine Everything

<p>Combine all the pieces into a single script, and make sure to close the database connection when the application is closed.</p>

```python
def on_closing():
conn.close()
window.destroy()window.protocol("WM_DELETE_WINDOW", on_closing)
```
## Explaination
1. `def on_closing()::` This line defines a function named on_closing(). This function is intended to handle the actions that should occur when the user attempts to close the application window.
2. `conn.close():` This line closes the connection to the SQLite database. It's essential to close the database connection properly when the application is closing to ensure that all database operations are completed, and resources are released.
3.` window.destroy():` This line destroys the Tkinter window, effectively closing the application. It ensures that the GUI window is closed properly when the user exits the application.
4. `window.protocol("WM_DELETE_WINDOW", on_closing):` This line associates the on_closing() function with the window's close event. It specifies that when the user attempts to close the window, the on_closing() function should be called to execute the actions specified within it (closing the database connection and destroying the window).
            
<h3>Start Application</h3>
<p>Launch the application from the terminal or using any code editor e.g. VS Code:</p>

```python
python expense-tracker.py
```
## Sample Output
<p>After running the application, a GUI window will open. You can enter your expenses and then view them by clicking the “Display Expenses” button. The expense data will be stored in the SQLite database.</p>
<img src="https://codeblockhub.com/wp-content/uploads/2023/10/Screenshot-2023-10-07-at-64408-PM.png"/>
