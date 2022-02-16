# 1. Object

# An object (instance) is an instantiation of a class. When class is defined, only the description for
# the object is defined.
# Therefore, no memory or storage is allocated.

# The example for object of parrot class can be:

# obj = Parrot()

# Here, obj is an object of class Parrot.

# Suppose we have details of parrots. Now, we are going to show how to build the class and objects of parrots.

# Example 1: Creating Class and Object in Python
class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is also {} years old".format(woo.name, woo.age))

# In the above program, we created a class with the name Parrot. Then, we define attributes.
# The attributes are a characteristic of an object.

# These attributes are defined inside the __init__ method of the class.
# it is the initializer method that is first run as soon as the object is created.

# Then, we create instances of the Parrot class. Here, blu and woo are references (value) to our new objects.

# We can access the class attribute using __class__.species. Class attributes are the same for all instances
# of a class.
# Similarly, we access the instance attributes using blu.name and blu.age.
# However, instance attributes are different for every instance of a class.

# In the above program, we define two methods i.e sing() and dance().
# These are called instance methods because they are called on an instance object i.e blu.