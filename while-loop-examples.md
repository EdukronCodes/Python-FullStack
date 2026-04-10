# 30 While Loop Examples (Code by Code)

Same style as `for-loop-examples.md`: **each line of code** in its own block with an explanation, then the **full program**, **each iteration / phase**, and **output line by line** where printing happens.

Assumptions: **Python 3**.

---

## 1. Count up with a condition

**Code — line by line**

```python
i = 0
```

*Loop variable before the loop starts.*

```python
while i < 5:
```

*Repeat while `i` is 0,1,2,3,4; stop when `i == 5`.*

```python
    print(i)
```

*Show current value.*

```python
    i += 1
```

*Advance so the loop eventually ends.*

**Full program**

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

**Each iteration**

| Pass | `i` at test | prints | then `i` |
|------|-------------|--------|----------|
| 1 | 0 | 0 | 1 |
| 2 | 1 | 1 | 2 |
| 3 | 2 | 2 | 3 |
| 4 | 3 | 3 | 4 |
| 5 | 4 | 4 | 5 |

**Output — line by line**

```text
0
```
```text
1
```
```text
2
```
```text
3
```
```text
4
```
*Same as `for i in range(5): print(i)`.*

---

## 2. Count down

**Code — line by line**

```python
n = 3
```

```python
while n > 0:
```

```python
    print(n)
```

```python
    n -= 1
```

**Full program**

```python
n = 3
while n > 0:
    print(n)
    n -= 1
```

**Output — line by line**

```text
3
```
```text
2
```
```text
1
```
*Stops when `n` becomes 0.*

---

## 3. Sum numbers from a list (index `while`)

**Code — line by line**

```python
nums = [2, 5, 1]
```

```python
i = 0
```

```python
total = 0
```

```python
while i < len(nums):
```

*Stay in loop until every index visited.*

```python
    total += nums[i]
```

```python
    i += 1
```

```python
print(total)
```

**Full program**

```python
nums = [2, 5, 1]
i = 0
total = 0
while i < len(nums):
    total += nums[i]
    i += 1
print(total)
```

**Output — line by line**

```text
8
```
*2+5+1; one print after the loop.*

---

## 4. Stop at a sentinel value

**Code — line by line**

```python
data = [1, 4, -1, 9]
```

*`-1` means “stop processing”.*

```python
i = 0
```

```python
while i < len(data) and data[i] != -1:
```

*End early if sentinel seen.*

```python
    print(data[i])
```

```python
    i += 1
```

**Full program**

```python
data = [1, 4, -1, 9]
i = 0
while i < len(data) and data[i] != -1:
    print(data[i])
    i += 1
```

**Output — line by line**

```text
1
```
```text
4
```
*9 never prints — loop stops at `-1`.*

---

## 5. `break` when target found

**Code — line by line**

```python
items = [3, 8, 2, 5]
```

```python
i = 0
```

```python
target = 2
```

```python
while i < len(items):
```

```python
    if items[i] == target:
```

```python
        print("found at", i)
```

```python
        break
```

*Exit immediately; no further iterations.*

```python
    i += 1
```

**Full program**

```python
items = [3, 8, 2, 5]
i = 0
target = 2
while i < len(items):
    if items[i] == target:
        print("found at", i)
        break
    i += 1
```

**Output — line by line**

```text
found at 2
```
*Index of first `2`; elements after it are not scanned.*

---

## 6. `continue` — skip even numbers

**Code — line by line**

```python
n = 0
```

```python
while n < 6:
```

```python
    n += 1
```

*Bump first so we eventually progress.*

```python
    if n % 2 == 0:
```

```python
        continue
```

*Skip the `print` for this pass.*

```python
    print(n)
```

**Full program**

```python
n = 0
while n < 6:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
```

**Output — line by line**

```text
1
```
```text
3
```
```text
5
```
*Even values 2,4,6 never reach `print`.*

---

## 7. `while` … `else` (no `break`)

**Code — line by line**

```python
n = 2
```

```python
while n > 0:
```

```python
    print(n)
```

```python
    n -= 1
```

```python
else:
```

*Runs when the condition becomes false **if** the loop did not `break`.*

```python
    print("finished normally")
```

**Full program**

```python
n = 2
while n > 0:
    print(n)
    n -= 1
else:
    print("finished normally")
```

**Output — line by line**

```text
2
```
```text
1
```
```text
finished normally
```
*`else` attached to `while` is not the same as `if/else`.*

---

## 8. `while` … `else` skipped by `break`

**Code — line by line**

```python
n = 5
```

```python
while n > 0:
```

```python
    print(n)
```

```python
    if n == 3:
```

```python
        break
```

```python
    n -= 1
```

```python
else:
```

```python
    print("done")
```

**Full program**

```python
n = 5
while n > 0:
    print(n)
    if n == 3:
        break
    n -= 1
else:
    print("done")
```

**Output — line by line**

```text
5
```
```text
4
```
```text
3
```
*`break` skips `else`; no `"done"`.*

---

## 9. Menu-style `while True` + `break`

**Code — line by line**

```python
choice = "y"
```

*Simulated user input sequence.*

```python
rounds = 0
```

```python
while True:
```

*Runs until `break`.*

```python
    rounds += 1
```

```python
    print("round", rounds)
```

```python
    if rounds >= 2:
```

```python
        break
```

**Full program**

```python
rounds = 0
while True:
    rounds += 1
    print("round", rounds)
    if rounds >= 2:
        break
```

**Output — line by line**

```text
round 1
```
```text
round 2
```
*Common pattern: infinite loop with explicit exit.*

---

## 10. Count digits in a positive integer

**Code — line by line**

```python
n = 408
```

```python
count = 0
```

```python
while n > 0:
```

```python
    n //= 10
```

*Drop last digit (integer division by 10).*

```python
    count += 1
```

```python
print(count)
```

**Full program**

```python
n = 408
count = 0
while n > 0:
    n //= 10
    count += 1
print(count)
```

**Output — line by line**

```text
3
```
*408 → 40 → 4 → 0: three steps.*

---

## 11. Reverse digits of a number

**Code — line by line**

```python
n = 123
```

```python
rev = 0
```

```python
while n > 0:
```

```python
    rev = rev * 10 + n % 10
```

*Shift `rev` left and append last digit of `n`.*

```python
    n //= 10
```

```python
print(rev)
```

**Full program**

```python
n = 123
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
```

**Output — line by line**

```text
321
```

---

## 12. Factorial with `while`

**Code — line by line**

```python
n = 4
```

```python
result = 1
```

```python
while n > 1:
```

```python
    result *= n
```

```python
    n -= 1
```

```python
print(result)
```

**Full program**

```python
n = 4
result = 1
while n > 1:
    result *= n
    n -= 1
print(result)
```

**Output — line by line**

```text
24
```
*4×3×2.*

---

## 13. Fibonacci until value exceeds a limit

**Code — line by line**

```python
limit = 20
```

```python
a, b = 0, 1
```

```python
while a <= limit:
```

```python
    print(a)
```

```python
    a, b = b, a + b
```

*Classic Fibonacci step.*

**Full program**

```python
limit = 20
a, b = 0, 1
while a <= limit:
    print(a)
    a, b = b, a + b
```

**Output — line by line**

```text
0
```
```text
1
```
```text
1
```
```text
2
```
```text
3
```
```text
5
```
```text
8
```
```text
13
```
*Next would be 21 > 20, so loop stops before printing it.*

---

## 14. GCD (Euclidean algorithm)

**Code — line by line**

```python
a, b = 48, 18
```

```python
while b != 0:
```

```python
    a, b = b, a % b
```

*Replace `(a,b)` with `(b, remainder)` until remainder is 0.*

```python
print(a)
```

**Full program**

```python
a, b = 48, 18
while b != 0:
    a, b = b, a % b
print(a)
```

**Output — line by line**

```text
6
```
*Greatest common divisor of 48 and 18.*

---

## 15. Integer power `base ** exp` using multiplication

**Code — line by line**

```python
base, exp = 3, 4
```

```python
result = 1
```

```python
while exp > 0:
```

```python
    result *= base
```

```python
    exp -= 1
```

```python
print(result)
```

**Full program**

```python
base, exp = 3, 4
result = 1
while exp > 0:
    result *= base
    exp -= 1
print(result)
```

**Output — line by line**

```text
81
```
*3×3×3×3.*

---

## 16. Collatz — print sequence until 1

**Code — line by line**

```python
n = 6
```

```python
while n != 1:
```

```python
    print(n)
```

```python
    if n % 2 == 0:
```

```python
        n //= 2
```

```python
    else:
```

```python
        n = 3 * n + 1
```

```python
print(n)
```

*Final 1.*

**Full program**

```python
n = 6
while n != 1:
    print(n)
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(n)
```

**Output — line by line**

```text
6
```
```text
3
```
```text
10
```
```text
5
```
```text
16
```
```text
8
```
```text
4
```
```text
2
```
```text
1
```

---

## 17. Sum of digits

**Code — line by line**

```python
n = 502
```

```python
s = 0
```

```python
while n > 0:
```

```python
    s += n % 10
```

*Add last digit.*

```python
    n //= 10
```

```python
print(s)
```

**Full program**

```python
n = 502
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)
```

**Output — line by line**

```text
7
```
*5+0+2.*

---

## 18. Check prime (trial division with `while`)

**Code — line by line**

```python
n = 17
```

```python
d = 2
```

```python
is_prime = n >= 2
```

```python
while d * d <= n and is_prime:
```

*Try divisors up to √n.*

```python
    if n % d == 0:
```

```python
        is_prime = False
```

```python
    d += 1
```

```python
print(is_prime)
```

**Full program**

```python
n = 17
d = 2
is_prime = n >= 2
while d * d <= n and is_prime:
    if n % d == 0:
        is_prime = False
    d += 1
print(is_prime)
```

**Output — line by line**

```text
True
```

---

## 19. Count how many times you can halve an even number

**Code — line by line**

```python
n = 40
```

```python
steps = 0
```

```python
while n % 2 == 0 and n > 0:
```

```python
    n //= 2
```

```python
    steps += 1
```

```python
print(steps, n)
```

**Full program**

```python
n = 40
steps = 0
while n % 2 == 0 and n > 0:
    n //= 2
    steps += 1
print(steps, n)
```

**Output — line by line**

```text
3 5
```
*40→20→10→5; three factors of 2.*

---

## 20. Double until exceeding a threshold

**Code — line by line**

```python
x = 1
```

```python
while x <= 30:
```

```python
    print(x)
```

```python
    x *= 2
```

**Full program**

```python
x = 1
while x <= 30:
    print(x)
    x *= 2
```

**Output — line by line**

```text
1
```
```text
2
```
```text
4
```
```text
8
```
```text
16
```
*Next would be 32 > 30 — condition fails before that print.*

---

## 21. Linear search with `while` (not found case)

**Code — line by line**

```python
items = [1, 3, 5]
```

```python
target = 4
```

```python
i = 0
```

```python
while i < len(items) and items[i] != target:
```

```python
    i += 1
```

```python
if i < len(items):
```

```python
    print("at", i)
```

```python
else:
```

```python
    print("missing")
```

**Full program**

```python
items = [1, 3, 5]
target = 4
i = 0
while i < len(items) and items[i] != target:
    i += 1
if i < len(items):
    print("at", i)
else:
    print("missing")
```

**Output — line by line**

```text
missing
```
*Loop exits when `i == len(items)`.*

---

## 22. String traversal by index

**Code — line by line**

```python
s = "go"
```

```python
i = 0
```

```python
out = ""
```

```python
while i < len(s):
```

```python
    out = s[i] + out
```

*Prepend each character → reverse.*

```python
    i += 1
```

```python
print(out)
```

**Full program**

```python
s = "go"
i = 0
out = ""
while i < len(s):
    out = s[i] + out
    i += 1
print(out)
```

**Output — line by line**

```text
og
```

---

## 23. Strip trailing spaces (concept)

**Code — line by line**

```python
text = "hi   "
```

```python
while text.endswith(" "):
```

```python
    text = text[:-1]
```

*Remove one space from the end each time.*

```python
print(repr(text))
```

**Full program**

```python
text = "hi   "
while text.endswith(" "):
    text = text[:-1]
print(repr(text))
```

**Output — line by line**

```text
'hi'
```
*`repr` shows quotes; content is `hi` with no trailing spaces.*

---

## 24. First index where predicate holds

**Code — line by line**

```python
nums = [3, -1, 4]
```

```python
i = 0
```

```python
while i < len(nums) and nums[i] >= 0:
```

```python
    i += 1
```

```python
if i < len(nums):
```

```python
    print("first negative at", i)
```

*If the loop stopped because a negative was found, `i` points at it.*

```python
else:
```

```python
    print("none")
```

*All elements were ≥ 0.*

**Full program**

```python
nums = [3, -1, 4]
i = 0
while i < len(nums) and nums[i] >= 0:
    i += 1
if i < len(nums):
    print("first negative at", i)
else:
    print("none")
```

**Output — line by line**

```text
first negative at 1
```

---

## 25. Reduce number by subtracting until in range

**Code — line by line**

```python
x = 23
```

```python
while x > 10:
```

```python
    x -= 5
```

```python
print(x)
```

**Full program**

```python
x = 23
while x > 10:
    x -= 5
print(x)
```

**Output — line by line**

```text
8
```
*23→18→13→8; 8 ≤ 10 stops the loop.*

---

## 26. Accumulate product until product > 50

**Code — line by line**

```python
k = 1
```

```python
p = 1
```

```python
while p <= 50:
```

```python
    p *= k
```

```python
    k += 1
```

```python
print(p)
```

**Full program**

```python
k = 1
p = 1
while p <= 50:
    p *= k
    k += 1
print(p)
```

**Output — line by line**

```text
120
```
*Loop multiplies `p` by `1,2,3,…` until `p` exceeds 50; the printed value is that first product above 50 (here 120).*

---

## 27. Two-pointer merge (print pairs until one list ends)

**Code — line by line**

```python
a = [1, 4]
```

```python
b = [2, 3, 9]
```

```python
i, j = 0, 0
```

```python
while i < len(a) and j < len(b):
```

```python
    if a[i] <= b[j]:
```

```python
        print(a[i])
```

```python
        i += 1
```

```python
    else:
```

```python
        print(b[j])
```

```python
        j += 1
```

**Full program**

```python
a = [1, 4]
b = [2, 3, 9]
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        print(a[i])
        i += 1
    else:
        print(b[j])
        j += 1
```

**Output — line by line**

```text
1
```
*Pick from `a`.*

```text
2
```
```text
3
```
*Pick from `b` twice.*

```text
4
```
*Then `i` exhausts `a`; loop stops — 9 not printed.*

---

## 28. Palindrome check (characters)

**Code — line by line**

```python
s = "racecar"
```

```python
left, right = 0, len(s) - 1
```

```python
ok = True
```

```python
while left < right:
```

```python
    if s[left] != s[right]:
```

```python
        ok = False
```

```python
        break
```

```python
    left += 1
```

```python
    right -= 1
```

```python
print(ok)
```

**Full program**

```python
s = "racecar"
left, right = 0, len(s) - 1
ok = True
while left < right:
    if s[left] != s[right]:
        ok = False
        break
    left += 1
    right -= 1
print(ok)
```

**Output — line by line**

```text
True
```

---

## 29. Integer logarithm base 2 (floor)

**Code — line by line**

```python
n = 31
```

```python
count = -1
```

```python
t = n
```

```python
while t > 0:
```

```python
    t //= 2
```

```python
    count += 1
```

```python
print(count)
```

**Full program**

```python
n = 31
count = -1
t = n
while t > 0:
    t //= 2
    count += 1
print(count)
```

**Output — line by line**

```text
4
```
*Each loop halves `t` and increments `count`; when `t` becomes 0, `count` is ⌊log₂ 31⌋, which is 4.*

---

## 30. Retry counter (max attempts)

**Code — line by line**

```python
attempt = 0
```

```python
max_try = 3
```

```python
secret_ok = False
```

```python
while attempt < max_try and not secret_ok:
```

```python
    attempt += 1
```

```python
    print("try", attempt)
```

```python
    if attempt == 2:
```

*Simulate success on second try.*

```python
        secret_ok = True
```

```python
print("ok" if secret_ok else "fail")
```

**Full program**

```python
attempt = 0
max_try = 3
secret_ok = False
while attempt < max_try and not secret_ok:
    attempt += 1
    print("try", attempt)
    if attempt == 2:
        secret_ok = True
print("ok" if secret_ok else "fail")
```

**Output — line by line**

```text
try 1
```
```text
try 2
```
```text
ok
```
*Loop stops after success even though `max_try` not reached.*

---

## Quick reference

| Idea | `while` condition often looks like |
|------|-------------------------------------|
| Scan sequence | `i < len(data)` |
| Sentinel | `... and data[i] != sentinel` |
| Reduce a number | `n > 0` with `n //= 10` or similar |
| Until goal | `not done` or `x < limit` |
| Infinite menu | `while True` + `break` |
| Two pointers | `left < right` or two indices in bounds |

**`for` vs `while`:** use **`for`** when you already have a sequence or a clear `range`; use **`while`** when the number of steps depends on runtime data or a condition that is not a simple counter.

File: `while-loop-examples.md` — Python 3.
