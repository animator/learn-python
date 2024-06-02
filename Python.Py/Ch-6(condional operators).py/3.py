# A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”.
# Write a program to detect these spams.

text=input("Enter Your Text")

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
else:
    spam=False
    
if(spam):
        print("THis text is spam")
else:
        print("This text is not spam")
        
    