# 30 For Loop Examples (Code by Code)

This file builds each example **one line of code at a time**: each snippet is in its own block, followed by what that line does. Then you see the **full program**, **each iteration**, and **each output line** explained.

---

## 1. Simple range — print 0 to 4

**Code — line by line**

```python
for i in range(5):
```

*Starts a loop. `range(5)` produces 0, 1, 2, 3, 4 (stop before 5). Each time, `i` is the next value.*

```python
    print(i)
```

*Indented under `for`: runs every iteration and prints the current `i`.*

**Full program**

```python
for i in range(5):
    print(i)
```

**Each iteration**

| Run | `i` | What happens |
|-----|-----|----------------|
| 1 | 0 | `print(0)` |
| 2 | 1 | `print(1)` |
| 3 | 2 | `print(2)` |
| 4 | 3 | `print(3)` |
| 5 | 4 | `print(4)` |

**Output — line by line**

```text
0
```
*First value from `range(5)`.*

```text
1
```
*Second iteration.*

```text
2
```
*Third.*

```text
3
```
*Fourth.*

```text
4
```
*Fifth; 5 is never reached because `range` stops before the end number.*

---

## 2. Range with start and stop

**Code — line by line**

```python
for n in range(3, 8):
```

*`range(3, 8)` = start at 3, stop before 8 → 3,4,5,6,7.*

```python
    print(n)
```

*Prints the current `n` each time.*

**Full program**

```python
for n in range(3, 8):
    print(n)
```

**Each iteration** — `n` is 3, then 4, 5, 6, 7 (five prints).

**Output — line by line**

```text
3
```
*Start is inclusive.*

```text
4
```
```text
5
```
```text
6
```
```text
7
```
*8 is exclusive, so it never prints.*

---

## 3. Range with step

**Code — line by line**

```python
for x in range(0, 10, 2):
```

*Start 0, stop before 10, add 2 each time → 0,2,4,6,8.*

```python
    print(x)
```

*Prints each even step value.*

**Full program**

```python
for x in range(0, 10, 2):
    print(x)
```

**Output — line by line**

```text
0
```
*0 + 2×0.*

```text
2
```
*0 + 2×1.*

```text
4
```
```text
6
```
```text
8
```
*Next would be 10, which hits the stop; loop ends.*

---

## 4. Iterate a string (characters)

**Code — line by line**

```python
for ch in "Hi":
```

*String is a sequence: first `ch` is `'H'`, then `'i'`.*

```python
    print(ch)
```

*One character printed per iteration.*

**Full program**

```python
for ch in "Hi":
    print(ch)
```

**Output — line by line**

```text
H
```
*First character.*

```text
i
```
*Second character.*

---

## 5. Iterate a list

**Code — line by line**

```python
for item in [10, 20, 30]:
```

*Each iteration sets `item` to the next list element.*

```python
    print(item)
```

*Prints that element.*

**Full program**

```python
for item in [10, 20, 30]:
    print(item)
```

**Output — line by line**

```text
10
```
*First element.*

```text
20
```
```text
30
```
*Second and third.*

---

## 6. Accumulator — sum

**Code — line by line**

```python
total = 0
```

*Running sum starts at zero.*

```python
for v in [1, 2, 3, 4]:
```

*Each `v` is the next number to add.*

```python
    total = total + v
```

*Adds current `v` into `total`.*

```python
print(total)
```

*Runs once after the loop; shows final sum.*

**Full program**

```python
total = 0
for v in [1, 2, 3, 4]:
    total = total + v
print(total)
```

**Each iteration** — after v=1 → total 1; v=2 → 3; v=3 → 6; v=4 → 10.

**Output — line by line**

```text
10
```
*Single line: 1+2+3+4; only `print(total)` runs after all additions.*

---

## 7. Count matches

**Code — line by line**

```python
words = ["a", "bb", "ccc", "dd"]
```

*Data to scan.*

```python
count = 0
```

*Counter starts at 0.*

```python
for w in words:
```

*Each `w` is one string.*

```python
    if len(w) == 2:
```

*True only for two-character strings.*

```python
        count += 1
```

*Increase count when length is 2.*

```python
print(count)
```

*Print how many matched.*

**Full program**

```python
words = ["a", "bb", "ccc", "dd"]
count = 0
for w in words:
    if len(w) == 2:
        count += 1
print(count)
```

**Output — line by line**

```text
2
```
*`"bb"` and `"dd"` each add 1; `"a"` and `"ccc"` do not.*

---

## 8. Build a new list

**Code — line by line**

```python
squares = []
```

*Empty list to fill.*

```python
for k in range(1, 4):
```

*`k` is 1, 2, 3.*

```python
    squares.append(k * k)
```

*Append square of current `k`.*

```python
print(squares)
```

*Show the built list once.*

**Full program**

```python
squares = []
for k in range(1, 4):
    squares.append(k * k)
print(squares)
```

**Output — line by line**

```text
[1, 4, 9]
```
*One print: squares of 1, 2, 3 collected in order.*

---

## 9. `enumerate` — index and value

**Code — line by line**

```python
for i, letter in enumerate(["x", "y"]):
```

*Yields (0,'x'), then (1,'y').*

```python
    print(i, letter)
```

*Prints index and character together.*

**Full program**

```python
for i, letter in enumerate(["x", "y"]):
    print(i, letter)
```

**Output — line by line**

```text
0 x
```
*Index 0, first item.*

```text
1 y
```
*Index 1, second item.*

---

## 10. `zip` two lists

**Code — line by line**

```python
for a, b in zip([1, 2], [10, 20]):
```

*Pairs: (1,10), (2,20).*

```python
    print(a + b)
```

*Prints sum of the pair.*

**Full program**

```python
for a, b in zip([1, 2], [10, 20]):
    print(a + b)
```

**Output — line by line**

```text
11
```
*1 + 10.*

```text
22
```
*2 + 20.*

---

## 11. Nested loop — combinations

**Code — line by line**

```python
for i in range(2):
```

*Outer: `i` is 0, then 1.*

```python
    for j in range(2):
```

*Inner: for each `i`, `j` is 0 then 1.*

```python
        print(i, j)
```

*Runs 2×2 times.*

**Full program**

```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

**Output — line by line**

```text
0 0
```
*i=0, j=0.*

```text
0 1
```
*i=0, j=1.*

```text
1 0
```
*i=1, j=0.*

```text
1 1
```
*i=1, j=1.*

---

## 12. `break` — exit early

**Code — line by line**

```python
for n in range(10):
```

*Would go 0…9, but `break` may stop earlier.*

```python
    if n == 3:
```

*When `n` reaches 3…*

```python
        break
```

*…exit the whole `for` immediately.*

```python
    print(n)
```

*Skipped for `n == 3` and never reached for higher `n` after break.*

**Full program**

```python
for n in range(10):
    if n == 3:
        break
    print(n)
```

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
*When `n` is 3, `break` runs; no print for 3 or above.*

---

## 13. `continue` — skip rest of iteration

**Code — line by line**

```python
for n in range(4):
```

*`n`: 0,1,2,3.*

```python
    if n == 2:
```

*On the iteration where `n` is 2…*

```python
        continue
```

*…skip the rest of this iteration; go to next `n`.*

```python
    print(n)
```

*Not run when `continue` fires.*

**Full program**

```python
for n in range(4):
    if n == 2:
        continue
    print(n)
```

**Output — line by line**

```text
0
```
```text
1
```
```text
3
```
*No line for 2 — that iteration jumped to the next with `continue`.*

---

## 14. `for` with `else` (no `break`)

**Code — line by line**

```python
for x in [1, 2]:
```

*Normal loop over two values.*

```python
    print(x)
```

*Print each.*

```python
else:
```

*Runs after loop **only if** the loop did not `break`.*

```python
    print("done")
```

*Executes here because completion was normal.*

**Full program**

```python
for x in [1, 2]:
    print(x)
else:
    print("done")
```

**Output — line by line**

```text
1
```
```text
2
```
```text
done
```
*`else` runs after finishing all items without `break`.*

---

## 15. `for` with `else` and `break`

**Code — line by line**

```python
for x in [1, 2, 3]:
```

*Starts with x=1.*

```python
    if x == 2:
```

*True on second iteration.*

```python
        break
```

*Leaves loop; `else` is skipped.*

```python
    print(x)
```

*Only runs for x=1 before break.*

```python
else:
    print("done")
```

*Never reached — loop exited by `break`.*

**Full program**

```python
for x in [1, 2, 3]:
    if x == 2:
        break
    print(x)
else:
    print("done")
```

**Output — line by line**

```text
1
```
*Only output: break happens before printing 2.*

---

## 16. Reverse `range`

**Code — line by line**

```python
for i in range(3, 0, -1):
```

*Start 3, go down by 1, stop before 0 → 3,2,1.*

```python
    print(i)
```

*Print each value.*

**Full program**

```python
for i in range(3, 0, -1):
    print(i)
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
*Countdown; 0 is not included (exclusive stop for negative step).*

---

## 17. Tuple unpacking in loop

**Code — line by line**

```python
pairs = [(1, "a"), (2, "b")]
```

*List of two tuples.*

```python
for num, label in pairs:
```

*Each tuple unpacks into `num` and `label`.*

```python
    print(num, label)
```

*Print both.*

**Full program**

```python
pairs = [(1, "a"), (2, "b")]
for num, label in pairs:
    print(num, label)
```

**Output — line by line**

```text
1 a
```
*From first tuple.*

```text
2 b
```
*From second tuple.*

---

## 18. Dictionary — keys only

**Code — line by line**

```python
d = {"x": 1, "y": 2}
```

*A small dict.*

```python
for key in d:
```

*Iterating a dict yields keys (insertion order in 3.7+).*

```python
    print(key)
```

*Print each key.*

**Full program**

```python
d = {"x": 1, "y": 2}
for key in d:
    print(key)
```

**Output — line by line**

```text
x
```
*First key.*

```text
y
```
*Second key.*

---

## 19. Dictionary — `.items()`

**Code — line by line**

```python
d = {"x": 1, "y": 2}
```

*Same dict.*

```python
for k, v in d.items():
```

*Each step: one (key, value) pair.*

```python
    print(k, v)
```

*Print key and value.*

**Full program**

```python
d = {"x": 1, "y": 2}
for k, v in d.items():
    print(k, v)
```

**Output — line by line**

```text
x 1
```
```text
y 2
```
*One line per entry.*

---

## 20. String concatenation in a loop

**Code — line by line**

```python
s = ""
```

*Empty string to grow.*

```python
for part in ["A", "B", "C"]:
```

*Each `part` is one piece.*

```python
    s = s + part
```

*Append `part` to the right of current `s`.*

```python
print(s)
```

*Final combined string.*

**Full program**

```python
s = ""
for part in ["A", "B", "C"]:
    s = s + part
print(s)
```

**Output — line by line**

```text
ABC
```
*Single line after all concatenations.*

---

## 21. Find maximum (manual)

**Code — line by line**

```python
nums = [3, 7, 2]
```

*List to search.*

```python
m = nums[0]
```

*Best-so-far starts as first element.*

```python
for n in nums[1:]:
```

*Walk remaining elements: 7, 2.*

```python
    if n > m:
```

*If current is larger than best-so-far…*

```python
        m = n
```

*…update best.*

```python
print(m)
```

*Print largest found.*

**Full program**

```python
nums = [3, 7, 2]
m = nums[0]
for n in nums[1:]:
    if n > m:
        m = n
print(m)
```

**Output — line by line**

```text
7
```
*7 beats 3; 2 does not beat 7.*

---

## 22. Flag pattern

**Code — line by line**

```python
found = False
```

*Assume not found until proven.*

```python
for x in [1, 2, 3]:
```

*Check each value.*

```python
    if x == 2:
```

*Match condition.*

```python
        found = True
```

*Set flag; loop still continues unless you break.*

```python
print(found)
```

*Shows whether any iteration matched.*

**Full program**

```python
found = False
for x in [1, 2, 3]:
    if x == 2:
        found = True
print(found)
```

**Output — line by line**

```text
True
```
*At least one `x` was 2.*

---

## 23. Index with `range(len(...))`

**Code — line by line**

```python
arr = ["p", "q"]
```

*List with two items.*

```python
for i in range(len(arr)):
```

*`len` is 2 → `range(2)` → i is 0, then 1.*

```python
    print(i, arr[i])
```

*Print index and element at that index.*

**Full program**

```python
arr = ["p", "q"]
for i in range(len(arr)):
    print(i, arr[i])
```

**Output — line by line**

```text
0 p
```
*Index 0 → `'p'`.*

```text
1 q
```
*Index 1 → `'q'`.*

---

## 24. Empty sequence

**Code — line by line**

```python
for x in []:
```

*No items → loop body never runs.*

```python
    print(x)
```

*Never executed.*

```python
print("after")
```

*Always runs after the (empty) loop.*

**Full program**

```python
for x in []:
    print(x)
print("after")
```

**Output — line by line**

```text
after
```
*Only the statement after the loop produces output.*

---

## 25. `split` and loop words

**Code — line by line**

```python
for word in "one two".split():
```

*`split()` → `["one", "two"]`; each `word` is one token.*

```python
    print(word)
```

*One word per line.*

**Full program**

```python
for word in "one two".split():
    print(word)
```

**Output — line by line**

```text
one
```
*First token.*

```text
two
```
*Second token.*

---

## 26. Modify list by index

**Code — line by line**

```python
nums = [1, 2, 3]
```

*Original list.*

```python
for i in range(len(nums)):
```

*Indices 0, 1, 2.*

```python
    nums[i] = nums[i] * 2
```

*Replace each slot with double its old value.*

```python
print(nums)
```

*Show list after all updates.*

**Full program**

```python
nums = [1, 2, 3]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums)
```

**Output — line by line**

```text
[2, 4, 6]
```
*Each original value ×2.*

---

## 27. Nested loops — count iterations

**Code — line by line**

```python
count = 0
```

*Start counter.*

```python
for a in [1, 2]:
```

*Two outer values.*

```python
    for b in ["x", "y", "z"]:
```

*Three inner values per outer.*

```python
        count += 1
```

*Runs 2×3 times.*

```python
print(count)
```

*Total inner-body executions.*

**Full program**

```python
count = 0
for a in [1, 2]:
    for b in ["x", "y", "z"]:
        count += 1
print(count)
```

**Output — line by line**

```text
6
```
*2 outer × 3 inner = 6 increments.*

---

## 28. Filter — print only evens

**Code — line by line**

```python
for n in range(5):
```

*`n`: 0,1,2,3,4.*

```python
    if n % 2 == 0:
```

*True when `n` is even.*

```python
        print(n, "even")
```

*Only runs when condition holds.*

**Full program**

```python
for n in range(5):
    if n % 2 == 0:
        print(n, "even")
```

**Output — line by line**

```text
0 even
```
*n=0, even.*

```text
2 even
```
*n=2.*

```text
4 even
```
*n=4. Odd `n` produce no lines.*

---

## 29. Running product

**Code — line by line**

```python
p = 1
```

*Multiplicative identity.*

```python
for f in [2, 3, 4]:
```

*Each factor.*

```python
    p = p * f
```

*Multiply running product by `f`.*

```python
print(p)
```

*Final product.*

**Full program**

```python
p = 1
for f in [2, 3, 4]:
    p = p * f
print(p)
```

**Output — line by line**

```text
24
```
*2 × 3 × 4.*

---

## 30. Formatted output (`f`-string)

**Code — line by line**

```python
for i in range(1, 4):
```

*`i` is 1, 2, 3.*

```python
    print(f"step {i}: {i * 10}")
```

*Inserts `i` and `i*10` into the string.*

**Full program**

```python
for i in range(1, 4):
    print(f"step {i}: {i * 10}")
```

**Output — line by line**

```text
step 1: 10
```
*i=1 → 1×10.*

```text
step 2: 20
```
*i=2.*

```text
step 3: 30
```
*i=3.*

---

## Quick reference

| Pattern | Use |
|---------|-----|
| `for i in range(n)` | Indices 0 … n−1 |
| `for x in sequence` | Each element |
| `enumerate` | Index + element |
| `zip` | Parallel sequences |
| `break` / `continue` | Exit or skip |
| `for … else` | Runs if no `break` |
| Accumulator | Sum, product, build lists |

All examples use **Python 3**.
