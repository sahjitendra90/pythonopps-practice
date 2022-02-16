class Employee:
    no_of_leave=10
    pass

jitendra=Employee()
ashish = Employee()

jitendra.name="Jitendra"
jitendra.job="developer"
jitendra.salary=0

ashish.name="Ashish"
ashish.job="mentor"
ashish.salary=2000000

print(jitendra.__dict__)
print(jitendra.no_of_leave)

Employee.no_of_leave=9

print(ashish.no_of_leave)
print(ashish.__dict__)
print(Employee.no_of_leave)