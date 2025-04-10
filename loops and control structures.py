# ---------------------------- FOR LOOP EXAMPLES ----------------------------

# 1. Print numbers from 1 to 5
for i in range(1, 6):  # Loops from 1 to 5
    print("For Loop 1:", i)

# 2. Print each letter in a string
for char in "Hello":
    print("For Loop 2:", char)

# 3. Sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("For Loop 3 Total:", total)

# 4. Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print("For Loop 4 Even:", i)

# 5. Print multiplication table of 3
for i in range(1, 11):
    print("For Loop 5 Table of 3:", 3, "x", i, "=", 3 * i)

# 6. Iterate over list with index
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print("For Loop 6:", i, fruits[i])

# 7. Print squares of numbers
for i in range(6):
    print("For Loop 7 Square of", i, "is", i ** 2)

# 8. Loop over dictionary
student = {"name": "Alice", "age": 20}
for key in student:
    print("For Loop 8:", key, "->", student[key])

# 9. Nested loop for pairs
for i in range(3):
    for j in range(2):
        print("For Loop 9 Pair:", i, j)

# 10. Loop over a set
colors = {"red", "blue", "green"}
for color in colors:
    print("For Loop 10 Color:", color)

# 11. Loop with break
for i in range(5):
    if i == 3:
        break
    print("For Loop 11:", i)

# 12. Loop with continue
for i in range(5):
    if i == 2:
        continue
    print("For Loop 12:", i)

# 13. Reverse a string
s = "hello"
for char in reversed(s):
    print("For Loop 13 Reverse:", char)

# 14. Loop through two lists
names = ["A", "B", "C"]
scores = [90, 80, 70]
for name, score in zip(names, scores):
    print("For Loop 14:", name, score)

# 15. Nested list
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for value in row:
        print("For Loop 15 Matrix Value:", value)

# 16. List comprehension
squares = [x**2 for x in range(5)]
print("For Loop 16 Squares:", squares)

# 17. Loop with else
for i in range(3):
    print("For Loop 17:", i)
else:
    print("For Loop 17: Done")

# 18. Filter vowels
for char in "education":
    if char in 'aeiou':
        print("For Loop 18 Vowel:", char)

# 19. ASCII values
for char in "AB":
    print("For Loop 19:", char, "->", ord(char))

# 20. Countdown
for i in range(5, 0, -1):
    print("For Loop 20 Countdown:", i)

# ---------------------------- WHILE LOOP EXAMPLES ----------------------------

# 1. Count from 1 to 5
i = 1
while i <= 5:
    print("While Loop 1:", i)
    i += 1

# 2. Print even numbers less than 10
i = 2
while i < 10:
    print("While Loop 2 Even:", i)
    i += 2

# 3. Sum until 100
sum = 0
i = 1
while sum < 100:
    sum += i
    i += 1
print("While Loop 3 Sum:", sum)

# 4. Countdown from 5
i = 5
while i > 0:
    print("While Loop 4 Countdown:", i)
    i -= 1

# 5. Infinite loop with break
i = 0
while True:
    print("While Loop 5:", i)
    if i == 2:
        break
    i += 1

# 6. Loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("While Loop 6:", i)

# 7. Print powers of 2 below 100
i = 1
while i < 100:
    print("While Loop 7 Power of 2:", i)
    i *= 2

# 8. Loop over list
lst = [1, 2, 3]
i = 0
while i < len(lst):
    print("While Loop 8 List Item:", lst[i])
    i += 1

# 9. Input validation
x = ""
while x != "yes":
    x = "yes"  # In real case, use input()
    print("While Loop 9 waiting for 'yes'")

# 10. Factorial using while
n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("While Loop 10 Factorial:", fact)

# 11. Loop through characters
s = "data"
i = 0
while i < len(s):
    print("While Loop 11 Char:", s[i])
    i += 1

# 12. Loop with else
i = 0
while i < 3:
    print("While Loop 12:", i)
    i += 1
else:
    print("While Loop 12: Done")

# 13. Print digits of number
n = 123
while n > 0:
    print("While Loop 13 Digit:", n % 10)
    n //= 10

# 14. Nested while loop
i = 0
while i < 2:
    j = 0
    while j < 2:
        print("While Loop 14 Pair:", i, j)
        j += 1
    i += 1

# 15. Print odd numbers
i = 1
while i < 10:
    print("While Loop 15 Odd:", i)
    i += 2

# 16. Check prime
n = 7
i = 2
is_prime = True
while i < n:
    if n % i == 0:
        is_prime = False
        break
    i += 1
print("While Loop 16 Prime:", is_prime)

# 17. Reverse number
num = 123
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("While Loop 17 Reverse:", rev)

# 18. Print Fibonacci up to 10
a, b = 0, 1
while b <= 10:
    print("While Loop 18 Fibonacci:", b)
    a, b = b, a + b

# 19. Loop to find first multiple of 7 > 50
n = 51
while n % 7 != 0:
    n += 1
print("While Loop 19 First Multiple of 7 > 50:", n)

# 20. Check palindrome
word = "madam"
i = 0
j = len(word) - 1
is_palindrome = True
while i < j:
    if word[i] != word[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
print("While Loop 20 Palindrome:", is_palindrome)

# ---------------------------- IF-ELSE EXAMPLES ----------------------------

# 1. Check even or odd
n = 4
if n % 2 == 0:
    print("If-Else 1: Even")
else:
    print("If-Else 1: Odd")

# 2. Positive, Negative or Zero
n = 0
if n > 0:
    print("If-Else 2: Positive")
elif n < 0:
    print("If-Else 2: Negative")
else:
    print("If-Else 2: Zero")

# 3. Check eligibility
age = 18
if age >= 18:
    print("If-Else 3: Eligible")
else:
    print("If-Else 3: Not Eligible")

# 4. Max of two
a, b = 5, 7
if a > b:
    print("If-Else 4: Max is", a)
else:
    print("If-Else 4: Max is", b)

# 5. Grading
score = 85
if score >= 90:
    print("If-Else 5: A")
elif score >= 80:
    print("If-Else 5: B")
else:
    print("If-Else 5: C")

# 6. Check divisor
a = 20
if a % 5 == 0:
    print("If-Else 6: Divisible by 5")

# 7. Username match
username = "admin"
if username == "admin":
    print("If-Else 7: Welcome admin")

# 8. Password check
password = "1234"
if password == "1234":
    print("If-Else 8: Access granted")
else:
    print("If-Else 8: Access denied")

# 9. Number in range
num = 8
if 1 <= num <= 10:
    print("If-Else 9: In range")

# 10. Leap year check
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("If-Else 10: Leap Year")
else:
    print("If-Else 10: Not Leap Year")

# 11. Check type
value = "123"
if isinstance(value, str):
    print("If-Else 11: It’s a string")

# 12. Check alphabet
char = 'a'
if char.isalpha():
    print("If-Else 12: Alphabet")

# 13. Check upper or lower
char = 'A'
if char.isupper():
    print("If-Else 13: Uppercase")
else:
    print("If-Else 13: Lowercase")

# 14. Vowel or consonant
ch = 'e'
if ch in 'aeiou':
    print("If-Else 14: Vowel")
else:
    print("If-Else 14: Consonant")

# 15. Login validation
uname = "user"
pwd = "pass"
if uname == "user" and pwd == "pass":
    print("If-Else 15: Login Successful")
else:
    print("If-Else 15: Login Failed")

# 16. Triangle type
a, b, c = 3, 3, 3
if a == b == c:
    print("If-Else 16: Equilateral")
elif a == b or b == c or a == c:
    print("If-Else 16: Isosceles")
else:
    print("If-Else 16: Scalene")

# 17. Age group
age = 30
if age < 13:
    print("If-Else 17: Child")
elif age < 20:
    print("If-Else 17: Teen")
else:
    print("If-Else 17: Adult")

# 18. Check last digit
n = 123
if n % 10 == 3:
    print("If-Else 18: Ends with 3")

# 19. Number length
n = 1234
if len(str(n)) == 4:
    print("If-Else 19: 4-digit number")

# 20. Compare strings
s1 = "hello"
s2 = "world"
if s1 < s2:
    print("If-Else 20: s1 comes before s2")





