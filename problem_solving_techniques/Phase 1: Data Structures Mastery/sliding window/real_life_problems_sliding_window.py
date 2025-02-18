"""
1. Detect High Traffic in a Website (Max Requests in a Time Window)
Problem Statement:
A website receives a large number of requests per second. Given a list where each element represents the number of requests received
at a particular second, find the maximum number of requests received in any K-second window.

Example Input:
requests = [10, 3, 15, 8, 25, 18, 12, 20]
K = 3
Example Output:
Maximum requests in a 3-second window: 55
"""

def max_requests_in_window(requests, K):
    """
    This function finds the maximum number of requests received in any K-second window.

    :param requests: List of integers where each element represents the number of requests received in a second.
    :param K: Integer representing the size of the time window (in seconds).
    :return: Maximum number of requests received within any K-second window.
    """

    max_requests = 0  # Stores the maximum requests found in any K-second window
    window_sum = 0  # Stores the sum of requests in the current window
    left = 0  # Left boundary of the sliding window

    # Iterate over each second (right boundary of the sliding window)
    for right in range(len(requests)):
        window_sum += requests[right]  # Add current second's requests to the window sum

        # Ensure the window size reaches exactly K before calculating max
        if right >= K - 1:
            max_requests = max(max_requests, window_sum)  # Update max requests if this window has more
            
            # Slide the window: remove the oldest request from the sum
            window_sum -= requests[left]
            left += 1  # Move the left boundary forward

    return max_requests  # Return the maximum found within any K-second window


# Example Usage
requests = [10, 3, 15, 8, 25, 18, 12, 20]  # Number of requests per second
K = 3  # Window size in seconds

# Output the maximum number of requests seen in any 3-second window
print("Maximum requests in a 3-second window:", max_requests_in_window(requests, K))

# Time Complexity: O(N)
# Space Complexity: O(1)

"""
2. Identify Peak Demand Period in an Electricity Grid
Problem Statement:
An electricity grid logs power consumption every hour. Given an array representing hourly consumption, 
find the hourly window of size K that had the highest power usage.

Example Input:
power_usage = [100, 200, 150, 300, 250, 400, 350, 500]
K = 4
Example Output:
Maximum power usage in a 4-hour window: 1500
"""
def max_power_usage(power_usage, K):
    """
    This function finds the maximum power usage recorded within any K-hour window.

    :param power_usage: List of integers where each element represents power usage in an hour.
    :param K: Integer representing the size of the time window (in hours).
    :return: Maximum power usage recorded within any K-hour window.
    """

    max_usage = 0  # Stores the maximum power usage found in any K-hour window
    window_usage = 0  # Stores the sum of power usage in the current sliding window
    left = 0  # Left boundary of the sliding window

    # Iterate over each hour (right boundary of the sliding window)
    for right in range(len(power_usage)):
        window_usage += power_usage[right]  # Add current hour's power usage to the window sum

        # Ensure the window size reaches exactly K before calculating max
        if right >= K - 1:
            max_usage = max(max_usage, window_usage)  # Update max usage if this window has more
            
            # Slide the window: remove the oldest hour's power usage from the sum
            window_usage -= power_usage[left]
            left += 1  # Move the left boundary forward

    return max_usage  # Return the maximum found within any K-hour window


# Example Usage
power_usage = [100, 200, 150, 300, 250, 400, 350, 500]  # Power usage in different hours
K = 4  # Window size in hours

# Output the maximum power usage recorded in any 4-hour window
print("Maximum power usage in a 4-hour window:", max_power_usage(power_usage, K))

# Time Complexity: O(N)
# Space Complexity: O(1)

"""
3. Detect Suspicious Financial Transactions
Problem Statement:
A bank monitors transactions per day. If the total transaction amount in any K-day window exceeds a given 
fraud threshold, the system raises an alert.

Example Input:
transactions = [1000, 2000, 1500, 500, 1200, 3000, 700]
K = 3
threshold = 5000
Example Output:
Fraud detected in a 3-day window!
"""
def detect_fraud(transactions, K, threshold):
    """
    Detects fraud in a series of daily transactions by checking if 
    the sum of transactions in any K-day window exceeds a given threshold.

    :param transactions: List of integers where each element represents the transaction amount for a day.
    :param K: Integer representing the size of the sliding window (number of days).
    :param threshold: Integer representing the fraud threshold.
    :return: A string indicating whether fraud was detected or not.
    """

    window_sum = 0  # Tracks the sum of transactions in the current K-day window
    left = 0  # Left boundary of the sliding window

    # Iterate through each day's transaction (right boundary of the window)
    for right in range(len(transactions)):
        window_sum += transactions[right]  # Add the current day's transaction to the window sum

        # When the window reaches the required size (K days)
        if right >= K - 1:  
            # Check if the sum of transactions in the current window exceeds the fraud threshold
            if window_sum > threshold:
                print("Fraud detected in the following {}-day window:".format(K))
                print(transactions[left:right+1])  # Print the transactions in the window where fraud was detected
                return "Fraud detected in a {}-day window!".format(K)

            # Remove the oldest transaction from the window before sliding forward
            window_sum -= transactions[left]
            left += 1  # Move the left boundary of the window

    return "No fraud detected"  # If no fraud case is found, return this message


# Example Usage
transactions = [1000, 2000, 1500, 500, 120000, 3000, 700]  # Daily transaction amounts
K = 3  # Window size (number of consecutive days to check)
threshold = 5000  # Fraud detection threshold

# Output whether fraud was detected
print(detect_fraud(transactions, K, threshold))

# Time Complexity: O(N)
# Space Complexity: O(1)

"""
Problem Statement: Detect Suspicious Financial Transactions
A bank monitors daily transactions to detect suspicious activity. If the total transaction amount in any K-day window falls within 
a suspicious range (between a minimum and maximum threshold), the system raises an alert.

Your task: Write a function that detects whether any K-day window has a total transaction sum within the given suspicious range.

Input:
transactions = [1000, 2000, 1500, 500, 1200, 3000, 700]
K = 3
min_threshold = 4000
max_threshold = 6000

Output:
"Suspicious transactions detected in a 3-day window!"

Input:

transactions = [800, 1500, 1200, 700, 900, 1100]
K = 2
min_threshold = 3000
max_threshold = 500

OutPut
"No suspicious activity detected"

"""

def detect_suspicious_transactions(transactions, K, min_threshold, max_threshold):
    """
    Detects suspicious transactions in any K-day window where:
    - The total transaction amount exceeds max_threshold.
    - The total transaction amount is at least min_threshold.

    :param transactions: List of integers representing daily transactions.
    :param K: Integer representing the sliding window size (days).
    :param min_threshold: Minimum required transaction amount for fraud detection.
    :param max_threshold: Maximum allowed transaction amount before an alert is triggered.
    :return: A string indicating if fraud is detected.
    """

    window_sum = 0  # Track the sum of transactions in the current K-day window
    left = 0  # Left boundary of the sliding window

    for right in range(len(transactions)):
        window_sum += transactions[right]  # Add the current day's transaction

        # Ensure window has exactly K days before checking thresholds
        if right >= K - 1:  
            # Check if the transaction sum is within the fraud range
            if min_threshold <= window_sum <= max_threshold:
                return f"Suspicious transactions detected in a {K}-day window!"
            
            # Slide the window by removing the oldest transaction
            window_sum -= transactions[left]
            left += 1  # Move the left boundary

    return "No suspicious activity detected"

# Example Usage
transactions = [1000, 2000, 1500, 500, 1200, 3000, 700]
K = 3  # Window size in days
min_threshold = 4000  # Minimum suspicious transaction amount
max_threshold = 6000  # Maximum allowed transaction amount

# Output fraud detection result
print(detect_suspicious_transactions(transactions, K, min_threshold, max_threshold))



"""
4. Count Continuous Good Reviews for a Product
Problem Statement:
A company tracks daily customer reviews (1 = good, 0 = bad). Find the longest continuous streak of good reviews within any K-day window.

Example Input:
reviews = [1, 1, 0, 1, 1, 1, 0, 1, 1]
K = 4
Example Output:
Longest streak of good reviews in a 4-day window: 3"""
def longest_good_reviews(reviews, K):
    """
    Finds the maximum number of good reviews (represented by 1s) 
    in any K-day sliding window.

    :param reviews: List of integers where 1 represents a good review and 0 represents a bad review.
    :param K: Integer representing the size of the sliding window (number of days).
    :return: Maximum count of good reviews in any K-day window.
    """

    max_good = 0  # Stores the maximum count of good reviews in any K-day window
    window_good = 0  # Tracks the count of good reviews in the current window
    left = 0  # Left boundary of the sliding window

    # Iterate through the reviews list, treating each day as the right boundary of the window
    for right in range(len(reviews)):
        # If the current day's review is good (1), increase the count in the window
        if reviews[right] == 1:
            window_good += 1

        # Once the window reaches size K
        if right >= K - 1:
            # Update the maximum number of good reviews found in any window
            max_good = max(max_good, window_good)

            # Before sliding the window, check if the outgoing element was a good review
            if reviews[left] == 1:
                window_good -= 1  # Reduce the count if we're removing a good review

            # Move the left boundary of the window forward
            left += 1

    return max_good  # Return the maximum good reviews found in any K-day window


# Example Usage
reviews = [1, 1, 0, 1, 1, 1, 0, 1, 1]  # 1 represents a good review, 0 represents a bad review
K = 4  # Window size (number of days to check)

# Output the maximum number of good reviews in any 4-day window
print("Longest streak of good reviews in a 4-day window:", longest_good_reviews(reviews, K))

# Time Complexity: O(N)
# Space Complexity: O(1)
"""
5. Find the Maximum Number of Customers in a Store Within a Time Window
Problem Statement:
A store records the number of customers entering every minute. Given an array representing the number of customers 
per minute and a time window K (in minutes), find the maximum number of customers present in any K-minute window.

Example Input:
customers = [5, 3, 8, 10, 2, 4, 1, 6, 7]
K = 3
Example Output:
Maximum customers in a 3-minute window: 21
"""
def max_customers(customers, K):
    """
    Finds the maximum number of customers present in any K-minute sliding window.

    :param customers: List of integers where each element represents the number of customers 
                      arriving in that particular minute.
    :param K: Integer representing the size of the sliding window (number of minutes).
    :return: Maximum number of customers in any K-minute window.
    """

    max_count = 0  # Stores the maximum number of customers seen in any K-minute window
    window_sum = 0  # Stores the sum of customers in the current sliding window
    left = 0  # Marks the left boundary of the sliding window

    # Iterate through each minute in the customers list
    for right in range(len(customers)):
        window_sum += customers[right]  # Add the current minute's customer count to the window

        # When the window reaches the required size K
        if right >= K - 1:
            # Update max_count to store the highest number of customers in any K-minute window
            max_count = max(max_count, window_sum)

            # Remove the outgoing element (customer count from the left of the window)
            window_sum -= customers[left]

            # Move the left boundary of the window forward
            left += 1  

    return max_count  # Return the maximum number of customers found in any K-minute window


# Example Usage
customers = [5, 3, 8, 10, 2, 4, 1, 6, 7]  # Customer count per minute
K = 3  # Window size (3-minute window)

# Output the maximum number of customers in any 3-minute window
print("Maximum customers in a 3-minute window:", max_customers(customers, K))

# Time Complexity: O(N)
# Space Complexity: O(1)
"""
6. Find the Longest Period of Stable Internet Speed
Problem Statement:
A company monitors internet speed every second. Given an array where each element represents internet speed (in Mbps), 
find the longest contiguous period where the speed fluctuation does not exceed K Mbps.

Example Input:
speeds = [20, 21, 19, 23, 22, 25, 26, 27, 28, 24, 22]
K = 5
Example Output:
Longest stable internet speed period: 7
"""
def longest_stable_speed(speeds, K):
    left = 0
    max_length = 0

    for right in range(len(speeds)):
        while max(speeds[left:right+1]) - min(speeds[left:right+1]) > K:
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example Usage
speeds = [20, 21, 19, 23, 22, 25, 26, 27, 28, 24, 22]
K = 5
print("Longest stable internet speed period:", longest_stable_speed(speeds, K))
# Time Complexity: O(N)
# Space Complexity: O(1)

"""
7. Find the Minimum Time Required to Read a Book
Problem Statement:
A student is reading a book and keeps track of the number of pages read per hour. Given an array where each element represents 
pages read per hour, find the minimum time required to read at least T pages.

Example Input:
pages_per_hour = [10, 20, 30, 40, 50, 60]
T = 100
Example Output:
Minimum time to read at least 100 pages: 3
"""
def min_reading_time(pages_per_hour, T):
    """
    Finds the minimum number of hours required to read at least T pages, given a list
    of pages read per hour.

    :param pages_per_hour: List of integers representing the number of pages read per hour.
    :param T: Integer representing the target number of pages to be read.
    :return: Minimum number of hours to read at least T pages, or 0 if not possible.
    """
    min_hours = float('inf')  # Initialize the minimum hours as infinity (no valid window found yet)
    left = 0  # Marks the left boundary of the sliding window
    window_sum = 0  # Sum of pages read in the current window

    # Iterate through the list of pages read per hour
    for right in range(len(pages_per_hour)):
        window_sum += pages_per_hour[right]  # Add the pages read in the current hour to the window sum

        # While the sum of pages in the window is greater than or equal to the target (T)
        while window_sum >= T:
            # Update the minimum hours required to read at least T pages
            min_hours = min(min_hours, right - left + 1)

            # Slide the window to the right by removing the pages at the left
            window_sum -= pages_per_hour[left]
            left += 1  # Move the left boundary of the window

    # If we found a valid window, return the minimum hours; otherwise, return 0 (no valid window)
    return min_hours if min_hours != float('inf') else 0

# Example Usage
pages_per_hour = [10, 20, 30, 40, 50, 60]  # Pages read per hour
T = 100  # Target pages to read

# Output the minimum time (in hours) to read at least 100 pages
print("Minimum time to read at least 100 pages:", min_reading_time(pages_per_hour, T))

# Time Complexity: O(N)
# Space Complexity: O(1)

"""
8. Find the Most Popular Product in an Online Store (Mode in a Sliding Window)
Problem Statement:
An online store records product IDs of items sold every second. Given a list of product IDs, 
find the most frequently sold product in any K-second window.

Example Input:
products = [1, 2, 2, 3, 3, 3, 4, 5, 2, 3]
K = 4
Example Output:
Most popular product in a 4-second window: 3
from collections import Counter
"""
from collections import Counter

def most_popular_product(products, K):
    """
    Finds the most popular product within a sliding window of size K.

    :param products: List of product IDs (can be any hashable data type).
    :param K: Integer representing the size of the sliding window.
    :return: The most popular product in the current window, or None if no products are present.
    """
    freq = Counter()  # Counter to keep track of product frequencies in the current window
    left = 0  # Left boundary of the sliding window
    max_product = None  # Variable to store the most popular product

    # Iterate through the products list
    for right in range(len(products)):
        # Add the current product to the frequency counter
        freq[products[right]] += 1

        # Once the window reaches size K, we need to evaluate the most popular product
        if right >= K - 1:
            # Get the product with the maximum frequency in the current window
            max_product = max(freq, key=freq.get)

            # Slide the window by removing the product at the left
            freq[products[left]] -= 1  # Decrease frequency of the product at the left of the window

            # If the product at the left is no longer in the window, remove it from the counter
            if freq[products[left]] == 0:
                del freq[products[left]]

            # Move the left of the window to the right (slide window)
            left += 1

    return max_product  # Return the most popular product in the final window

# Example Usage
products = [1, 2, 2, 3, 3, 3, 4, 5, 2, 3]
K = 4
print("Most popular product in a 4-second window:", most_popular_product(products, K))


# Time Complexity: O(N)
# Space Complexity: O(K)
"""
9. Find the Longest Stretch of Working Hours Without a Break
Problem Statement:
A company monitors employees’ working hours. Given an array where 1 represents work and 0 represents a break, 
find the longest contiguous stretch of working hours that allows up to K breaks.

Example Input:
work_hours = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
K = 1
Longest work stretch with at most 1 break: 6
"""
def longest_work_stretch(work_hours, K):
    """
    Finds the longest stretch of work hours with at most K breaks (0 hours) in a sliding window.

    :param work_hours: List of work hours where 1 represents work and 0 represents a break.
    :param K: Integer representing the maximum number of breaks allowed in the stretch.
    :return: The length of the longest stretch of work hours with at most K breaks.
    """
    left = 0  # Left boundary of the sliding window
    max_length = 0  # To store the maximum stretch length of work hours
    breaks = 0  # To keep track of the number of breaks in the current window

    # Iterate through the work_hours list
    for right in range(len(work_hours)):
        # If the current hour is a break (0), increment the break count
        if work_hours[right] == 0:
            breaks += 1

        # If the number of breaks exceeds the allowed limit K, shrink the window from the left
        while breaks > K:
            # If the hour at the left of the window is a break (0), decrement the break count
            if work_hours[left] == 0:
                breaks -= 1
            # Move the left of the window to the right (slide window)
            left += 1

        # Update the maximum length of the work stretch by calculating the window size
        max_length = max(max_length, right - left + 1)

    return max_length  # Return the longest stretch found

# Example Usage
work_hours = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
K = 1
print("Longest work stretch with at most 1 break:", longest_work_stretch(work_hours, K))

# Time Complexity: O(N)
# Space Complexity: O(1)


"""
10. Detect Anomalous Temperature Fluctuations
Problem Statement:
A weather monitoring station records temperature every minute. Given a list of temperatures, 
determine the smallest window size where the difference between the maximum and minimum temperature exceeds a given threshold T.

Example Input:
temperatures = [30, 32, 35, 40, 50, 55, 60, 30, 40]
T = 20
Example Output:
Smallest window with temperature difference > 20: 3
"""

from collections import deque

def smallest_window_temp_difference(temps, T):
    """
    This function finds the smallest window where the temperature difference 
    exceeds the given threshold T.

    :param temps: List of integers where each element represents the temperature at a time.
    :param T: Integer representing the temperature difference threshold.
    :return: Size of the smallest window where the max-min temperature exceeds T, or -1 if none exists.
    """

    # Deques to maintain max and min temperatures within the window
    min_deque, max_deque = deque(), deque()

    left = 0  # Left boundary of the sliding window
    min_window = float('inf')  # Store the minimum window size found

    # Iterate over each temperature reading (right boundary of the sliding window)
    for right in range(len(temps)):

        # Maintain decreasing order in max_deque (stores max values)
        while max_deque and temps[max_deque[-1]] < temps[right]:
            max_deque.pop()  # Remove elements that are smaller than the current value
        max_deque.append(right)  # Add current index

        # Maintain increasing order in min_deque (stores min values)
        while min_deque and temps[min_deque[-1]] > temps[right]:
            min_deque.pop()  # Remove elements that are greater than the current value
        min_deque.append(right)  # Add current index

        # Shrink the window from the left until the max-min difference is <= T
        while temps[max_deque[0]] - temps[min_deque[0]] > T:
            min_window = min(min_window, right - left + 1)  # Update minimum window size
            
            left += 1  # Move left boundary forward

            # Remove elements that are out of the new window
            if min_deque[0] < left:
                min_deque.popleft()
            if max_deque[0] < left:
                max_deque.popleft()

    # If no valid window was found, return -1
    return min_window if min_window != float('inf') else -1


# Example Usage
temperatures = [30, 32, 35, 40, 50, 55, 60, 30, 40]  # Temperature readings
T = 20  # Threshold difference

# Output the smallest window size where temperature difference exceeds 20
print("Smallest window with temperature difference > 20:", smallest_window_temp_difference(temperatures, T))

# Time Complexity: O(N)
# Space Complexity: O(K)
