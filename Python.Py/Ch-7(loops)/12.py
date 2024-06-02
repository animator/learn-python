# Write a program to print the multiplication table of n using for loop in reversed order.

num=int(input("Enter Your Numberm : "))

for i in range (10,0,-1):
    #print(str(num) + " X " + str(i) + "=" + str(i*num))
    
    print(f"{num} X {i} = {num*i}") # fstrings