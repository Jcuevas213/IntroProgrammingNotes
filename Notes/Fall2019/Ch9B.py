# Chapter 9 - Functions
import math

# Functions are repeatable
# help us organize our code.

def say_hi(name):
    print("Hello", name)


say_hi("Mr. Lee")  # Call to the function
say_hi("Antoine")


# Area of a circle function
def area_circle(radius):
    area = math.pi * radius ** 2
    print("Area =", area)

area_circle(5)
area_circle(10)
print(area_circle(5))  # this prints None


# improved area circle function
def area_circle2(radius):
    area = math.pi * radius ** 2
    return area

print(area_circle2(5))  # this prints the answer
area = area_circle2(7)  # return and capture
print(area)

def volume_cylinder(radius, height):
    volume = area_circle2(radius) * height
    return volume

print("Volume of a six pack =", volume_cylinder(3, 15) * 6)


# Variable Scope
# The most confusing thing in this chapter


# Scope example 1
def f():
    x = 5  # this is a local variable


f()
# print(x)  # ERROR here you are trying to print a local variable in the global scope


# Scope example 2
y = 5  # global variable y

def f():
    print(y)  # global variables can be seen inside functions


f()


# Scope example 3
z = 10  # global

def f():
    # z += 1  # cannot change a global variable inside a function
    print(z)

f()

# Scope rules
# Local variables are born inside functions
# Global variables are born outside
# Local variables cannot be seen or used in the global scope
# Global variables CAN be seen, but CANNOT be changed in the local scope.



# The way to get a value from a function is by RETURN AND CAPTURE

x = 1  # global


def f(y):
    y += 1  # local
    return y


print(x)  # prints global x
x = f(x)  # return and capture, set global x to returned value
print(x)








