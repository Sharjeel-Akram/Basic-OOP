class Employee:
    def __init__(self,First_Name,Last_Name,Salary):
        self.First_Name = First_Name
        self.Last_Name =Last_Name
        self.Salary = Salary
        if self.Salary < 0:
            self.Set_Salary = 0
        else:
            self.Set_Salary = self.Salary
    
    def Get_Attributes(self):
        return (self.First_Name, self.Last_Name, self.Salary)

    def Set_First_Name(self,First_Name):
        self.First_Name = First_Name

    def Set_Last_name(self,Last_Name):
        self.Last_Name = Last_Name

    def Set_Salary(self,Salary):
        self.Salary = Salary

    def Get_First_Name(self):
            return self.First_Name

    def Get_Last_Name(self):
            return self.Last_Name
    def Get_Salary(self):
            return self.Salary
    def __add__(self,other):
         return self.Salary + other.Salary
    
    def __sub__(self,other):
        return self.Salary - other.Salary

    def __gt__(self,other):
        if(self.Salary > other.Salary): 
            return True
        else: 
            return False
    def __lt__(self,other):
        if(self.Salary < other.Salary): 
            return True
        else: 
            return False
    def __eq__(self,other):
        if(self.Salary == other.Salary): 
            return True
        else: 
            return False

Object1 = Employee("Sharjeel", "Akram", 100000)
Object2 = Employee("Adeel", "Akram", 80000)
print("Attributes of Obkect1: ", Object1.Get_Attributes()) 
print("Attributes of Obkect2: ",Object2.Get_Attributes())
print("Addition of salaries: ", Object1 + Object2)
print("Subtraction of salaries: ", Object1 - Object2)
print("greater salary: ", Object1 > Object2)
print("lesser salary :", Object1 < Object2)
print("equal salary: ", Object1 == Object2)