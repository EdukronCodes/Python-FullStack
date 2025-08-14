import numpy as np
import pandas as pd

# ============================================================================
# NUMPY ASSIGNMENT: RETAIL DATA ANALYSIS
# ============================================================================

print("=" * 60)
print("NUMPY ASSIGNMENT: RETAIL DATA ANALYSIS")
print("=" * 60)

# Create retail data: 10 rows × 5 columns
# Columns: Product_ID, Price, Quantity_Sold, Customer_Rating, Days_in_Stock
retail_data = np.array([
    [1001, 29.99, 45, 4.2, 15],
    [1002, 49.99, 32, 4.5, 8],
    [1003, 19.99, 78, 3.8, 22],
    [1004, 89.99, 12, 4.7, 5],
    [1005, 15.99, 95, 4.0, 18],
    [1006, 69.99, 28, 4.3, 12],
    [1007, 39.99, 56, 3.9, 20],
    [1008, 79.99, 18, 4.6, 7],
    [1009, 25.99, 67, 4.1, 16],
    [1010, 59.99, 34, 4.4, 10]
])

print("\nORIGINAL RETAIL DATA:")
print(retail_data)
print(f"\nData shape: {retail_data.shape}")
print(f"Data type: {retail_data.dtype}")

# ============================================================================
# QUESTION 1: ARRAY CREATION AND MANIPULATION
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 1: ARRAY CREATION AND MANIPULATION")
print("=" * 60)

print("\nQ1.1: Create a 3x3 identity matrix using np.eye()")
print("Answer:")
identity_matrix = np.eye(3)
print(identity_matrix)

print("\nQ1.2: Create an array of 10 zeros using np.zeros()")
print("Answer:")
zeros_array = np.zeros(10)
print(zeros_array)

print("\nQ1.3: Create an array of 5 ones using np.ones()")
print("Answer:")
ones_array = np.ones(5)
print(ones_array)

print("\nQ1.4: Create an array with values from 0 to 9 using np.arange()")
print("Answer:")
range_array = np.arange(10)
print(range_array)

print("\nQ1.5: Create an array with 6 evenly spaced values from 0 to 10 using np.linspace()")
print("Answer:")
linspace_array = np.linspace(0, 10, 6)
print(linspace_array)

# ============================================================================
# QUESTION 2: ARRAY ATTRIBUTES AND INFORMATION
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 2: ARRAY ATTRIBUTES AND INFORMATION")
print("=" * 60)

print("\nQ2.1: What is the shape of the retail_data array?")
print("Answer:")
print(f"Shape: {retail_data.shape}")

print("\nQ2.2: What is the data type of the retail_data array?")
print("Answer:")
print(f"Data type: {retail_data.dtype}")

print("\nQ2.3: What is the size (total number of elements) of the retail_data array?")
print("Answer:")
print(f"Size: {retail_data.size}")

print("\nQ2.4: What is the number of dimensions of the retail_data array?")
print("Answer:")
print(f"Dimensions: {retail_data.ndim}")

print("\nQ2.5: What is the memory size of the retail_data array in bytes?")
print("Answer:")
print(f"Memory size: {retail_data.nbytes} bytes")

# ============================================================================
# QUESTION 3: INDEXING AND SLICING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 3: INDEXING AND SLICING")
print("=" * 60)

print("\nQ3.1: Extract the first row of retail_data")
print("Answer:")
first_row = retail_data[0]
print(first_row)

print("\nQ3.2: Extract the last row of retail_data")
print("Answer:")
last_row = retail_data[-1]
print(last_row)

print("\nQ3.3: Extract the Price column (column index 1)")
print("Answer:")
price_column = retail_data[:, 1]
print(price_column)

print("\nQ3.4: Extract the first 3 rows and first 2 columns")
print("Answer:")
subset = retail_data[:3, :2]
print(subset)

print("\nQ3.5: Extract rows 2 to 5 (inclusive)")
print("Answer:")
rows_2_to_5 = retail_data[2:6]
print(rows_2_to_5)

# ============================================================================
# QUESTION 4: MATHEMATICAL OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 4: MATHEMATICAL OPERATIONS")
print("=" * 60)

print("\nQ4.1: Calculate the sum of all prices")
print("Answer:")
total_price = np.sum(retail_data[:, 1])
print(f"Total price: ${total_price:.2f}")

print("\nQ4.2: Calculate the mean price")
print("Answer:")
mean_price = np.mean(retail_data[:, 1])
print(f"Mean price: ${mean_price:.2f}")

print("\nQ4.3: Calculate the standard deviation of prices")
print("Answer:")
std_price = np.std(retail_data[:, 1])
print(f"Standard deviation of prices: ${std_price:.2f}")

print("\nQ4.4: Calculate the variance of prices")
print("Answer:")
var_price = np.var(retail_data[:, 1])
print(f"Variance of prices: ${var_price:.2f}")

print("\nQ4.5: Calculate the median price")
print("Answer:")
median_price = np.median(retail_data[:, 1])
print(f"Median price: ${median_price:.2f}")

# ============================================================================
# QUESTION 5: STATISTICAL FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 5: STATISTICAL FUNCTIONS")
print("=" * 60)

print("\nQ5.1: Find the minimum and maximum prices")
print("Answer:")
min_price = np.min(retail_data[:, 1])
max_price = np.max(retail_data[:, 1])
print(f"Minimum price: ${min_price:.2f}")
print(f"Maximum price: ${max_price:.2f}")

print("\nQ5.2: Find the minimum and maximum quantities sold")
print("Answer:")
min_qty = np.min(retail_data[:, 2])
max_qty = np.min(retail_data[:, 2])
print(f"Minimum quantity: {min_qty}")
print(f"Maximum quantity: {max_qty}")

print("\nQ5.3: Calculate the percentile values for prices (25th, 50th, 75th)")
print("Answer:")
percentiles = np.percentile(retail_data[:, 1], [25, 50, 75])
print(f"25th percentile: ${percentiles[0]:.2f}")
print(f"50th percentile: ${percentiles[1]:.2f}")
print(f"75th percentile: ${percentiles[2]:.2f}")

print("\nQ5.4: Calculate the correlation between prices and quantities sold")
print("Answer:")
correlation = np.corrcoef(retail_data[:, 1], retail_data[:, 2])[0, 1]
print(f"Correlation: {correlation:.4f}")

print("\nQ5.5: Calculate the covariance between prices and quantities sold")
print("Answer:")
covariance = np.cov(retail_data[:, 1], retail_data[:, 2])[0, 1]
print(f"Covariance: {covariance:.4f}")

# ============================================================================
# QUESTION 6: ARRAY RESHAPING AND MANIPULATION
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 6: ARRAY RESHAPING AND MANIPULATION")
print("=" * 60)

print("\nQ6.1: Reshape the retail_data to 5 rows × 10 columns")
print("Answer:")
reshaped_5x10 = retail_data.reshape(5, 10)
print(reshaped_5x10)

print("\nQ6.2: Flatten the retail_data to a 1D array")
print("Answer:")
flattened = retail_data.flatten()
print(flattened)

print("\nQ6.3: Transpose the retail_data")
print("Answer:")
transposed = retail_data.T
print(transposed)

print("\nQ6.4: Split the retail_data into 2 equal parts vertically")
print("Answer:")
split_vertical = np.vsplit(retail_data, 2)
print("First part:")
print(split_vertical[0])
print("\nSecond part:")
print(split_vertical[1])

print("\nQ6.5: Split the retail_data into 2 equal parts horizontally")
print("Answer:")
split_horizontal = np.hsplit(retail_data, 2)
print("First part:")
print(split_horizontal[0])
print("\nSecond part:")
print(split_horizontal[1])

# ============================================================================
# QUESTION 7: LOGICAL OPERATIONS AND FILTERING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 7: LOGICAL OPERATIONS AND FILTERING")
print("=" * 60)

print("\nQ7.1: Find products with price greater than $50")
print("Answer:")
expensive_products = retail_data[retail_data[:, 1] > 50]
print(expensive_products)

print("\nQ7.2: Find products with customer rating greater than 4.0")
print("Answer:")
high_rated = retail_data[retail_data[:, 3] > 4.0]
print(high_rated)

print("\nQ7.3: Find products with quantity sold greater than 50 AND price less than $40")
print("Answer:")
popular_affordable = retail_data[(retail_data[:, 2] > 50) & (retail_data[:, 1] < 40)]
print(popular_affordable)

print("\nQ7.4: Count how many products have price between $20 and $60")
print("Answer:")
price_range_count = np.sum((retail_data[:, 1] >= 20) & (retail_data[:, 1] <= 60))
print(f"Products in $20-$60 range: {price_range_count}")

print("\nQ7.5: Find the index of the product with the highest rating")
print("Answer:")
highest_rating_idx = np.argmax(retail_data[:, 3])
print(f"Index: {highest_rating_idx}, Product ID: {retail_data[highest_rating_idx, 0]}")

# ============================================================================
# QUESTION 8: SORTING AND SEARCHING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 8: SORTING AND SEARCHING")
print("=" * 60)

print("\nQ8.1: Sort the retail_data by price (ascending)")
print("Answer:")
sorted_by_price = retail_data[retail_data[:, 1].argsort()]
print(sorted_by_price)

print("\nQ8.2: Sort the retail_data by quantity sold (descending)")
print("Answer:")
sorted_by_qty_desc = retail_data[(-retail_data[:, 2]).argsort()]
print(sorted_by_qty_desc)

print("\nQ8.3: Find the indices that would sort the array by customer rating")
print("Answer:")
rating_sort_indices = np.argsort(retail_data[:, 3])
print(rating_sort_indices)

print("\nQ8.4: Find the product with the second highest price")
print("Answer:")
second_highest_price_idx = np.argsort(retail_data[:, 1])[-2]
second_highest_product = retail_data[second_highest_price_idx]
print(f"Product ID: {second_highest_product[0]}, Price: ${second_highest_product[1]:.2f}")

print("\nQ8.5: Find the product with the lowest quantity sold")
print("Answer:")
lowest_qty_idx = np.argmin(retail_data[:, 2])
lowest_qty_product = retail_data[lowest_qty_idx]
print(f"Product ID: {lowest_qty_product[0]}, Quantity: {lowest_qty_product[2]}")

# ============================================================================
# QUESTION 9: MATHEMATICAL FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 9: MATHEMATICAL FUNCTIONS")
print("=" * 60)

print("\nQ9.1: Calculate the absolute values of all elements")
print("Answer:")
absolute_values = np.abs(retail_data)
print(absolute_values)

print("\nQ9.2: Calculate the square root of all prices")
print("Answer:")
sqrt_prices = np.sqrt(retail_data[:, 1])
print(sqrt_prices)

print("\nQ9.3: Calculate the square of all quantities sold")
print("Answer:")
squared_qty = np.square(retail_data[:, 2])
print(squared_qty)

print("\nQ9.4: Calculate the exponential of all customer ratings")
print("Answer:")
exp_ratings = np.exp(retail_data[:, 3])
print(exp_ratings)

print("\nQ9.5: Calculate the natural logarithm of all prices")
print("Answer:")
log_prices = np.log(retail_data[:, 1])
print(log_prices)

# ============================================================================
# QUESTION 10: ADVANCED OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 10: ADVANCED OPERATIONS")
print("=" * 60)

print("\nQ10.1: Calculate the cumulative sum of prices")
print("Answer:")
cumsum_prices = np.cumsum(retail_data[:, 1])
print(cumsum_prices)

print("\nQ10.2: Calculate the cumulative product of quantities sold")
print("Answer:")
cumprod_qty = np.cumprod(retail_data[:, 2])
print(cumprod_qty)

print("\nQ10.3: Calculate the difference between consecutive prices")
print("Answer:")
diff_prices = np.diff(retail_data[:, 1])
print(diff_prices)

print("\nQ10.4: Calculate the gradient of prices")
print("Answer:")
gradient_prices = np.gradient(retail_data[:, 1])
print(gradient_prices)

print("\nQ10.5: Calculate the histogram of prices with 5 bins")
print("Answer:")
hist_prices, bin_edges = np.histogram(retail_data[:, 1], bins=5)
print(f"Histogram counts: {hist_prices}")
print(f"Bin edges: {bin_edges}")

# ============================================================================
# QUESTION 11: RANDOM NUMBERS AND SIMULATION
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 11: RANDOM NUMBERS AND SIMULATION")
print("=" * 60)

print("\nQ11.1: Generate 5 random integers between 1 and 100")
print("Answer:")
random_ints = np.random.randint(1, 101, 5)
print(random_ints)

print("\nQ11.2: Generate 5 random floats between 0 and 1")
print("Answer:")
random_floats = np.random.random(5)
print(random_floats)

print("\nQ11.3: Generate 5 random numbers from normal distribution (mean=0, std=1)")
print("Answer:")
normal_random = np.random.normal(0, 1, 5)
print(normal_random)

print("\nQ11.4: Shuffle the retail_data rows randomly")
print("Answer:")
shuffled_data = retail_data.copy()
np.random.shuffle(shuffled_data)
print(shuffled_data)

print("\nQ11.5: Set random seed to 42 and generate 3 random numbers")
print("Answer:")
np.random.seed(42)
seeded_random = np.random.random(3)
print(seeded_random)

# ============================================================================
# QUESTION 12: LINEAR ALGEBRA OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 12: LINEAR ALGEBRA OPERATIONS")
print("=" * 60)

print("\nQ12.1: Calculate the dot product of price and quantity columns")
print("Answer:")
dot_product = np.dot(retail_data[:, 1], retail_data[:, 2])
print(f"Dot product: {dot_product:.2f}")

print("\nQ12.2: Calculate the cross product of first two rows")
print("Answer:")
cross_product = np.cross(retail_data[0, :3], retail_data[1, :3])
print(cross_product)

print("\nQ12.3: Calculate the norm (magnitude) of the price column")
print("Answer:")
price_norm = np.linalg.norm(retail_data[:, 1])
print(f"Price norm: {price_norm:.2f}")

print("\nQ12.4: Create a 2x2 matrix and calculate its determinant")
print("Answer:")
matrix_2x2 = np.array([[2, 3], [1, 4]])
determinant = np.linalg.det(matrix_2x2)
print(f"Matrix:\n{matrix_2x2}")
print(f"Determinant: {determinant}")

print("\nQ12.5: Calculate the inverse of the 2x2 matrix")
print("Answer:")
inverse_matrix = np.linalg.inv(matrix_2x2)
print(f"Inverse matrix:\n{inverse_matrix}")

# ============================================================================
# QUESTION 13: STRING OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 13: STRING OPERATIONS")
print("=" * 60)

print("\nQ13.1: Convert all product IDs to strings")
print("Answer:")
product_ids_str = retail_data[:, 0].astype(str)
print(product_ids_str)

print("\nQ13.2: Check if any product ID contains '100'")
print("Answer:")
contains_100 = np.char.find(product_ids_str, '100') >= 0
print(contains_100)

print("\nQ13.3: Convert all product IDs to uppercase (if they were strings)")
print("Answer:")
# Since they're numbers, we'll convert to string first
product_ids_upper = np.char.upper(product_ids_str)
print(product_ids_upper)

print("\nQ13.4: Count the length of each product ID string")
print("Answer:")
id_lengths = np.char.str_len(product_ids_str)
print(id_lengths)

print("\nQ13.5: Replace '100' with 'PROD' in product IDs")
print("Answer:")
replaced_ids = np.char.replace(product_ids_str, '100', 'PROD')
print(replaced_ids)

# ============================================================================
# QUESTION 14: DATE AND TIME OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 14: DATE AND TIME OPERATIONS")
print("=" * 60)

print("\nQ14.1: Convert days in stock to hours")
print("Answer:")
days_to_hours = retail_data[:, 4] * 24
print(days_to_hours)

print("\nQ14.2: Calculate the average days in stock")
print("Answer:")
avg_days = np.mean(retail_data[:, 4])
print(f"Average days in stock: {avg_days:.1f}")

print("\nQ14.3: Find products that have been in stock for more than 15 days")
print("Answer:")
long_stock = retail_data[retail_data[:, 4] > 15]
print(long_stock)

print("\nQ14.4: Calculate the total time all products have been in stock (in days)")
print("Answer:")
total_stock_time = np.sum(retail_data[:, 4])
print(f"Total stock time: {total_stock_time} days")

print("\nQ14.5: Find the product with the shortest time in stock")
print("Answer:")
shortest_stock_idx = np.argmin(retail_data[:, 4])
shortest_stock_product = retail_data[shortest_stock_idx]
print(f"Product ID: {shortest_stock_product[0]}, Days: {shortest_stock_product[4]}")

# ============================================================================
# QUESTION 15: ADVANCED ARRAY OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 15: ADVANCED ARRAY OPERATIONS")
print("=" * 60)

print("\nQ15.1: Apply a function to square all prices")
print("Answer:")
def square_price(x):
    return x ** 2

squared_prices = np.vectorize(square_price)(retail_data[:, 1])
print(squared_prices)

print("\nQ15.2: Use np.where to replace prices > $50 with 'Expensive' and others with 'Affordable'")
print("Answer:")
price_labels = np.where(retail_data[:, 1] > 50, 'Expensive', 'Affordable')
print(price_labels)

print("\nQ15.3: Use np.select to categorize products by price ranges")
print("Answer:")
conditions = [
    retail_data[:, 1] < 20,
    (retail_data[:, 1] >= 20) & (retail_data[:, 1] < 50),
    retail_data[:, 1] >= 50
]
choices = ['Budget', 'Mid-range', 'Premium']
price_categories = np.select(conditions, choices, default='Unknown')
print(price_categories)

print("\nQ15.4: Use np.piecewise to apply different functions based on price ranges")
print("Answer:")
def low_price(x): return x * 0.9  # 10% discount
def mid_price(x): return x * 1.0  # No change
def high_price(x): return x * 1.1  # 10% markup

discounted_prices = np.piecewise(
    retail_data[:, 1],
    [retail_data[:, 1] < 20, (retail_data[:, 1] >= 20) & (retail_data[:, 1] < 50), retail_data[:, 1] >= 50],
    [low_price, mid_price, high_price]
)
print(discounted_prices)

print("\nQ15.5: Use np.apply_along_axis to calculate the sum of each row")
print("Answer:")
row_sums = np.apply_along_axis(np.sum, 1, retail_data)
print(row_sums)

# ============================================================================
# QUESTION 16: ARRAY CONCATENATION AND STACKING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 16: ARRAY CONCATENATION AND STACKING")
print("=" * 60)

print("\nQ16.1: Concatenate two arrays horizontally using np.hstack()")
print("Answer:")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
hstacked = np.hstack([arr1, arr2])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Horizontally stacked: {hstacked}")

print("\nQ16.2: Concatenate two arrays vertically using np.vstack()")
print("Answer:")
vstacked = np.vstack([arr1, arr2])
print(f"Vertically stacked:\n{vstacked}")

print("\nQ16.3: Concatenate arrays along a specific axis using np.concatenate()")
print("Answer:")
concatenated = np.concatenate([arr1, arr2], axis=0)
print(f"Concatenated along axis 0: {concatenated}")

print("\nQ16.4: Stack arrays depth-wise using np.dstack()")
print("Answer:")
dstacked = np.dstack([arr1, arr2])
print(f"Depth-wise stacked:\n{dstacked}")

print("\nQ16.5: Create a column stack using np.column_stack()")
print("Answer:")
col_stacked = np.column_stack([arr1, arr2])
print(f"Column stacked:\n{col_stacked}")

# ============================================================================
# QUESTION 17: ARRAY SPLITTING OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 17: ARRAY SPLITTING OPERATIONS")
print("=" * 60)

print("\nQ17.1: Split an array into 3 equal parts using np.split()")
print("Answer:")
arr_to_split = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
split_parts = np.split(arr_to_split, 3)
print(f"Original array: {arr_to_split}")
for i, part in enumerate(split_parts):
    print(f"Part {i+1}: {part}")

print("\nQ17.2: Split an array at specific indices using np.split()")
print("Answer:")
split_at_indices = np.split(arr_to_split, [3, 6])
print(f"Split at indices [3, 6]:")
for i, part in enumerate(split_at_indices):
    print(f"Part {i+1}: {part}")

print("\nQ17.3: Split an array horizontally using np.hsplit()")
print("Answer:")
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
hsplit_parts = np.hsplit(arr_2d, 3)
print(f"Original 2D array:\n{arr_2d}")
for i, part in enumerate(hsplit_parts):
    print(f"Horizontal part {i+1}:\n{part}")

print("\nQ17.4: Split an array vertically using np.vsplit()")
print("Answer:")
vsplit_parts = np.vsplit(arr_2d, 2)
print(f"Vertical parts:")
for i, part in enumerate(vsplit_parts):
    print(f"Part {i+1}:\n{part}")

print("\nQ17.5: Split an array into equal chunks using np.array_split()")
print("Answer:")
chunks = np.array_split(arr_to_split, 4)
print(f"Split into 4 chunks:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")

# ============================================================================
# QUESTION 18: ARRAY REPETITION AND TILING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 18: ARRAY REPETITION AND TILING")
print("=" * 60)

print("\nQ18.1: Repeat each element of an array 3 times using np.repeat()")
print("Answer:")
repeat_elements = np.repeat(arr1, 3)
print(f"Original: {arr1}")
print(f"Repeated 3 times: {repeat_elements}")

print("\nQ18.2: Repeat an entire array 2 times using np.tile()")
print("Answer:")
tiled_array = np.tile(arr1, 2)
print(f"Original: {arr1}")
print(f"Tiled 2 times: {tiled_array}")

print("\nQ18.3: Repeat a 2D array using np.tile()")
print("Answer:")
arr_2d_small = np.array([[1, 2], [3, 4]])
tiled_2d = np.tile(arr_2d_small, (2, 3))
print(f"Original:\n{arr_2d_small}")
print(f"Tiled (2, 3):\n{tiled_2d}")

print("\nQ18.4: Create a pattern using np.tile()")
print("Answer:")
pattern = np.array([1, 0])
pattern_tiled = np.tile(pattern, 5)
print(f"Pattern: {pattern}")
print(f"Tiled 5 times: {pattern_tiled}")

print("\nQ18.5: Repeat elements with different counts using np.repeat()")
print("Answer:")
repeat_counts = [2, 1, 3]
repeated_variable = np.repeat(arr1, repeat_counts)
print(f"Original: {arr1}")
print(f"Repeat counts: {repeat_counts}")
print(f"Result: {repeated_variable}")

# ============================================================================
# QUESTION 19: ARRAY COMPARISON AND LOGICAL OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 19: ARRAY COMPARISON AND LOGICAL OPERATIONS")
print("=" * 60)

print("\nQ19.1: Compare two arrays for equality using np.array_equal()")
print("Answer:")
arr_a = np.array([1, 2, 3])
arr_b = np.array([1, 2, 3])
arr_c = np.array([1, 2, 4])
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"Array C: {arr_c}")
print(f"A equals B: {np.array_equal(arr_a, arr_b)}")
print(f"A equals C: {np.array_equal(arr_a, arr_c)}")

print("\nQ19.2: Check if arrays are close using np.allclose()")
print("Answer:")
arr_d = np.array([1.0, 2.0, 3.0])
arr_e = np.array([1.001, 2.001, 3.001])
print(f"Array D: {arr_d}")
print(f"Array E: {arr_e}")
print(f"Arrays are close: {np.allclose(arr_d, arr_e, atol=0.01)}")

print("\nQ19.3: Apply logical AND operation between arrays")
print("Answer:")
logical_and = np.logical_and(arr_a > 1, arr_a < 3)
print(f"Array: {arr_a}")
print(f"Logical AND (1 < x < 3): {logical_and}")

print("\nQ19.4: Apply logical OR operation between arrays")
print("Answer:")
logical_or = np.logical_or(arr_a == 1, arr_a == 3)
print(f"Array: {arr_a}")
print(f"Logical OR (x == 1 OR x == 3): {logical_or}")

print("\nQ19.5: Apply logical NOT operation to an array")
print("Answer:")
logical_not = np.logical_not(arr_a == 2)
print(f"Array: {arr_a}")
print(f"Logical NOT (x != 2): {logical_not}")

# ============================================================================
# QUESTION 20: ARRAY SET OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 20: ARRAY SET OPERATIONS")
print("=" * 60)

print("\nQ20.1: Find unique elements in an array using np.unique()")
print("Answer:")
arr_with_duplicates = np.array([1, 2, 2, 3, 3, 3, 4])
unique_elements = np.unique(arr_with_duplicates)
print(f"Original array: {arr_with_duplicates}")
print(f"Unique elements: {unique_elements}")

print("\nQ20.2: Find the intersection of two arrays using np.intersect1d()")
print("Answer:")
arr_f = np.array([1, 2, 3, 4])
arr_g = np.array([3, 4, 5, 6])
intersection = np.intersect1d(arr_f, arr_g)
print(f"Array F: {arr_f}")
print(f"Array G: {arr_g}")
print(f"Intersection: {intersection}")

print("\nQ20.3: Find the union of two arrays using np.union1d()")
print("Answer:")
union = np.union1d(arr_f, arr_g)
print(f"Union: {union}")

print("\nQ20.4: Find elements in first array but not in second using np.setdiff1d()")
print("Answer:")
set_difference = np.setdiff1d(arr_f, arr_g)
print(f"Elements in F but not in G: {set_difference}")

print("\nQ20.5: Find the symmetric difference between two arrays using np.setxor1d()")
print("Answer:")
symmetric_diff = np.setxor1d(arr_f, arr_g)
print(f"Symmetric difference: {symmetric_diff}")

# ============================================================================
# QUESTION 21: ARRAY SEARCHING AND COUNTING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 21: ARRAY SEARCHING AND COUNTING")
print("=" * 60)

print("\nQ21.1: Count occurrences of a value using np.count_nonzero()")
print("Answer:")
arr_with_values = np.array([1, 2, 2, 3, 2, 4, 2])
count_of_2 = np.count_nonzero(arr_with_values == 2)
print(f"Array: {arr_with_values}")
print(f"Count of 2: {count_of_2}")

print("\nQ21.2: Find indices where a condition is True using np.where()")
print("Answer:")
indices_greater_than_2 = np.where(arr_with_values > 2)
print(f"Array: {arr_with_values}")
print(f"Indices where x > 2: {indices_greater_than_2[0]}")

print("\nQ21.3: Find the first index where a condition is True using np.argwhere()")
print("Answer:")
first_index_greater_than_2 = np.argwhere(arr_with_values > 2)[0][0]
print(f"First index where x > 2: {first_index_greater_than_2}")

print("\nQ21.4: Check if any element satisfies a condition using np.any()")
print("Answer:")
any_greater_than_3 = np.any(arr_with_values > 3)
print(f"Array: {arr_with_values}")
print(f"Any element > 3: {any_greater_than_3}")

print("\nQ21.5: Check if all elements satisfy a condition using np.all()")
print("Answer:")
all_positive = np.all(arr_with_values > 0)
print(f"Array: {arr_with_values}")
print(f"All elements > 0: {all_positive}")

# ============================================================================
# QUESTION 22: ARRAY BROADCASTING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 22: ARRAY BROADCASTING")
print("=" * 60)

print("\nQ22.1: Demonstrate broadcasting with a scalar")
print("Answer:")
scalar = 5
broadcasted = arr_a + scalar
print(f"Array: {arr_a}")
print(f"Scalar: {scalar}")
print(f"Broadcasted result: {broadcasted}")

print("\nQ22.2: Demonstrate broadcasting with different shapes")
print("Answer:")
arr_2d_broadcast = np.array([[1], [2], [3]])
arr_1d_broadcast = np.array([10, 20])
broadcasted_2d = arr_2d_broadcast + arr_1d_broadcast
print(f"2D array:\n{arr_2d_broadcast}")
print(f"1D array: {arr_1d_broadcast}")
print(f"Broadcasted result:\n{broadcasted_2d}")

print("\nQ22.3: Demonstrate broadcasting with np.newaxis")
print("Answer:")
arr_newaxis = arr_a[:, np.newaxis]
print(f"Original array: {arr_a}")
print(f"With newaxis:\n{arr_newaxis}")

print("\nQ22.4: Demonstrate broadcasting with np.outer()")
print("Answer:")
outer_product = np.outer(arr_a, arr_b)
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"Outer product:\n{outer_product}")

print("\nQ22.5: Demonstrate broadcasting with np.einsum()")
print("Answer:")
einsum_result = np.einsum('i,j->ij', arr_a, arr_b)
print(f"Einsum result:\n{einsum_result}")

# ============================================================================
# QUESTION 23: ARRAY ITERATION AND INDEXING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 23: ARRAY ITERATION AND INDEXING")
print("=" * 60)

print("\nQ23.1: Iterate over array elements using np.nditer()")
print("Answer:")
print("Iterating over array elements:")
for element in np.nditer(arr_a):
    print(f"Element: {element}")

print("\nQ23.2: Iterate over array with index using np.ndenumerate()")
print("Answer:")
print("Iterating with indices:")
for index, element in np.ndenumerate(arr_a):
    print(f"Index {index}: {element}")

print("\nQ23.3: Use advanced indexing with boolean arrays")
print("Answer:")
bool_mask = np.array([True, False, True])
advanced_indexed = arr_a[bool_mask]
print(f"Array: {arr_a}")
print(f"Boolean mask: {bool_mask}")
print(f"Advanced indexed result: {advanced_indexed}")

print("\nQ23.4: Use integer array indexing")
print("Answer:")
int_indices = np.array([0, 2])
integer_indexed = arr_a[int_indices]
print(f"Array: {arr_a}")
print(f"Integer indices: {int_indices}")
print(f"Integer indexed result: {integer_indexed}")

print("\nQ23.5: Use fancy indexing with multiple arrays")
print("Answer:")
row_indices = np.array([0, 1])
col_indices = np.array([1, 2])
arr_2d_fancy = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
fancy_indexed = arr_2d_fancy[row_indices, col_indices]
print(f"2D array:\n{arr_2d_fancy}")
print(f"Row indices: {row_indices}")
print(f"Column indices: {col_indices}")
print(f"Fancy indexed result: {fancy_indexed}")

# ============================================================================
# QUESTION 24: ARRAY VIEWS AND COPIES
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 24: ARRAY VIEWS AND COPIES")
print("=" * 60)

print("\nQ24.1: Create a view of an array using slicing")
print("Answer:")
arr_original = np.array([1, 2, 3, 4, 5])
arr_view = arr_original[1:4]
print(f"Original array: {arr_original}")
print(f"View: {arr_view}")
print(f"Are they the same object? {arr_view is arr_original}")
print(f"Do they share memory? {arr_view.base is arr_original}")

print("\nQ24.2: Create a copy of an array using np.copy()")
print("Answer:")
arr_copy = np.copy(arr_original)
print(f"Original array: {arr_original}")
print(f"Copy: {arr_copy}")
print(f"Are they the same object? {arr_copy is arr_original}")
print(f"Do they share memory? {arr_copy.base is arr_original}")

print("\nQ24.3: Demonstrate the difference between view and copy")
print("Answer:")
arr_original[0] = 99
print(f"After modifying original:")
print(f"Original: {arr_original}")
print(f"View: {arr_view}")
print(f"Copy: {arr_copy}")

print("\nQ24.4: Create a view using np.view()")
print("Answer:")
arr_view_method = arr_original.view()
print(f"Original: {arr_original}")
print(f"View: {arr_view_method}")
print(f"Are they the same object? {arr_view_method is arr_original}")

print("\nQ24.5: Check if an array is a view or copy")
print("Answer:")
print(f"Original base: {arr_original.base}")
print(f"View base: {arr_view.base}")
print(f"Copy base: {arr_copy.base}")

# ============================================================================
# QUESTION 25: ARRAY MEMORY LAYOUT
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 25: ARRAY MEMORY LAYOUT")
print("=" * 60)

print("\nQ25.1: Check if an array is C-contiguous using np.flags")
print("Answer:")
print(f"Array flags:")
print(f"C-contiguous: {arr_a.flags.c_contiguous}")
print(f"F-contiguous: {arr_a.flags.f_contiguous}")

print("\nQ25.2: Check array memory layout using np.flags")
print("Answer:")
print(f"Memory layout flags:")
print(f"OWNDATA: {arr_a.flags.owndata}")
print(f"WRITEABLE: {arr_a.flags.writeable}")
print(f"ALIGNED: {arr_a.flags.aligned}")

print("\nQ25.3: Make an array C-contiguous using np.ascontiguousarray()")
print("Answer:")
arr_f_style = np.array([[1, 2], [3, 4]], order='F')
arr_c_style = np.ascontiguousarray(arr_f_style)
print(f"F-style array:\n{arr_f_style}")
print(f"C-style array:\n{arr_c_style}")
print(f"F-style C-contiguous: {arr_f_style.flags.c_contiguous}")
print(f"C-style C-contiguous: {arr_c_style.flags.c_contiguous}")

print("\nQ25.4: Check array strides")
print("Answer:")
print(f"Array shape: {arr_a.shape}")
print(f"Array strides: {arr_a.strides}")
print(f"Array itemsize: {arr_a.itemsize}")

print("\nQ25.5: Reshape array without copying using np.reshape()")
print("Answer:")
reshaped_no_copy = arr_a.reshape(1, 3)
print(f"Original: {arr_a}")
print(f"Reshaped: {reshaped_no_copy}")
print(f"Share memory? {reshaped_no_copy.base is arr_a}")

# ============================================================================
# QUESTION 26: ARRAY POLYNOMIAL OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 26: ARRAY POLYNOMIAL OPERATIONS")
print("=" * 60)

print("\nQ26.1: Create a polynomial from roots using np.poly()")
print("Answer:")
roots = np.array([1, 2, 3])
polynomial = np.poly(roots)
print(f"Roots: {roots}")
print(f"Polynomial coefficients: {polynomial}")

print("\nQ26.2: Find roots of a polynomial using np.roots()")
print("Answer:")
coeffs = np.array([1, -6, 11, -6])
roots_found = np.roots(coeffs)
print(f"Coefficients: {coeffs}")
print(f"Roots: {roots_found}")

print("\nQ26.3: Evaluate a polynomial using np.polyval()")
print("Answer:")
x_values = np.array([0, 1, 2, 3])
poly_values = np.polyval(coeffs, x_values)
print(f"Coefficients: {coeffs}")
print(f"X values: {x_values}")
print(f"Polynomial values: {poly_values}")

print("\nQ26.4: Add two polynomials using np.polyadd()")
print("Answer:")
poly1 = np.array([1, 2, 3])
poly2 = np.array([4, 5])
sum_poly = np.polyadd(poly1, poly2)
print(f"Polynomial 1: {poly1}")
print(f"Polynomial 2: {poly2}")
print(f"Sum: {sum_poly}")

print("\nQ26.5: Multiply two polynomials using np.polymul()")
print("Answer:")
product_poly = np.polymul(poly1, poly2)
print(f"Product: {product_poly}")

# ============================================================================
# QUESTION 27: ARRAY FINANCIAL FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 27: ARRAY FINANCIAL FUNCTIONS")
print("=" * 60)

print("\nQ27.1: Calculate future value using np.fv()")
print("Answer:")
rate = 0.05  # 5% interest rate
nper = 10    # 10 periods
pmt = -100   # Payment of $100
pv = -1000   # Present value of $1000
fv = np.fv(rate, nper, pmt, pv)
print(f"Rate: {rate}, Periods: {nper}, Payment: {pmt}, PV: {pv}")
print(f"Future Value: ${fv:.2f}")

print("\nQ27.2: Calculate present value using np.pv()")
print("Answer:")
fv_value = 2000
pv_calculated = np.pv(rate, nper, pmt, fv_value)
print(f"Present Value: ${pv_calculated:.2f}")

print("\nQ27.3: Calculate payment amount using np.pmt()")
print("Answer:")
payment = np.pmt(rate, nper, pv, fv_value)
print(f"Payment amount: ${payment:.2f}")

print("\nQ27.4: Calculate number of periods using np.nper()")
print("Answer:")
periods = np.nper(rate, pmt, pv, fv_value)
print(f"Number of periods: {periods:.1f}")

print("\nQ27.5: Calculate interest rate using np.rate()")
print("Answer:")
interest_rate = np.rate(nper, pmt, pv, fv_value)
print(f"Interest rate: {interest_rate:.4f}")

# ============================================================================
# QUESTION 28: ARRAY DISCRETE FOURIER TRANSFORM
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 28: ARRAY DISCRETE FOURIER TRANSFORM")
print("=" * 60)

print("\nQ28.1: Compute 1D FFT using np.fft.fft()")
print("Answer:")
signal = np.array([1, 2, 3, 4, 5, 6, 7, 8])
fft_result = np.fft.fft(signal)
print(f"Signal: {signal}")
print(f"FFT result (first 4 values): {fft_result[:4]}")

print("\nQ28.2: Compute inverse FFT using np.fft.ifft()")
print("Answer:")
ifft_result = np.fft.ifft(fft_result)
print(f"Inverse FFT result: {ifft_result.real}")

print("\nQ28.3: Compute 2D FFT using np.fft.fft2()")
print("Answer:")
signal_2d = np.array([[1, 2], [3, 4]])
fft_2d = np.fft.fft2(signal_2d)
print(f"2D signal:\n{signal_2d}")
print(f"2D FFT:\n{fft_2d}")

print("\nQ28.4: Compute FFT frequency bins using np.fft.fftfreq()")
print("Answer:")
freq_bins = np.fft.fftfreq(8)
print(f"Frequency bins: {freq_bins}")

print("\nQ28.5: Shift zero-frequency component to center using np.fft.fftshift()")
print("Answer:")
fft_shifted = np.fft.fftshift(fft_result)
print(f"Shifted FFT (first 4 values): {fft_shifted[:4]}")

# ============================================================================
# QUESTION 29: ARRAY INTERPOLATION
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 29: ARRAY INTERPOLATION")
print("=" * 60)

print("\nQ29.1: Linear interpolation using np.interp()")
print("Answer:")
x_known = np.array([0, 1, 2, 3, 4])
y_known = np.array([0, 1, 4, 9, 16])
x_new = np.array([0.5, 1.5, 2.5, 3.5])
y_interpolated = np.interp(x_new, x_known, y_known)
print(f"Known x: {x_known}")
print(f"Known y: {y_known}")
print(f"New x: {x_new}")
print(f"Interpolated y: {y_interpolated}")

print("\nQ29.2: Polynomial interpolation using np.polyfit() and np.polyval()")
print("Answer:")
coefficients = np.polyfit(x_known, y_known, 2)
y_poly = np.polyval(coefficients, x_new)
print(f"Polynomial coefficients: {coefficients}")
print(f"Polynomial interpolated y: {y_poly}")

print("\nQ29.3: 1D interpolation using scipy.interpolate (if available)")
print("Answer:")
try:
    from scipy import interpolate
    f = interpolate.interp1d(x_known, y_known, kind='cubic')
    y_cubic = f(x_new)
    print(f"Cubic interpolated y: {y_cubic}")
except ImportError:
    print("SciPy not available for cubic interpolation")

print("\nQ29.4: Interpolate missing values using np.interp()")
print("Answer:")
data_with_nan = np.array([1, np.nan, 3, np.nan, 5])
valid_indices = ~np.isnan(data_with_nan)
x_valid = np.arange(len(data_with_nan))[valid_indices]
y_valid = data_with_nan[valid_indices]
x_all = np.arange(len(data_with_nan))
interpolated_data = np.interp(x_all, x_valid, y_valid)
print(f"Original data: {data_with_nan}")
print(f"Interpolated data: {interpolated_data}")

print("\nQ29.5: 2D interpolation using np.meshgrid()")
print("Answer:")
x = np.array([0, 1, 2])
y = np.array([0, 1, 2])
z = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4]])
X, Y = np.meshgrid(x, y)
print(f"X meshgrid:\n{X}")
print(f"Y meshgrid:\n{Y}")
print(f"Z values:\n{z}")

# ============================================================================
# QUESTION 30: ARRAY SIGNAL PROCESSING
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 30: ARRAY SIGNAL PROCESSING")
print("=" * 60)

print("\nQ30.1: Create a sine wave signal")
print("Answer:")
t = np.linspace(0, 2*np.pi, 100)
sine_wave = np.sin(t)
print(f"Time points: {len(t)}")
print(f"Sine wave amplitude range: [{np.min(sine_wave):.3f}, {np.max(sine_wave):.3f}]")

print("\nQ30.2: Add noise to a signal")
print("Answer:")
noise = np.random.normal(0, 0.1, len(sine_wave))
noisy_signal = sine_wave + noise
print(f"Noise standard deviation: {np.std(noise):.3f}")
print(f"Signal-to-noise ratio: {np.std(sine_wave)/np.std(noise):.3f}")

print("\nQ30.3: Apply a moving average filter")
print("Answer:")
window_size = 5
moving_avg = np.convolve(noisy_signal, np.ones(window_size)/window_size, mode='valid')
print(f"Moving average window size: {window_size}")
print(f"Filtered signal length: {len(moving_avg)}")

print("\nQ30.4: Create a window function (Hamming)")
print("Answer:")
hamming_window = np.hamming(20)
print(f"Hamming window (first 5 values): {hamming_window[:5]}")

print("\nQ30.5: Apply window function to signal")
print("Answer:")
windowed_signal = sine_wave[:20] * hamming_window
print(f"Windowed signal (first 5 values): {windowed_signal[:5]}")

# ============================================================================
# QUESTION 31: ARRAY OPTIMIZATION AND PERFORMANCE
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 31: ARRAY OPTIMIZATION AND PERFORMANCE")
print("=" * 60)

print("\nQ31.1: Time array operations using time module")
print("Answer:")
import time
large_array = np.random.random(1000000)
start_time = time.time()
result = np.sum(large_array)
end_time = time.time()
print(f"Array size: {len(large_array)}")
print(f"Sum: {result:.6f}")
print(f"Time taken: {(end_time - start_time)*1000:.3f} ms")

print("\nQ31.2: Compare vectorized vs loop operations")
print("Answer:")
small_array = np.random.random(1000)
# Vectorized operation
start_time = time.time()
vectorized_result = np.square(small_array)
vectorized_time = time.time() - start_time

# Loop operation
start_time = time.time()
loop_result = np.array([x**2 for x in small_array])
loop_time = time.time() - start_time

print(f"Vectorized time: {vectorized_time*1000:.3f} ms")
print(f"Loop time: {loop_time*1000:.3f} ms")
print(f"Speedup: {loop_time/vectorized_time:.1f}x")

print("\nQ31.3: Use memory-efficient operations")
print("Answer:")
# In-place operation
arr_inplace = np.array([1, 2, 3, 4, 5])
arr_inplace *= 2
print(f"In-place multiplication: {arr_inplace}")

print("\nQ31.4: Optimize array creation")
print("Answer:")
# Pre-allocate array
preallocated = np.zeros(1000)
for i in range(1000):
    preallocated[i] = i**2
print(f"Pre-allocated array sum: {np.sum(preallocated)}")

print("\nQ31.5: Use efficient array methods")
print("Answer:")
# Use built-in methods instead of Python loops
efficient_sum = large_array.sum()
efficient_mean = large_array.mean()
print(f"Efficient sum: {efficient_sum:.6f}")
print(f"Efficient mean: {efficient_mean:.6f}")

# ============================================================================
# QUESTION 32: ARRAY MASKED ARRAYS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 32: ARRAY MASKED ARRAYS")
print("=" * 60)

print("\nQ32.1: Create a masked array with invalid values")
print("Answer:")
data_with_invalid = np.array([1, 2, -999, 4, 5])
mask = (data_with_invalid == -999)
masked_array = np.ma.masked_array(data_with_invalid, mask=mask)
print(f"Original data: {data_with_invalid}")
print(f"Mask: {mask}")
print(f"Masked array: {masked_array}")

print("\nQ32.2: Calculate statistics on masked array")
print("Answer:")
masked_mean = np.ma.mean(masked_array)
masked_std = np.ma.std(masked_array)
print(f"Masked array mean: {masked_mean}")
print(f"Masked array std: {masked_std}")

print("\nQ32.3: Fill masked values with a specific value")
print("Answer:")
filled_array = masked_array.filled(fill_value=0)
print(f"Filled array: {filled_array}")

print("\nQ32.4: Create masked array from condition")
print("Answer:")
condition_mask = (data_with_invalid < 0)
conditioned_masked = np.ma.masked_array(data_with_invalid, mask=condition_mask)
print(f"Condition mask: {condition_mask}")
print(f"Conditioned masked array: {conditioned_masked}")

print("\nQ32.5: Combine multiple masks")
print("Answer:")
mask1 = (data_with_invalid < 0)
mask2 = (data_with_invalid > 10)
combined_mask = mask1 | mask2
combined_masked = np.ma.masked_array(data_with_invalid, mask=combined_mask)
print(f"Combined mask: {combined_mask}")
print(f"Combined masked array: {combined_masked}")

# ============================================================================
# QUESTION 33: ARRAY STRUCTURED ARRAYS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 33: ARRAY STRUCTURED ARRAYS")
print("=" * 60)

print("\nQ33.1: Create a structured array with named fields")
print("Answer:")
dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]
structured_data = np.array([('Alice', 25, 165.5), ('Bob', 30, 180.0)], dtype=dtype)
print(f"Structured array:\n{structured_data}")

print("\nQ33.2: Access structured array fields")
print("Answer:")
names = structured_data['name']
ages = structured_data['age']
print(f"Names: {names}")
print(f"Ages: {ages}")

print("\nQ33.3: Sort structured array by field")
print("Answer:")
sorted_by_age = np.sort(structured_data, order='age')
print(f"Sorted by age:\n{sorted_by_age}")

print("\nQ33.4: Filter structured array by condition")
print("Answer:")
tall_people = structured_data[structured_data['height'] > 170]
print(f"People taller than 170cm:\n{tall_people}")

print("\nQ33.5: Create structured array from existing arrays")
print("Answer:")
names_array = np.array(['Charlie', 'Diana'])
ages_array = np.array([35, 28])
heights_array = np.array([175.0, 162.0])
new_structured = np.core.records.fromarrays([names_array, ages_array, heights_array], 
                                           names='name,age,height')
print(f"New structured array:\n{new_structured}")

# ============================================================================
# QUESTION 34: ARRAY RECORD ARRAYS
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 34: ARRAY RECORD ARRAYS")
print("=" * 60)

print("\nQ34.1: Create a record array")
print("Answer:")
record_array = np.rec.array([('Eve', 22, 160.0), ('Frank', 45, 175.0)], 
                           dtype=[('name', 'U10'), ('age', 'i4'), ('height', 'f4')])
print(f"Record array:\n{record_array}")

print("\nQ34.2: Access record array attributes")
print("Answer:")
print(f"First person name: {record_array[0].name}")
print(f"First person age: {record_array[0].age}")

print("\nQ34.3: Filter record array by attribute")
print("Answer:")
young_people = record_array[record_array.age < 30]
print(f"Young people:\n{young_people}")

print("\nQ34.4: Sort record array by multiple fields")
print("Answer:")
sorted_records = np.sort(record_array, order=['age', 'height'])
print(f"Sorted by age then height:\n{sorted_records}")

print("\nQ34.5: Convert record array to regular array")
print("Answer:")
regular_array = np.array(record_array.tolist())
print(f"Regular array:\n{regular_array}")

# ============================================================================
# QUESTION 35: ARRAY UNIVERSAL FUNCTIONS (UFUNCS)
# ============================================================================

print("\n" + "=" * 60)
print("QUESTION 35: ARRAY UNIVERSAL FUNCTIONS (UFUNCS)")
print("=" * 60)

print("\nQ35.1: Apply ufunc to array with output parameter")
print("Answer:")
input_array = np.array([1, 2, 3, 4, 5])
output_array = np.zeros_like(input_array)
np.square(input_array, out=output_array)
print(f"Input array: {input_array}")
print(f"Output array: {output_array}")

print("\nQ35.2: Use ufunc with where parameter")
print("Answer:")
condition = input_array > 2
np.square(input_array, out=output_array, where=condition)
print(f"Condition: {condition}")
print(f"Conditional output: {output_array}")

print("\nQ35.3: Apply ufunc with reduce")
print("Answer:")
reduced_sum = np.add.reduce(input_array)
reduced_product = np.multiply.reduce(input_array)
print(f"Reduced sum: {reduced_sum}")
print(f"Reduced product: {reduced_product}")

print("\nQ35.4: Apply ufunc with accumulate")
print("Answer:")
accumulated_sum = np.add.accumulate(input_array)
accumulated_product = np.multiply.accumulate(input_array)
print(f"Accumulated sum: {accumulated_sum}")
print(f"Accumulated product: {accumulated_product}")

print("\nQ35.5: Use ufunc with outer")
print("Answer:")
outer_sum = np.add.outer(input_array, input_array)
print(f"Outer sum:\n{outer_sum}")

# ============================================================================
# SUMMARY AND INSIGHTS
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY AND INSIGHTS")
print("=" * 60)

print("\nKey Statistics Summary:")
print(f"Total Revenue: ${np.sum(retail_data[:, 1] * retail_data[:, 2]):.2f}")
print(f"Average Price: ${np.mean(retail_data[:, 1]):.2f}")
print(f"Total Products Sold: {np.sum(retail_data[:, 2])}")
print(f"Average Customer Rating: {np.mean(retail_data[:, 3]):.2f}")
print(f"Average Days in Stock: {np.mean(retail_data[:, 4]):.1f}")

print("\nTop Performing Products:")
# Sort by revenue (price × quantity)
revenue = retail_data[:, 1] * retail_data[:, 2]
top_products_idx = np.argsort(revenue)[-3:][::-1]
for i, idx in enumerate(top_products_idx):
    product = retail_data[idx]
    revenue_val = product[1] * product[2]
    print(f"{i+1}. Product {product[0]}: ${revenue_val:.2f}")

print("\n" + "=" * 60)
print("ASSIGNMENT COMPLETED!")
print("=" * 60)
