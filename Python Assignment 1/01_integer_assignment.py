# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
# Your code here
a = 1 
for i in range(1,11):
  a = a * i 
print("Product of first 10 natural numbers : ",a)
  
# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
# Your code here
a = 156 
b = 7 
print("Remainder when 156 by 7 : ",a%b)

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
# Your code here
a = 25
b = a ** 2
print("Square of 25 : ", b)

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
# Your code here
import math
a = 125
b = a ** (1/3)
b = round(b)

print("Cube root of 125 : ",b)

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
# Your code here
numbers = 12345

sum_numbers = 0 
for i in str(numbers):
  sum_numbers = sum_numbers + int(i)
print("Sum of digits in number 12345 : ", sum_numbers)



# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
# Your code here
a = 97
is_prime = True

if a < 2:
  is_prime = False
else:
  for i in range(2,a):
    if (a%i == 0):
      is_prime = False
      break
if is_prime:
  print(a,"is Prime Number")
else:
  print(a,"is Not Prime Number")

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
# Your code here
a = 8

factorial = 1
for i in range(1,a+1):
  factorial = factorial * i 
print("Factorial of n is : ", factorial)
  
  

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
# Your code here
numbers = 15,23,31,42,56

length_numbers = len(numbers)

sum_numbers = 0 
for i in numbers:
  sum_numbers = sum_numbers + int(i)
 print("the average of numbers: ", sum_numbers / length_numbers)

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
# Your code here
a = 48
b = 36

divisiors_a = []
divisiors_b = []

for i in range(1,a+1):
  if(a%i == 0):
    divisiors_a.append(i)

for j in range(1,b+1):
  if(b%j == 0):
    divisiors_b.append(j)

common = []
for x in divisiors_a:
  if x in divisiors_b:
    common.append(x)
gcd = max(common)

print(gcd)

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
# Your code here 

a = 0 
for i in range(1,40):
  if(i%2 != 0):
    a = a + i 
print(a)
