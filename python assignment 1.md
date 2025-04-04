```python
retail_inventory = {
    "Electronics": {
        "Laptop": [55000, 30, "Dell"],
        "Mobile": [25000, 50, "Samsung"],
        "Tablet": [18000, 20, "Lenovo"],
        "Smart Watch": [7999, 40, "Noise"]
    },
    "Apparel": {
        "T-Shirt": [499, 100, "H&M"],
        "Jeans": [1199, 60, "Levi's"],
        "Jacket": [2499, 25, "Puma"]
    },
    "Home Appliances": {
        "Microwave": [8500, 15, "LG"],
        "Vacuum Cleaner": [7000, 10, "Philips"],
        "Refrigerator": [30000, 8, "Samsung"]
    }
}
```
## 🟢 Easy (Level 1)

1. How do you get all the keys from a dictionary? `(Use .keys())`
2. How do you get all the values from a dictionary? `(Use .values())`
3. How do you retrieve the value for a specific key safely? `(Use .get(key))`
4. How do you check if a key exists in a dictionary? `(Use in)`
5. How do you remove a key and return its value? `(Use .pop(key))`
6. How do you copy a dictionary? `(Use .copy())`
7. How do you remove all key-value pairs from a dictionary? `(Use .clear())`
8. How do you add or update a value for a key? `(Use .update({key: value}))`
9. How do you retrieve both keys and values? `(Use .items())`
10. How do you create an empty dictionary? `(Use {} or dict())`

---

## 🟡 Medium (Level 2)

11. Use `.setdefault()` to assign a default value to a missing key.  
12. Use `.update()` to merge two dictionaries.  
13. Use `.get()` with a default return value if key is not found.  
14. What’s the difference between `.pop()` and `.popitem()`? Try both.  
15. Use `del` to remove a key from a dictionary.  
16. Get the number of keys in a dictionary. `(Use len())`  
17. Convert a list of tuples into a dictionary. `(Use dict() constructor)`  
18. Create a dictionary from two lists: one of keys and one of values. `(Use zip() and dict())`  
19. Check if two dictionaries have the same keys. `(Use .keys() and ==)`  
20. Check if a dictionary is empty. `(Use not or len())`

---

## 🔴 Complex (Level 3 — Still no loops)

21. Get a list of all unique values using `set()` and `.values()`.  
22. Create a nested dictionary using dictionary literals.  
23. Merge 3 dictionaries using chained `.update()`.  
24. Use `.fromkeys()` to create a dictionary with default values.  
25. Use `.get()` to avoid a `KeyError` while accessing a deeply nested dictionary.  
26. Copy a dictionary and modify the copy (check original doesn’t change).  
27. Extract only the keys from a dictionary where the value is a specific type (e.g., list).  
28. Convert a flat dictionary to a string using `str()` or `json.dumps()`.  
29. Check if a dictionary has all keys from a given list using `all()` and `in`.  
30. Use `max()` and `min()` to find keys or values with highest/lowest value.
