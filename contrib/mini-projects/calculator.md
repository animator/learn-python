//Simple Calculator in Python

from tkinter import *

exp = "" 

def press(num):  

	global exp

	exp = exp + str(num) 
 
	equation.set(exp) 
 
 def equal_press(): 
 
	try: 
 
		global exp 
  
		total = str(eval(exp)) 
  
		equation.set(total)
  
		exp = "" 
  
	except: 
 
        equation.set(" error ") 
		
		exp = "" 


def clear_press(): 

	global exp 
 
	exp = "" 
 
	equation.set("") 


# main code 
window = Tk() 

window.configure(background="white")  

window.title("Simple Calculator")  

window.geometry("320x320") 

equation = StringVar() 

expression_field = Entry(window, textvariable=equation, border=5) 

expression_field.grid(columnspan=4, ipadx=70)

# create a Buttons  
b1 = Button(window, text=' 1 ', fg='black', bg='beige',command=lambda: press(1), height=1, width=7) 

b1.grid(row=2, column=0) 

b2 = Button(window, text=' 2 ', fg='black', bg='beige',command=lambda: press(2), height=1, width=7) 

b2.grid(row=2, column=1) 

b3 = Button(window, text=' 3 ', fg='black', bg='beige',command=lambda: press(3), height=1, width=7) 

b3.grid(row=2, column=2) 

b4 = Button(window, text=' 4 ', fg='black', bg='beige', command=lambda: press(4), height=1, width=7) 

b4.grid(row=3, column=0) 

b5 = Button(window, text=' 5 ', fg='black', bg='beige', command=lambda: press(5), height=1, width=7) 

b5.grid(row=3, column=1) 

b6 = Button(window, text=' 6 ', fg='black', bg='beige', command=lambda: press(6), height=1, width=7) 

b6.grid(row=3, column=2) 

b7 = Button(window, text=' 7 ', fg='black', bg='beige', command=lambda: press(7), height=1, width=7) 

b7.grid(row=4, column=0) 

b8 = Button(window, text=' 8 ', fg='black', bg='beige',command=lambda: press(8), height=1, width=7) 

b8.grid(row=4, column=1) 

b9 = Button(window, text=' 9 ', fg='black', bg='beige',command=lambda: press(9), height=1, width=7) 

b9.grid(row=4, column=2) 
	
b10 = Button(window, text=' 0 ', fg='black', bg='beige', command=lambda: press(0), height=1, width=7) 

b10.grid(row=5, column=0) 

addition = Button(window, text=' + ', fg='black', bg='beige',command=lambda: press("+"), height=1, width=7) 

addition.grid(row=2, column=3) 

subtraction = Button(window, text=' - ', fg='black', bg='beige',command=lambda: press("-"), height=1, width=7) 

subtraction.grid(row=3, column=3) 

multiply = Button(window, text=' * ', fg='black', bg='beige',command=lambda: press("*"), height=1, width=7) 

multiply.grid(row=4, column=3) 

division = Button(window, text=' / ', fg='black', bg='beige',command=lambda: press("/"), height=1, width=7) 

division.grid(row=5, column=3) 

equals_to = Button(window, text=' = ', fg='black', bg='beige',command=equal_press, height=1, width=7) 

equals_to.grid(row=5, column=2) 

clear_b = Button(window, text='Clear', fg='black', bg='beige',command=clear_press, height=1, width=7) 

clear_b.grid(row=5, column=1) 

Decimal= Button(window, text='.', fg='black', bg='beige',command=lambda: press('.'), height=1, width=7) 

Decimal.grid(row=6, column=3) 

window.mainloop() 

![image](https://github.com/Sagarika-Dubey/learn-python/assets/141268973/4ebff207-14f9-4eff-aa08-b16340588a6e)
