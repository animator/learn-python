#Dictionary Syntax

my_Dict= {
    "Ashish": "Brilliant name",
        "Ashish Madhup": "Brilliant Human" ,
        "marks": [99,98,99] ,
        "another_Dict": {"ashish": "Ashish"},
        1:2
}

print(my_Dict['Ashish'])
print(my_Dict['Ashish Madhup'])
print(my_Dict["marks"])
print(my_Dict["another_Dict"])
print(my_Dict['another_Dict']['ashish'])

print(my_Dict.keys())
print(list(my_Dict.keys()))
print(my_Dict.values())
print(my_Dict.items())

print(my_Dict)
updateDict={
    "Seju":"Friend",
    "Ashish": "Brilliant Person"
}
my_Dict.update(updateDict)
print(my_Dict)

print(my_Dict.get("Ashish"))
print(my_Dict["Ashish"])