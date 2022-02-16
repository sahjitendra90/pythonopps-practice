# 6. Polymorphism

# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle).
# However we could use the same method to color any shape. This concept is called Polymorphism.

# Example 6: Using Polymorphism in Python

class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can not swim")


class Penguin:

    def fly(self):
        print("Penguin can not fly")

    def swim(self):
        print("Penguin can swim")


# common interface

def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()
# passing the object
flying_test(blu)
flying_test(peggy)

# In the above program, we defined two classes Parrot and Penguin. Each of them have a common fly() method.
# However, their functions are different.

# To use polymorphism, we created a common interface
# i.e flying_test() function that takes any object and calls the object's fly() method.
# Thus, when we passed the blu and peggy objects in the flying_test() function, it ran effectively.

# Key Points to Remember:

# Object-Oriented Programming makes the program easy to understand as well as efficient.
# Since the class is sharable, the code can be reused.
# Data is safe and secure with data abstraction.
# Polymorphism allows the same interface for different objects, so programmers can write efficient code.