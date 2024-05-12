import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
res = cursor.execute("SELECT name FROM sqlite_master WHERE name='expenses'")
if res.fetchone() is None:
  cursor.execute(
    '''CREATE TABLE expenses (id INTEGER PRIMARY KEY,
    category TEXT,  amount REAL,
    date TEXT)'''
    )
window = tk.Tk()
window.title("Expense Tracker")

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tk.Label(frame, text="Category").grid(row=0, column=0)
tk.Label(frame, text="Amount").grid(row=1, column=0)
tk.Label(frame, text="Date").grid(row=2, column=0)

category = tk.StringVar()
amount = tk.DoubleVar()
date = tk.StringVar()

category_entry = ttk.Entry(frame, textvariable=category)
amount_entry = ttk.Entry(frame, textvariable=amount)
date_entry = ttk.Entry(frame, textvariable=date)

category_entry.grid(row=0, column=1)
amount_entry.grid(row=1, column=1)
date_entry.grid(row=2, column=1)

def add_expense():
    cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
                   (category.get(), amount.get(), date.get()))
    conn.commit()

add_button = ttk.Button(frame, text="Add Expense", command=add_expense)
add_button.grid(row=3, columnspan=2)

def display_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    for expense in expenses:
        print(f"ID: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}, Date: {expense[3]}")

display_button = ttk.Button(frame, text="Display Expenses", command=display_expenses)
display_button.grid(row=4, columnspan=2)



def on_closing():
    conn.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
