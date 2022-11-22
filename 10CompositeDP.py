from abc import ABCMeta,abstractmethod

class IDepartement(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,employees):
        """
        Implement in child class
        """
    @staticmethod
    def print_department():
        """Implement in child class"""


class Accounting(IDepartement):
    def __init__(self, employees):
        super().__init__(employees)
        self.employees = employees
        

    def print_departement(self):
        print(f"Accounting department: {self.employees}")



class Development(IDepartement):
    def __init__(self, employees):
        super().__init__(employees)
        self.employees = employees
    

    def print_departement(self):
        print(f"Development department: {self.employees}")



class ParentDepartment(IDepartement):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []
    
    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees +=dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent department base employees: {self.base_employees}")

        for dept in self.sub_depts:
            dept.print_department()
        
        print(f"Total number of employees: {self.employees}")



dept1 = Accounting(200)
dept2 = Development(30)
parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()