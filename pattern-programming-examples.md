# 30 Pattern Programs (Code by Code)

Same style as `for-loop-examples.md`: **each line of code** in its own block with a short explanation, then the **full program**, **how each row/iteration builds the pattern**, and **output row by row** (each printed line of the figure).

Assumptions: **Python 3**. Most patterns use `n = 4` or `n = 5` where noted.

---

## 1. Right-angled triangle — stars

**Code — line by line**

```python
n = 4
```

*Number of rows.*

```python
for i in range(1, n + 1):
```

*Row index `i` runs 1 … n; row `i` will have `i` stars.*

```python
    print("*" * i)
```

*Repeat `*` `i` times; one print per row.*

**Full program**

```python
n = 4
for i in range(1, n + 1):
    print("*" * i)
```

**Each row**

| Row | `i` | Printed |
|-----|-----|---------|
| 1 | 1 | `*` |
| 2 | 2 | `**` |
| 3 | 3 | `***` |
| 4 | 4 | `****` |

**Output — line by line**

```text
*
```
*Row 1: one star.*

```text
**
```
*Row 2.*

```text
***
```
*Row 3.*

```text
****
```
*Row 4: base of the triangle.*

---

## 2. Inverted right-angled triangle — stars

**Code — line by line**

```python
n = 4
```

```python
for i in range(n, 0, -1):
```

*`i` goes n, n−1, …, 1 so each row shrinks.*

```python
    print("*" * i)
```

**Full program**

```python
n = 4
for i in range(n, 0, -1):
    print("*" * i)
```

**Each row** — lengths 4, 3, 2, 1.

**Output — line by line**

```text
****
```
```text
***
```
```text
**
```
```text
*
```

---

## 3. Solid square of stars

**Code — line by line**

```python
n = 3
```

*Square side length.*

```python
for _ in range(n):
```

*Repeat `n` rows; index unused.*

```python
    print("*" * n)
```

*Each row has `n` stars.*

**Full program**

```python
n = 3
for _ in range(n):
    print("*" * n)
```

**Output — line by line**

```text
***
```
```text
***
```
```text
***
```
*Three identical rows → 3×3 block.*

---

## 4. Hollow square

**Code — line by line**

```python
n = 5
```

```python
for i in range(n):
```

*Row index 0 … n−1.*

```python
    if i == 0 or i == n - 1:
```

*First or last row: all stars.*

```python
        print("*" * n)
```

```python
    else:
```

*Middle rows: stars only at ends.*

```python
        print("*" + " " * (n - 2) + "*")
```

**Full program**

```python
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
```

**Output — line by line**

```text
*****
```
*Top border.*

```text
*   *
```
*Hollow middle (spaces inside).*

```text
*   *
```
```text
*   *
```
```text
*****
```
*Bottom border.*

---

## 5. Number triangle (1, 12, 123, …)

**Code — line by line**

```python
n = 4
```

```python
for i in range(1, n + 1):
```

*Row `i` prints digits 1 through `i`.*

```python
    for j in range(1, i + 1):
```

```python
        print(j, end="")
```

*No newline until row ends.*

```python
    print()
```

*End of row.*

**Full program**

```python
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

**Output — line by line**

```text
1
```
```text
12
```
```text
123
```
```text
1234
```
*Each row appends the next digit.*

---

## 6. Floyd’s triangle (continuous numbers)

**Code — line by line**

```python
n = 4
num = 1
```

*`num` tracks the next integer to print.*

```python
for i in range(1, n + 1):
```

```python
    for _ in range(i):
```

*Row `i` prints `i` numbers.*

```python
        print(num, end=" ")
```

```python
        num += 1
```

```python
    print()
```

**Full program**

```python
n = 4
num = 1
for i in range(1, n + 1):
    for _ in range(i):
        print(num, end=" ")
        num += 1
    print()
```

**Output — line by line**

```text
1 
```
*First row: one number.*

```text
2 3 
```
*Second row.*

```text
4 5 6 
```
```text
7 8 9 10 
```
*Numbers run 1 … 10 without resetting per row.*

---

## 7. Centered star pyramid

**Code — line by line**

```python
n = 4
```

```python
for i in range(1, n + 1):
```

```python
    spaces = " " * (n - i)
```

*More spaces on top rows to center the pyramid.*

```python
    stars = "*" * (2 * i - 1)
```

*Odd count: 1, 3, 5, 7…*

```python
    print(spaces + stars)
```

**Full program**

```python
n = 4
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

**Output — line by line**

```text
   *
```
*3 spaces + 1 star.*

```text
  ***
```
```text
 *****
```
```text
*******
```
*Widening centered triangle.*

---

## 8. Inverted centered star pyramid

**Code — line by line**

```python
n = 4
```

```python
for i in range(n, 0, -1):
```

*Start wide, narrow toward bottom.*

```python
    spaces = " " * (n - i)
```

```python
    stars = "*" * (2 * i - 1)
```

```python
    print(spaces + stars)
```

**Full program**

```python
n = 4
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

**Output — line by line**

```text
*******
```
```text
 *****
```
```text
  ***
```
```text
   *
```

---

## 9. Diamond (centered, stars)

**Code — line by line**

```python
n = 4
```

*Top half has `n` rows; bottom mirrors.*

```python
for i in range(1, n + 1):
```

*Upper pyramid (same as example 7).*

```python
    print(" " * (n - i) + "*" * (2 * i - 1))
```

```python
for i in range(n - 1, 0, -1):
```

*Lower inverted part (omit duplicate widest row).*

```python
    print(" " * (n - i) + "*" * (2 * i - 1))
```

**Full program**

```python
n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

**Output — line by line**

```text
   *
```
```text
  ***
```
```text
 *****
```
```text
*******
```
*Top half.*

```text
 *****
```
```text
  ***
```
```text
   *
```
*Bottom half mirrors.*

---

## 10. Same digit per row

**Code — line by line**

```python
n = 4
```

```python
for i in range(1, n + 1):
```

```python
    print((str(i) + " ") * i)
```

*String `i` repeated `i` times with spaces.*

**Full program**

```python
n = 4
for i in range(1, n + 1):
    print((str(i) + " ") * i)
```

**Output — line by line**

```text
1 
```
```text
2 2 
```
```text
3 3 3 
```
```text
4 4 4 4 
```
*Row label repeats across the row.*

---

## 11. Binary triangle (0 and 1)

**Code — line by line**

```python
n = 5
```

```python
val = 1
```

*Start with 1 so first cell prints 1.*

```python
for i in range(1, n + 1):
```

```python
    for _ in range(i):
```

```python
        print(val, end="")
```

```python
        val = 1 - val
```

*Toggles 0 ↔ 1 after each print.*

```python
    print()
```

**Full program**

```python
n = 5
val = 1
for i in range(1, n + 1):
    for _ in range(i):
        print(val, end="")
        val = 1 - val
    print()
```

**Output — line by line**

```text
1
```
```text
01
```
```text
010
```
```text
1010
```
```text
10101
```
*Alternation continues across rows.*

---

## 12. Checkerboard

**Code — line by line**

```python
size = 4
```

```python
for r in range(size):
```

```python
    for c in range(size):
```

```python
        cell = "#" if (r + c) % 2 == 0 else "."
```

*Parity of row+column picks the symbol.*

```python
        print(cell, end=" ")
```

```python
    print()
```

**Full program**

```python
size = 4
for r in range(size):
    for c in range(size):
        cell = "#" if (r + c) % 2 == 0 else "."
        print(cell, end=" ")
    print()
```

**Output — line by line**

```text
# . # . 
```
```text
. # . # 
```
```text
# . # . 
```
```text
. # . # 
```
*Neighboring cells differ.*

---

## 13. Hollow diamond

**Code — line by line**

```python
n = 4
```

*Half-height (widest row is row `n-1`).*

```python
for i in range(n):
```

*Upper part: `i` is 0 … n−1.*

```python
    left = n - i - 1
```

*Leading spaces to center.*

```python
    mid = 2 * i - 1
```

*Gap width between left and right star (negative when `i==0`; handled next).*

```python
    if i == 0:
```

*Tip row: single star.*

```python
        print(" " * left + "*")
```

```python
    else:
```

*Wider rows: star, spaces, star.*

```python
        print(" " * left + "*" + " " * mid + "*")
```

```python
for i in range(n - 2, -1, -1):
```

*Lower part: mirror without duplicating the widest row.*

```python
    left = n - i - 1
```

```python
    mid = 2 * i - 1
```

```python
    if i == 0:
```

```python
        print(" " * left + "*")
```

```python
    else:
```

```python
        print(" " * left + "*" + " " * mid + "*")
```

**Full program**

```python
n = 4
for i in range(n):
    left = n - i - 1
    mid = 2 * i - 1
    if i == 0:
        print(" " * left + "*")
    else:
        print(" " * left + "*" + " " * mid + "*")
for i in range(n - 2, -1, -1):
    left = n - i - 1
    mid = 2 * i - 1
    if i == 0:
        print(" " * left + "*")
    else:
        print(" " * left + "*" + " " * mid + "*")
```

**Output — line by line** (n=4)

```text
   *
```
```text
  * *
```
```text
 *   *
```
```text
*     *
```
```text
 *   *
```
```text
  * *
```
```text
   *
```
*Outline only; interior is spaces.*

---

## 14. Alphabet triangle

**Code — line by line**

```python
n = 4
```

```python
for i in range(1, n + 1):
```

```python
    for j in range(i):
```

```python
        print(chr(ord("A") + j), end="")
```

*Letters A, B, C, … along the row.*

```python
    print()
```

**Full program**

```python
n = 4
for i in range(1, n + 1):
    for j in range(i):
        print(chr(ord("A") + j), end="")
    print()
```

**Output — line by line**

```text
A
```
```text
AB
```
```text
ABC
```
```text
ABCD
```

---

## 15. Centered number pyramid

**Code — line by line**

```python
n = 4
```

```python
for i in range(1, n + 1):
```

```python
    nums = "".join(str(x) for x in range(1, i + 1))
```

*Left half ascending digits.*

```python
    line = nums + nums[-2::-1] if i > 1 else nums
```

*Mirror left part excluding last digit for palindrome row.*

```python
    pad = " " * (n - i)
```

```python
    print(pad + line)
```

**Full program**

```python
n = 4
for i in range(1, n + 1):
    nums = "".join(str(x) for x in range(1, i + 1))
    line = nums + nums[-2::-1] if i > 1 else nums
    pad = " " * (n - i)
    print(pad + line)
```

**Output — line by line**

```text
   1
```
```text
  121
```
```text
 12321
```
```text
1234321
```
*Palindromic numbers, centered.*

---

## 16. Right-aligned number triangle

**Code — line by line**

```python
n = 4
```

```python
for i in range(1, n + 1):
```

```python
    nums = "".join(str(x) for x in range(1, i + 1))
```

```python
    print(nums.rjust(n + i - 1))
```

*Pad with spaces so block aligns right.*

**Full program**

```python
n = 4
for i in range(1, n + 1):
    nums = "".join(str(x) for x in range(1, i + 1))
    print(nums.rjust(n + i - 1))
```

**Output — line by line**

```text
      1
```
```text
     12
```
```text
    123
```
```text
   1234
```
*Hypotenuse on the right.*

---

## 17. Butterfly (stars, two wings)

**Code — line by line**

```python
n = 3
```

*Half-height of wing pair.*

```python
for i in range(1, n + 1):
```

```python
    left = "*" * i
```

```python
    mid = " " * (2 * (n - i))
```

*Gap shrinks as `i` grows.*

```python
    right = "*" * i
```

```python
    print(left + mid + right)
```

```python
for i in range(n, 0, -1):
```

*Mirror the upper half.*

```python
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
```

**Full program**

```python
n = 3
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
```

**Output — line by line**

```text
*     *
```
```text
**   **
```
```text
*** ***
```
```text
**   **
```
```text
*     *
```
*Symmetric wings around a vertical space column.*

---

## 18. Hourglass (stars)

**Code — line by line**

```python
n = 5
```

*Must be odd for single center; or use floor.*

```python
for i in range(n, 0, -2):
```

*Odd widths: n, n−2, …*

```python
    stars = "*" * i
```

```python
    pad = " " * ((n - i) // 2)
```

```python
    print(pad + stars)
```

```python
for i in range(3, n + 1, 2):
```

*Widen again after narrowest row.*

```python
    stars = "*" * i
```

```python
    pad = " " * ((n - i) // 2)
```

```python
    print(pad + stars)
```

**Full program** (n odd, e.g. 5)

```python
n = 5
for i in range(n, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)
for i in range(3, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)
```

**Output — line by line**

```text
*****
```
```text
 ***
```
```text
  *
```
```text
 ***
```
```text
*****
```

---

## 19. Pascal’s triangle (coefficients)

**Code — line by line**

```python
rows = 5
```

```python
prev = []
```

```python
for r in range(rows):
```

```python
    cur = [1]
```

*Each row starts with 1.*

```python
    for j in range(1, r):
```

```python
        cur.append(prev[j - 1] + prev[j])
```

*Interior = sum of two cells above.*

```python
    if r > 0:
```

```python
        cur.append(1)
```

*End 1 for r ≥ 1.*

```python
    print(" ".join(str(x) for x in cur).center(rows * 3))
```

*Rough centering for display.*

```python
    prev = cur
```

**Full program**

```python
rows = 5
prev = []
for r in range(rows):
    cur = [1]
    for j in range(1, r):
        cur.append(prev[j - 1] + prev[j])
    if r > 0:
        cur.append(1)
    print(" ".join(str(x) for x in cur).center(rows * 3))
    prev = cur
```

**Output — line by line** (spacing may vary slightly)

```text
        1        
```
```text
       1 1       
```
```text
      1 2 1      
```
```text
     1 3 3 1     
```
```text
    1 4 6 4 1    
```
*Each number is binomial coefficient.*

---

## 20. X pattern (diagonals)

**Code — line by line**

```python
n = 5
```

*Odd `n` gives a single center star.*

```python
for r in range(n):
```

```python
    for c in range(n):
```

```python
        if r == c or r + c == n - 1:
```

*Main or anti-diagonal.*

```python
            print("*", end="")
```

```python
        else:
```

```python
            print(" ", end="")
```

```python
    print()
```

**Full program**

```python
n = 5
for r in range(n):
    for c in range(n):
        if r == c or r + c == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**Output — line by line**

```text
*   *
```
```text
 * * 
```
```text
  *  
```
```text
 * * 
```
```text
*   *
```

---

## 21. Plus pattern (cross)

**Code — line by line**

```python
n = 5
```

```python
mid = n // 2
```

*Center row and column index.*

```python
for r in range(n):
```

```python
    for c in range(n):
```

```python
        if r == mid or c == mid:
```

```python
            print("*", end="")
```

```python
        else:
```

```python
            print(" ", end="")
```

```python
    print()
```

**Full program**

```python
n = 5
mid = n // 2
for r in range(n):
    for c in range(n):
        if r == mid or c == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**Output — line by line**

```text
  *  
```
```text
  *  
```
```text
*****
```
```text
  *  
```
```text
  *  
```

---

## 22. Number grid (row × column values)

**Code — line by line**

```python
n = 4
```

```python
for r in range(1, n + 1):
```

```python
    for c in range(1, n + 1):
```

```python
        print(r * c, end="\t")
```

*Cell shows product of row and column index.*

```python
    print()
```

**Full program**

```python
n = 4
for r in range(1, n + 1):
    for c in range(1, n + 1):
        print(r * c, end="\t")
    print()
```

**Output — line by line**

```text
1	2	3	4	
```
```text
2	4	6	8	
```
```text
3	6	9	12	
```
```text
4	8	12	16	
```
*Multiplication table snippet.*

---

## 23. Hollow rectangle

**Code — line by line**

```python
rows, cols = 3, 6
```

```python
for r in range(rows):
```

```python
    if r == 0 or r == rows - 1:
```

```python
        print("*" * cols)
```

```python
    else:
```

```python
        print("*" + " " * (cols - 2) + "*")
```

**Full program**

```python
rows, cols = 3, 6
for r in range(rows):
    if r == 0 or r == rows - 1:
        print("*" * cols)
    else:
        print("*" + " " * (cols - 2) + "*")
```

**Output — line by line**

```text
******
```
```text
*    *
```
```text
******
```

---

## 24. Inverted number triangle (all digits to n)

**Code — line by line**

```python
n = 4
```

```python
for i in range(n, 0, -1):
```

```python
    for j in range(1, i + 1):
```

```python
        print(j, end="")
```

```python
    print()
```

**Full program**

```python
n = 4
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

**Output — line by line**

```text
1234
```
```text
123
```
```text
12
```
```text
1
```

---

## 25. Zigzag (stars on a shifting diagonal)

**Code — line by line**

```python
cols = 7
```

*Width of each row.*

```python
for r in range(3):
```

*Three rows.*

```python
    line = [" "] * cols
```

*Start with spaces.*

```python
    for c in range(cols):
```

```python
        if (c + r) % 3 == 0:
```

*Every third column, phase depends on row `r`.*

```python
            line[c] = "*"
```

```python
    print("".join(line))
```

**Full program**

```python
cols = 7
for r in range(3):
    line = [" "] * cols
    for c in range(cols):
        if (c + r) % 3 == 0:
            line[c] = "*"
    print("".join(line))
```

**Output — line by line**

```text
*  *  *
```
*Row 0: columns 0,3,6.*

```text
 *  *  
```
*Row 1: pattern shifts right by one.*

```text
  *  * 
```
*Row 2: shifts again.*

---

## 26. GCD stripes (decorative bands)

**Code — line by line**

```python
h, w = 4, 12
```

```python
for r in range(h):
```

```python
    for c in range(w):
```

```python
        ch = "=" if (r + c) % 3 == 0 else "-"
```

*Three-phase stripe.*

```python
        print(ch, end="")
```

```python
    print()
```

**Full program**

```python
h, w = 4, 12
for r in range(h):
    for c in range(w):
        print("=" if (r + c) % 3 == 0 else "-", end="")
    print()
```

**Output — line by line**

```text
=--=--=--=--=
```
```text
-=-=--=-=-=-=
```
```text
--=--=--=--=-
```
```text
=-=--=-=-=-=-
```
*Where `(r+c) % 3 == 0` prints `=`; otherwise `-` — diagonal bands.*

---

## 27. Staircase blocks (`#`)

**Code — line by line**

```python
n = 4
```

```python
for i in range(1, n + 1):
```

```python
    print(("#" * i).ljust(n) + " " + ("#" * i))
```

*Left block grows; right block same width; gap for “steps”.*

**Full program**

```python
n = 4
for i in range(1, n + 1):
    print(("#" * i).ljust(n) + " " + ("#" * i))
```

**Output — line by line**

```text
#    #
```
```text
##   ##
```
```text
###  ###
```
```text
#### ####
```

---

## 28. Descending triangle of consecutive numbers

**Code — line by line**

```python
n = 4
```

*Row lengths: 4, 3, 2, 1.*

```python
start = n * (n + 1) // 2
```

*Total count of numbers = 1+2+…+n; first printed value.*

```python
for i in range(n, 0, -1):
```

*Each row has `i` numbers.*

```python
    row = []
```

```python
    for _ in range(i):
```

```python
        row.append(str(start))
```

```python
        start -= 1
```

*Global countdown across rows.*

```python
    print(" ".join(row))
```

**Full program**

```python
n = 4
start = n * (n + 1) // 2
for i in range(n, 0, -1):
    row = []
    for _ in range(i):
        row.append(str(start))
        start -= 1
    print(" ".join(row))
```

**Output — line by line**

```text
10 9 8 7
```
```text
6 5 4
```
```text
3 2
```
```text
1
```
*Triangle of numbers counting down overall.*

---

## 29. Square border with digits (interior empty)

**Code — line by line**

```python
n = 5
```

```python
for r in range(n):
```

```python
    for c in range(n):
```

```python
        if r == 0 or r == n - 1 or c == 0 or c == n - 1:
```

*On the outer frame only.*

```python
            print((r + c) % 10, end="")
```

*Digit is sum of indices mod 10.*

```python
        else:
```

```python
            print(" ", end="")
```

```python
    print()
```

**Full program**

```python
n = 5
for r in range(n):
    for c in range(n):
        if r == 0 or r == n - 1 or c == 0 or c == n - 1:
            print((r + c) % 10, end="")
        else:
            print(" ", end="")
    print()
```

**Output — line by line**

```text
01234
```
*Top border: (r+c)%10.*

```text
1   3
```
*Left digit column 0; interior spaces; right column.*

```text
2   4
```
```text
3   5
```
```text
45678
```
*Bottom border completes the ring.*

---

## 30. Arrow head (right-pointing)

**Code — line by line**

```python
n = 5
```

```python
for i in range(1, n + 1, 2):
```

*Odd widths 1,3,5…*

```python
    print("*" * i)
```

```python
for i in range(n - 2, 0, -2):
```

*Shrink after peak.*

```python
    print("*" * i)
```

**Full program**

```python
n = 5
for i in range(1, n + 1, 2):
    print("*" * i)
for i in range(n - 2, 0, -2):
    print("*" * i)
```

**Output — line by line**

```text
*
```
```text
***
```
```text
*****
```
```text
***
```
```text
*
```
*Increases then decreases by steps of 2.*

---

## Quick reference

| Idea | Typical loops |
|------|----------------|
| Rows | Outer `for` over height |
| Columns | Inner `for` over width |
| Centering | ` " " * (n - i)` + pattern |
| Hollow | Print border only when `r/c` at edges |
| Diagonals | `r == c` or `r + c == n - 1` |

File: `pattern-programming-examples.md` — Python 3.
