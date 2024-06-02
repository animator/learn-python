# Write a program to find whether a given number is prime or not.

num=int(input("Enter Your Number"))

prime=True
for i in range(2,num):
    if(num%i==0):
     prime =False
    break

if (prime):
    print("Number is Prime")
else:
    print("Number is not prime")