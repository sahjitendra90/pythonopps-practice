class Employee:
    no_of_leave = 10
    pass

    def printdetails(self):
        return f" The Name is {self.name}, salary is {self.salary} and role is {self.job}"


jitendra = Employee()
ashish = Employee()

jitendra.name = "Jitendra"
jitendra.job = "developer"
jitendra.salary = 0

ashish.name = "Ashish"
ashish.job = "mentor"
ashish.salary = 2000000

print(ashish.printdetails())
print(jitendra.printdetails())
