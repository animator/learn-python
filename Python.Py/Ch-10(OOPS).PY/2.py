class Employee :
    company="Google"
    salary=880000000
    
Ashish=Employee()
seju=Employee()
print(Ashish.company)
Ashish.salary=900000000
print(seju.company)
seju.salary=890000000
Employee.company="Microsoft"
print(Ashish.company)
print(seju.company)
print(Ashish.salary)
print(seju.salary)