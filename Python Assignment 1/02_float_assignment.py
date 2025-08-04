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
average_float= [3.14, 2.718, 1.618, 0.577]
print("average value for float data type: ", sum(average_float)/len(average_float))

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Your code here
Fahrenheit=98.6
celsius= (Fahrenheit - 32)*5/9
print("Convert 98.6 Fahrenheit to Celsius is:",celsius)

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Your code here
#Calculate the compound interest on $1000 at 5.5% for 3 years
Principal_amount=1000
rate_interest=5.5/100
compound_interest=1
tenure=3
Total_Amount=P*(1+r/n)**(n*t)
print("The compound interest is:",A-P);

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Your code here

# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Your code here

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Your code here
round_value=round(3.14159, 3)
print("rount of 3.14159 to 3 decimal places:",round_value)

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Your code here
a=45
b=67
c=(a*b)/100;
print("The percentage: 45 out of 67:",c)

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Your code here
number=23.456
sqrt=number**0.5
print("The square root of 23.456 is",sqrt);

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Your code here
P=2500
T=2.5
R=6.5
simple_interest=(P*T*R)/100;
print("Simple interest is",simple_interest)

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Your code here 
degrees=45.7
pi=3.14
radians=degrees*(pi/180)
print(radians);
print("The value of 45.7 degrees to radians is:", round(radians, 3));
