"""
Problem 1: Continuous Temperature Analysis
Problem Statement
A meteorological agency wants to analyze temperature fluctuations over a period of N days. Given a list of daily temperatures, 
they frequently need to determine the average temperature for various ranges of days [L, R].

Constraints:

You are given an integer N (1 ≤ N ≤ 10⁵), representing the number of days.
You are given an array temperatures of size N, where temperatures[i] represents the temperature on the i-th day.
You will receive multiple queries (L, R), and for each query, you need to return the average temperature from day L to R (both inclusive).
You should optimize the solution to efficiently handle multiple queries.
Example
Input
temperatures = [30, 32, 35, 40, 38, 37, 36]
queries = [(1, 3), (2, 5), (0, 6)]
Output
[32.33, 38.75, 35.43]
(Results are rounded to 2 decimal places for clarity.)
"""

def process_temperatures(temperatures, i, j):
    # Initialize prefix sum array
    prefix_sum = [0] * len(temperatures)
    prefix_sum[0] = temperatures[0]

    # Compute prefix sum
    for k in range(1, len(temperatures)):
        prefix_sum[k] = prefix_sum[k - 1] + temperatures[k]

    # Compute the range sum and average
    if i == 0:
        return round(prefix_sum[j] / (j - i + 1), 2)  # Fix: Return average instead of sum
    else:
        return round((prefix_sum[j] - prefix_sum[i - 1]) / (j - i + 1), 2)  

# Temperature data and queries
temperatures = [30, 32, 35, 40, 38, 37, 36]
queries = [(1, 3), (2, 5), (0, 6)]

# Process queries
temp_results = []
for i, j in queries:
    temp_results.append(process_temperatures(temperatures, i, j))

print(temp_results)  # Prints a list of computed values rounded to 2 decimal places
# Preprocessing: O(N)
# Query Execution: O(1) per query
# Total Complexity: O(N + Q), where Q is the number of queries.
# Space Complexity
# O(N) for the prefix sum array.

"""
Problem 2: Website Traffic Analysis
Problem Statement
A website administrator wants to analyze the traffic pattern of their website. Given daily visitor counts, 
the admin wants to find out how many visitors a particular section of the website received between days L and R multiple times.

Constraints:

You are given an integer N (1 ≤ N ≤ 10⁵), representing the number of days.
You are given an array visitors of size N, where visitors[i] represents the number of visitors on the i-th day.
You will receive multiple queries (L, R), and for each query, you need to return the sum of visitors from day L to R.
Example
Input
visitors = [120, 150, 200, 180, 170, 160, 140]
queries = [(0, 3), (2, 5), (1, 6)]
Output
[650, 710, 1000]
"""
def website_visitors(visitors, l, r):
    # Initialize prefix sum array with the same length as visitors
    prefix_sum = [0] * len(visitors)

    # Set the first element of prefix sum to be the first visitor count
    prefix_sum[0] = visitors[0]

    # Compute prefix sum array
    for k in range(1, len(visitors)):
        prefix_sum[k] = prefix_sum[k - 1] + visitors[k]  # Accumulate visitor counts

    # If the range starts from index 0, return the total sum up to index r
    if l == 0:
        return prefix_sum[r]
    else:
        # Otherwise, return the sum of visitors from index l to r
        return prefix_sum[r] - prefix_sum[l - 1]  # Subtract the sum before index l

# List of daily website visitors
visitors = [120, 150, 200, 180, 170, 160, 140]

# List of queries (each tuple represents a range [l, r])
queries = [(0, 3), (2, 5), (1, 6)]

# List to store results of visitor count queries
rest_pref = []

# Process each query and append the result
for l, r in queries:
    rest_pref.append(website_visitors(visitors, l, r))

# Print the results for each query
print(rest_pref)  # Expected Output: [650, 710, 1000]

# Time Complexity
# Preprocessing: O(N)
# Query Execution: O(1) per query
# Total Complexity: O(N + Q)
# Space Complexity
# O(N)

"""Problem 3: Bank Account Transactions
Problem Statement
A bank maintains a record of daily transactions for a customer. Given the transaction history, 
the bank wants to provide an efficient way for customers to check their balance over any date range.

Constraints:

You are given N (1 ≤ N ≤ 10⁵), representing days.
You are given an array transactions of size N, where transactions[i] represents the net balance change on that day.
You will receive multiple queries (L, R), and for each query, return the total balance change over that period.
Example
Input
transactions = [500, -200, 300, -100, 400, -50, -250]
queries = [(1, 3), (0, 5), (2, 6)]
Output
[0, 850, 300]
"""
def preprocess_prefix_sum(arr):
    """ Computes prefix sum for the transactions array. """
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    return prefix_sum

def balance_changes(transactions, queries):
    """ Returns the total balance change for each query range. """
    prefix_sum = preprocess_prefix_sum(transactions)
    result = []
    
    for L, R in queries:
        result.append(prefix_sum[R + 1] - prefix_sum[L])
    
    return result

# Example usage
transactions = [500, -200, 300, -100, 400, -50, -250]
queries = [(1, 3), (0, 5), (2, 6)]
print(balance_changes(transactions, queries))
# Time Complexity
# Preprocessing: O(N)
# Query Execution: O(1) per query
# Total Complexity: O(N + Q)
# Space Complexity
# O(N)