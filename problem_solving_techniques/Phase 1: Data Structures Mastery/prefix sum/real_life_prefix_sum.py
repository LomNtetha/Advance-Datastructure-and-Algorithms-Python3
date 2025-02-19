"""
Problem 1: Continuous Temperature Analysis
Problem Statement
A meteorological agency wants to analyze temperature fluctuations over a period of N days. Given a list of daily temperatures, they frequently need to determine the average temperature for various ranges of days [L, R].

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
def preprocess_prefix_sum(arr):
    """ Computes the prefix sum array for the given array. """
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    return prefix_sum

def average_temperature(temperatures, queries):
    """ Returns the average temperature for each (L, R) range. """
    prefix_sum = preprocess_prefix_sum(temperatures)
    result = []
    
    for L, R in queries:
        total_sum = prefix_sum[R + 1] - prefix_sum[L]
        count = R - L + 1
        result.append(round(total_sum / count, 2))  # Rounding to 2 decimal places
    
    return result

# Example usage
temperatures = [30, 32, 35, 40, 38, 37, 36]
queries = [(1, 3), (2, 5), (0, 6)]
print(average_temperature(temperatures, queries))
# Time Complexity
# Preprocessing: O(N)
# Query Execution: O(1) per query
# Total Complexity: O(N + Q), where Q is the number of queries.
# Space Complexity
# O(N) for the prefix sum array.

"""
Problem 2: Website Traffic Analysis
Problem Statement
A website administrator wants to analyze the traffic pattern of their website. Given daily visitor counts, the admin wants to find out how many visitors a particular section of the website received between days L and R multiple times.

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
def preprocess_prefix_sum(arr):
    """ Computes the prefix sum array for the given visitor counts. """
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    return prefix_sum

def total_visitors(visitors, queries):
    """ Returns the total visitors for each (L, R) range. """
    prefix_sum = preprocess_prefix_sum(visitors)
    result = []
    
    for L, R in queries:
        result.append(prefix_sum[R + 1] - prefix_sum[L])
    
    return result

# Example usage
visitors = [120, 150, 200, 180, 170, 160, 140]
queries = [(0, 3), (2, 5), (1, 6)]
print(total_visitors(visitors, queries))
# Time Complexity
# Preprocessing: O(N)
# Query Execution: O(1) per query
# Total Complexity: O(N + Q)
# Space Complexity
# O(N)

"""Problem 3: Bank Account Transactions
Problem Statement
A bank maintains a record of daily transactions for a customer. Given the transaction history, the bank wants to provide an efficient way for customers to check their balance over any date range.

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