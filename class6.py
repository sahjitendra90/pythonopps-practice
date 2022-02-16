class Employee:
    no_of_leave = 10

    def __init__(self, aname, ajob, asalary):
        self.name = aname
        self.job = ajob
        self.salary = asalary

    def printdetails(self):
        return f"The Name is {self.name} salary is {self.salary} and role is {self.job}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leave = newleaves

    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


jitendra = Employee("Jitendra", "devloper", 10)
karan = Employee.from_str("Karan-chor-420")
print(karan.salary)
jitendra.change_leaves(32)
print(jitendra.no_of_leave)