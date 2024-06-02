letter= '''Dear <|Name|> ,
Your are selected !

Date: <|Date|>

Greet from Hackeraashu Team'''

name = input("Entre Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)