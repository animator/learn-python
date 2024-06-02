class Employee :
    company="Google"
    
    def ShowDetails(self):
        print("This is an Employee")
    
    @classmethod
    def Change_Company(cls,comp):
        cls.company=comp
    
class Programmer(Employee):
    language="Python"
    def getLanguage(self):
        print(f"The Language is {self.Language}")
        
    def ShowDetails(self):
        print("This is an programmer")
    
e=Employee()
e.ShowDetails()
p=Programmer()
p.ShowDetails()
print(p.company)
e.Change_Company("Microsoft")
print(e.Change_Compapny)