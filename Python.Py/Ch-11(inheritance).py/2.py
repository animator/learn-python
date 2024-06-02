class Employee:
    company="Google"
    salary=5600
    salarybonus=500
    #totalSalary=6100
    
    @property #use of property(setter method)
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    @totalSalary.setter# setter method
    def totalSalary(self,val):
        self.salarybonus = val - self.salary
    
e = Employee()
print(e.totalSalary)
e.tatalSalary = 9999
print(e.salary)
print(e.salarybonus)