# Write a program to print the multiplication table of a given number using for loop.

num=int(input("Enter Your Numberm : "))

for i in range (1,11):
    #print(str(num) + " X " + str(i) + "=" + str(i*num))
    
    print(f"{num} X {i} = {num*i}") # fstrings