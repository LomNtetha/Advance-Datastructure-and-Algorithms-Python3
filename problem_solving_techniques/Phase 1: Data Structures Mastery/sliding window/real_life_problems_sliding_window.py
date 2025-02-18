"""
1. Detect High Traffic in a Website (Max Requests in a Time Window)
Problem Statement:
A website receives a large number of requests per second. Given a list where each element represents the number of requests received
at a particular second, find the maximum number of requests received in any K-second window.

Example Input:
requests = [10, 3, 15, 8, 25, 18, 12, 20]
K = 3
Example Output:
Maximum requests in a 3-second window: 51
"""

def max_requests_in_window(requests, K):
    max_requests = 0
    window_sum = 0
    start = 0

    for end in range(len(requests)):
        window_sum += requests[end]  # Add next second's requests
        
        if end >= K - 1:  # Once window reaches size K
            max_requests = max(max_requests, window_sum)
            window_sum -= requests[start]  # Remove oldest second's requests
            start += 1  # Move window

    return max_requests

# Example Usage
requests = [10, 3, 15, 8, 25, 18, 12, 20]
K = 3
print("Maximum requests in a 3-second window:", max_requests_in_window(requests, K))
# Time Complexity: O(N)
# Space Complexity: O(1)

"""
2. Identify Peak Demand Period in an Electricity Grid
Problem Statement:
An electricity grid logs power consumption every hour. Given an array representing hourly consumption, find the hourly window of size K that had the highest power usage.

Example Input:
power_usage = [100, 200, 150, 300, 250, 400, 350, 500]
K = 4
Example Output:
Maximum power usage in a 4-hour window: 1400
"""
def max_power_usage(power_usage, K):
    max_usage = 0
    window_usage = 0
    start = 0

    for end in range(len(power_usage)):
        window_usage += power_usage[end]

        if end >= K - 1:  # Window size reaches K
            max_usage = max(max_usage, window_usage)
            window_usage -= power_usage[start]
            start += 1  # Move window

    return max_usage

# Example Usage
power_usage = [100, 200, 150, 300, 250, 400, 350, 500]
K = 4
print("Maximum power usage in a 4-hour window:", max_power_usage(power_usage, K))
# Time Complexity: O(N)
# Space Complexity: O(1)
"""
3. Detect Anomalous Temperature Fluctuations
Problem Statement:
A weather monitoring station records temperature every minute. Given a list of temperatures, determine the smallest window size where the difference between the maximum and minimum temperature exceeds a given threshold T.

Example Input:
temperatures = [30, 32, 35, 40, 50, 55, 60, 30, 40]
T = 20
Example Output:
Smallest window with temperature difference > 20: 3
"""

from collections import deque

def smallest_window_temp_difference(temps, T):
    min_deque, max_deque = deque(), deque()
    start = 0
    min_window = float('inf')

    for end in range(len(temps)):
        # Maintain decreasing order for max values
        while max_deque and temps[max_deque[-1]] < temps[end]:
            max_deque.pop()
        max_deque.append(end)

        # Maintain increasing order for min values
        while min_deque and temps[min_deque[-1]] > temps[end]:
            min_deque.pop()
        min_deque.append(end)

        # Check if the temperature difference exceeds threshold
        while temps[max_deque[0]] - temps[min_deque[0]] > T:
            min_window = min(min_window, end - start + 1)
            start += 1
            if min_deque[0] < start:
                min_deque.popleft()
            if max_deque[0] < start:
                max_deque.popleft()

    return min_window if min_window != float('inf') else -1

# Example Usage
temperatures = [30, 32, 35, 40, 50, 55, 60, 30, 40]
T = 20
print("Smallest window with temperature difference > 20:", smallest_window_temp_difference(temperatures, T))
# Time Complexity: O(N)
# Space Complexity: O(K)

"""
4. Detect Suspicious Financial Transactions
Problem Statement:
A bank monitors transactions per day. If the total transaction amount in any K-day window exceeds a given fraud threshold, the system raises an alert.

Example Input:
transactions = [1000, 2000, 1500, 500, 1200, 3000, 700]
K = 3
threshold = 5000
Example Output:
Fraud detected in a 3-day window!
"""
def detect_fraud(transactions, K, threshold):
    window_sum = 0
    start = 0

    for end in range(len(transactions)):
        window_sum += transactions[end]

        if end >= K - 1:  # Check fraud condition
            if window_sum > threshold:
                return "Fraud detected in a {}-day window!".format(K)
            window_sum -= transactions[start]
            start += 1

    return "No fraud detected"

# Example Usage
transactions = [1000, 2000, 1500, 500, 1200, 3000, 700]
K = 3
threshold = 5000
print(detect_fraud(transactions, K, threshold))
# Time Complexity: O(N)
# Space Complexity: O(1)


"""
5. Count Continuous Good Reviews for a Product
Problem Statement:
A company tracks daily customer reviews (1 = good, 0 = bad). Find the longest continuous streak of good reviews within any K-day window.

Example Input:
reviews = [1, 1, 0, 1, 1, 1, 0, 1, 1]
K = 4
Example Output:
Longest streak of good reviews in a 4-day window: 3"""

def longest_good_reviews(reviews, K):
    max_good = 0
    window_good = 0
    start = 0

    for end in range(len(reviews)):
        if reviews[end] == 1:
            window_good += 1

        if end >= K - 1:  # When window size reaches K
            max_good = max(max_good, window_good)
            if reviews[start] == 1:
                window_good -= 1
            start += 1

    return max_good

# Example Usage
reviews = [1, 1, 0, 1, 1, 1, 0, 1, 1]
K = 4
print("Longest streak of good reviews in a 4-day window:", longest_good_reviews(reviews, K))
# Time Complexity: O(N)
# Space Complexity: O(1)
"""
6. Find the Maximum Number of Customers in a Store Within a Time Window
Problem Statement:
A store records the number of customers entering every minute. Given an array representing the number of customers per minute and a time window K (in minutes), find the maximum number of customers present in any K-minute window.

Example Input:
customers = [5, 3, 8, 10, 2, 4, 1, 6, 7]
K = 3
Example Output:
Maximum customers in a 3-minute window: 21
"""
def max_customers(customers, K):
    max_count = 0
    window_sum = 0
    start = 0

    for end in range(len(customers)):
        window_sum += customers[end]

        if end >= K - 1:
            max_count = max(max_count, window_sum)
            window_sum -= customers[start]
            start += 1

    return max_count

# Example Usage
customers = [5, 3, 8, 10, 2, 4, 1, 6, 7]
K = 3
print("Maximum customers in a 3-minute window:", max_customers(customers, K))
# Time Complexity: O(N)
# Space Complexity: O(1)
"""
7. Find the Longest Period of Stable Internet Speed
Problem Statement:
A company monitors internet speed every second. Given an array where each element represents internet speed (in Mbps), find the longest contiguous period where the speed fluctuation does not exceed K Mbps.

Example Input:
speeds = [20, 21, 19, 23, 22, 25, 26, 27, 28, 24, 22]
K = 5
Example Output:
Longest stable internet speed period: 7
"""
def longest_stable_speed(speeds, K):
    start = 0
    max_length = 0

    for end in range(len(speeds)):
        while max(speeds[start:end+1]) - min(speeds[start:end+1]) > K:
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

# Example Usage
speeds = [20, 21, 19, 23, 22, 25, 26, 27, 28, 24, 22]
K = 5
print("Longest stable internet speed period:", longest_stable_speed(speeds, K))
# Time Complexity: O(N)
# Space Complexity: O(1)

"""
8. Find the Minimum Time Required to Read a Book
Problem Statement:
A student is reading a book and keeps track of the number of pages read per hour. Given an array where each element represents pages read per hour, find the minimum time required to read at least T pages.

Example Input:
pages_per_hour = [10, 20, 30, 40, 50, 60]
T = 100
Example Output:
Minimum time to read at least 100 pages: 3
"""
def min_reading_time(pages_per_hour, T):
    min_hours = float('inf')
    start = 0
    window_sum = 0

    for end in range(len(pages_per_hour)):
        window_sum += pages_per_hour[end]

        while window_sum >= T:
            min_hours = min(min_hours, end - start + 1)
            window_sum -= pages_per_hour[start]
            start += 1

    return min_hours if min_hours != float('inf') else 0

# Example Usage
pages_per_hour = [10, 20, 30, 40, 50, 60]
T = 100
print("Minimum time to read at least 100 pages:", min_reading_time(pages_per_hour, T))
# Time Complexity: O(N)
# Space Complexity: O(1)

"""
9. Find the Most Popular Product in an Online Store (Mode in a Sliding Window)
Problem Statement:
An online store records product IDs of items sold every second. Given a list of product IDs, find the most frequently sold product in any K-second window.

Example Input:
products = [1, 2, 2, 3, 3, 3, 4, 5, 2, 3]
K = 4
Example Output:
Most popular product in a 4-second window: 3
from collections import Counter
"""
def most_popular_product(products, K):
    freq = Counter()
    start = 0
    max_product = None

    for end in range(len(products)):
        freq[products[end]] += 1
        if end >= K - 1:
            max_product = max(freq, key=freq.get)
            freq[products[start]] -= 1
            if freq[products[start]] == 0:
                del freq[products[start]]
            start += 1

    return max_product

# Example Usage
products = [1, 2, 2, 3, 3, 3, 4, 5, 2, 3]
K = 4
print("Most popular product in a 4-second window:", most_popular_product(products, K))

# Time Complexity: O(N)
# Space Complexity: O(K)
"""
10. Find the Longest Stretch of Working Hours Without a Break
Problem Statement:
A company monitors employees’ working hours. Given an array where 1 represents work and 0 represents a break, find the longest contiguous stretch of working hours that allows up to K breaks.

Example Input:
work_hours = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
K = 1
Longest work stretch with at most 1 break: 6
"""
def longest_work_stretch(work_hours, K):
    start = 0
    max_length = 0
    breaks = 0

    for end in range(len(work_hours)):
        if work_hours[end] == 0:
            breaks += 1

        while breaks > K:
            if work_hours[start] == 0:
                breaks -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

# Example Usage
work_hours = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
K = 1
print("Longest work stretch with at most 1 break:", longest_work_stretch(work_hours, K))
# Time Complexity: O(N)
# Space Complexity: O(1)
