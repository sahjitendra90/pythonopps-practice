# 4. Encapsulation

# Using OOP in Python, we can restrict access to methods and variables. T
# his prevents data from direct modification which is called encapsulation.
# In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.

# Example 4: Data Encapsulation in Python

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price

c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# In the above program, we defined a Computer class.

# We used __init__() method to store the maximum selling price of Computer. Here, notice the code

# c.__maxprice = 1000
# Here, we have tried to modify the value of __maxprice outside of the class.
# However, since __maxprice is a private variable, this modification is not seen on the output.

# As shown, to change the value, we have to use a setter function i.e setMaxPrice()
# which takes price as a parameter.