# NumPy Assignment: Banking Industry Analysis - Questions Only

## Dataset Overview
The assignment uses banking industry data with 10 rows × 5 columns:
- **Customer_ID**: Unique identifier for each customer
- **Account_Balance**: Customer's account balance in dollars
- **Credit_Score**: Customer's credit score (300-900 range)
- **Transaction_Count**: Number of transactions in the last month
- **Years_Active**: Number of years the customer has been with the bank

## Questions

### Question 1: Array Creation and Manipulation

**Q1.1:** Create a 4x4 identity matrix using `np.eye()`

**Q1.2:** Create an array of 8 zeros using `np.zeros()`

**Q1.3:** Create an array of 6 ones using `np.ones()`

**Q1.4:** Create an array with values from 0 to 15 using `np.arange()`

**Q1.5:** Create an array with 8 evenly spaced values from 0 to 100 using `np.linspace()`

### Question 2: Array Attributes and Information

**Q2.1:** What is the shape of the `banking_data` array?

**Q2.2:** What is the data type of the `banking_data` array?

**Q2.3:** What is the size (total number of elements) of the `banking_data` array?

**Q2.4:** What is the number of dimensions of the `banking_data` array?

**Q2.5:** What is the memory size of the `banking_data` array in bytes?

### Question 3: Indexing and Slicing

**Q3.1:** Extract the first row of `banking_data`

**Q3.2:** Extract the last row of `banking_data`

**Q3.3:** Extract the Account_Balance column (column index 1)

**Q3.4:** Extract the first 4 rows and first 3 columns

**Q3.5:** Extract rows 3 to 7 (inclusive)

### Question 4: Mathematical Operations

**Q4.1:** Calculate the sum of all account balances

**Q4.2:** Calculate the mean account balance

**Q4.3:** Calculate the standard deviation of account balances

**Q4.4:** Calculate the variance of account balances

**Q4.5:** Calculate the median account balance

### Question 5: Statistical Functions

**Q5.1:** Find the minimum and maximum account balances

**Q5.2:** Find the minimum and maximum credit scores

**Q5.3:** Calculate the percentile values for account balances (25th, 50th, 75th)

**Q5.4:** Calculate the correlation between account balance and credit score

**Q5.5:** Calculate the covariance between account balance and credit score

### Question 6: Array Reshaping and Manipulation

**Q6.1:** Reshape the `banking_data` to 5 rows × 10 columns

**Q6.2:** Flatten the `banking_data` to a 1D array

**Q6.3:** Transpose the `banking_data`

**Q6.4:** Split the `banking_data` into 2 equal parts vertically

**Q6.5:** Split the `banking_data` into 2 equal parts horizontally

### Question 7: Logical Operations and Filtering

**Q7.1:** Find customers with account balance greater than $100,000

**Q7.2:** Find customers with credit score greater than 800

**Q7.3:** Find customers with transaction count greater than 50 AND credit score less than 750

**Q7.4:** Count how many customers have account balance between $10,000 and $100,000

**Q7.5:** Find the index of the customer with the highest credit score

### Question 8: Sorting and Searching

**Q8.1:** Sort the `banking_data` by account balance (ascending)

**Q8.2:** Sort the `banking_data` by credit score (descending)

**Q8.3:** Find the indices that would sort the array by years active

**Q8.4:** Find the customer with the second highest account balance

**Q8.5:** Find the customer with the lowest transaction count

### Question 9: Mathematical Functions

**Q9.1:** Calculate the absolute values of all elements

**Q9.2:** Calculate the square root of all account balances

**Q9.3:** Calculate the square of all credit scores

**Q9.4:** Calculate the exponential of all transaction counts

**Q9.5:** Calculate the natural logarithm of all account balances

### Question 10: Advanced Operations

**Q10.1:** Calculate the cumulative sum of account balances

**Q10.2:** Calculate the cumulative product of transaction counts

**Q10.3:** Calculate the difference between consecutive account balances

**Q10.4:** Calculate the gradient of account balances

**Q10.5:** Calculate the histogram of account balances with 5 bins

### Question 11: Random Numbers and Simulation

**Q11.1:** Generate 6 random integers between 1 and 1000

**Q11.2:** Generate 6 random floats between 0 and 1

**Q11.3:** Generate 6 random numbers from normal distribution (mean=700, std=100)

**Q11.4:** Shuffle the `banking_data` rows randomly

**Q11.5:** Set random seed to 123 and generate 4 random numbers

### Question 12: Linear Algebra Operations

**Q12.1:** Calculate the dot product of account balance and credit score columns

**Q12.2:** Calculate the cross product of first two rows

**Q12.3:** Calculate the norm (magnitude) of the account balance column

**Q12.4:** Create a 3x3 matrix and calculate its determinant

**Q12.5:** Calculate the inverse of the 3x3 matrix

### Question 13: String Operations

**Q13.1:** Convert all customer IDs to strings

**Q13.2:** Check if any customer ID contains '100'

**Q13.3:** Convert all customer IDs to uppercase (if they were strings)

**Q13.4:** Count the length of each customer ID string

**Q13.5:** Replace '100' with 'CUST' in customer IDs

### Question 14: Date and Time Operations

**Q14.1:** Convert years active to months

**Q14.2:** Calculate the average years active

**Q14.3:** Find customers who have been active for more than 5 years

**Q14.4:** Calculate the total time all customers have been active (in years)

**Q14.5:** Find the customer with the shortest time active

### Question 15: Advanced Array Operations

**Q15.1:** Apply a function to calculate 5% interest on all account balances

**Q15.2:** Use `np.where` to categorize customers by balance ranges

**Q15.3:** Use `np.select` to categorize customers by credit score ranges

**Q15.4:** Use `np.piecewise` to apply different interest rates based on balance

**Q15.5:** Use `np.apply_along_axis` to calculate the sum of each row

### Question 16: Array Concatenation and Stacking

**Q16.1:** Concatenate two arrays horizontally using `np.hstack()`

**Q16.2:** Concatenate two arrays vertically using `np.vstack()`

**Q16.3:** Concatenate arrays along a specific axis using `np.concatenate()`

**Q16.4:** Stack arrays depth-wise using `np.dstack()`

**Q16.5:** Create a column stack using `np.column_stack()`

### Question 17: Array Splitting Operations

**Q17.1:** Split an array into 3 equal parts using `np.split()`

**Q17.2:** Split an array at specific indices using `np.split()`

**Q17.3:** Split an array horizontally using `np.hsplit()`

**Q17.4:** Split an array vertically using `np.vsplit()`

**Q17.5:** Split an array into equal chunks using `np.array_split()`

### Question 18: Array Repetition and Tiling

**Q18.1:** Repeat each element of an array 3 times using `np.repeat()`

**Q18.2:** Repeat an entire array 2 times using `np.tile()`

**Q18.3:** Repeat a 2D array using `np.tile()`

**Q18.4:** Create a pattern using `np.tile()`

**Q18.5:** Repeat elements with different counts using `np.repeat()`

### Question 19: Array Comparison and Logical Operations

**Q19.1:** Compare two arrays for equality using `np.array_equal()`

**Q19.2:** Check if arrays are close using `np.allclose()`

**Q19.3:** Apply logical AND operation between arrays

**Q19.4:** Apply logical OR operation between arrays

**Q19.5:** Apply logical NOT operation to an array

### Question 20: Array Set Operations

**Q20.1:** Find unique elements in an array using `np.unique()`

**Q20.2:** Find the intersection of two arrays using `np.intersect1d()`

**Q20.3:** Find the union of two arrays using `np.union1d()`

**Q20.4:** Find elements in first array but not in second using `np.setdiff1d()`

**Q20.5:** Find the symmetric difference between two arrays using `np.setxor1d()`

## Learning Objectives

This assignment covers:
- Basic NumPy array operations
- Statistical analysis of banking data
- Array manipulation and reshaping
- Logical operations and filtering
- Mathematical functions and linear algebra
- String operations and data processing
- Performance optimization techniques

## Expected Outcomes

Students should be able to:
- Manipulate banking data using NumPy
- Perform statistical analysis on financial data
- Apply various NumPy functions to real-world scenarios
- Understand array operations and their applications
- Analyze customer behavior patterns in banking data
