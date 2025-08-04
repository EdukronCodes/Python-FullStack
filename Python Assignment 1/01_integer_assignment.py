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
n=10
natural_numbers=list(range(1,n+1))
print(natural_numbers)

# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
# Your code here
a=156
b=7
remainder=(a%b)
print(float(remainder))

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
# Your code here

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
# Your code here
a=25
b=2
square=(a**b)
print(square)

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
# Your code here
number=12345
count=0
for i in str(number):
    count=int(i)+count
print(count)

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
# Your code here
n=97
if n%2==0:
    print("The number is not Prime: ",n)
else:
    print("The number is Prime: ",n)
  
# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
# Your code here
n=8
count=1
for i in range(1, n+1):
      count *=i
print(count)
print("Factorial of", n, "is:",count)

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
# Your code here
average=[15, 23, 31, 42, 56]
avg=sum(average)/len(average)
print("average:", avg);

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
# Your code here

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")

# Your code here 
count=0
add_numbers=[]
for i in range(1,40, 2):
    count+=1
    add_numbers.append(i)
    
print("sum of first 20 odd numbers:", sum(add_numbers))
