# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
# Your code here
numbers = [3.14, 2.718, 1.618, 0.577]
length = len(numbers)
average = 0 

for i in numbers:
  average = average + i
print("the average of 3.14, 2.718, 1.618, 0.577 : ", average/length)

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Your code here

### formula c = (f - 32) _ 5/9 
f = 98.6 
c = ((f - 32) * 5/9)
print("98.6 Fahrenheit to Celsius : ", c)


# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Your code here
p = 1000
r = 5.5 
t = 3 
amount = p * (1 + r/100) ** t 
compound_interest = amount - p 

print("Principal : $", p)
print("Amount after 3 years: $", round(amount,2))
print("Compound Interest: $" round(compound_interest, 2))

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Your code here
a = 3.5 
b = 4.2 

hypotenuse = (a ** 2 + b ** 2) ** 0.5 

print("Side 1:", a)
print("Side 2:" ,b)
print("Hypotenuse:", round(hypotenuse,3))

# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Your code here
pi = 3.14159
r = 7.8

volume = (4/3) * pi * (r ** 3)

print("Radius: ", r)
print("Volume of Sphere:", round(volume, 2))

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Your code here
number = 3.14159
print("Original:", number)
print("Rounded to 3 decimals:", round(number, 3))

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Your code here
part = 45 
total = 67 

percentage = (part/total) * 100

print("Part:", part)
print("Total:", total)
print("Percentage:", round(percentage,2), "%")

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Your code here
number = 23.456
sqrt = number ** 0.5 

print("Number:", number)
print("Square Root:", round(sqrt,3))

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Your code here
p = 2500 
r = 6.5 
t = 2.5 

simple_interest = (p * r * t)/ 100

print("Principal: $", p)
print("Rate:", r , "%")
print("Time:", t , "years")
print("Simple Interest: $", round(simple_interest, 2))

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Your code here 

pi = 3.14159
degrees = 45.7

radians = degrees * (pi / 180)

print("Degrees:", degrees)
print("Radians:", round(radians, 4))
