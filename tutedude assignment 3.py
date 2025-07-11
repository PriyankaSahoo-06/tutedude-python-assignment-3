#Task 1: Calculate Factorial Using a Function
def f(n):
 result=1
 for i in range(1,n+1):
  result*=i
 return result
a=int(input("enter a number:"))
print("Factorial of",a,"is",f(a))

#Task 2: Using the Math Module for Calculations
from math import *
a=int(input("Enter a number"))
print(sqrt(a))
print(log(a))

print(sin(a))