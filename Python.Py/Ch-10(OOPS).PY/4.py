class Employee:
    company="Goggle"
    def getSalary(self):
        print(f"Salary is {self.Salary}")
        
    @staticmethod
    def greet():#This doesn't required self
        print("Good Morning Sir")
        
Ashish=Employee
Ashish.greet()
Ashish.Salary=90000000
Ashish.getSalary()