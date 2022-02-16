# 5. data abstractmethod
# Data Abstraction
# Data abstraction and encapsulation both are often used as synonyms.
# Both are nearly synonyms because data abstraction is achieved through encapsulation.

# Abstraction is used to hide internal details and show only functionalities. Abstracting something means
# to give names to things so that the name captures the core of what a function or a whole program does.

# Example 5: data abstractmethod in Python
# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def shapesides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def shapesides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def shapesides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def shapesides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def shapesides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.shapesides()

K = Quadrilateral()
K.shapesides()

R = Pentagon()
R.shapesides()

K = Hexagon()
K.shapesides()