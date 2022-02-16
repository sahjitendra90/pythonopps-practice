class Employee:
    no_of_leave = 10

    def __init__(self, aname, ajob, asalary):
        self.name = aname
        self.job = ajob
        self.salary = asalary

    def printdetails(self):
        return f"The Name is {self.name}, salary is {self.salary} and role is {self.job}"


jitendra = Employee("Jitendra", "devloper", 10)
print(jitendra.salary)
print(jitendra.printdetails())
