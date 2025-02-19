from collections import defaultdict
import heapq
from typing import List, Optional, Tuple


def make_denominations(denominations,amount):

    denominations.sort(reverse = True)
    list_coin = []
    num_coins = 0

    for coin in denominations:

        if coin <= amount:
            num_coins +=1
            list_coin.append(coin)
            amount -=coin
           

    return list_coin, num_coins

denominations = [25, 16,10, 5, 1]
amount = 41  # Target amount in cents

list_oin, nums_coin = make_denominations(denominations, amount)
print(list_oin)
print(nums_coin)

def maximum_activities(start,end):

    activities = list(zip(start,end))
    activities.sort(key=lambda x:x[1])

    last_end_time = activities[0][1]
    count = 1
    select_activities = [0]

    for i in range(1, len(activities)):

        if activities[i][0] >= last_end_time:
            count+=1

            select_activities.append(i)

            last_end_time = activities[i][1]

    return count, select_activities

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

count, selected_activities = maximum_activities(start,end)
print(f"number of ctivities {count}")
print(f"selected activiies {selected_activities}")


def fractional_knapsack(weights,values,capacity):

    items = zip(values,weights)

    items_with_ratio = [(v/w,w) for v,w in items]

    items_with_ratio.sort(reverse=True)
    total_value = 0.0

    for value_per_weight,weight in items_with_ratio:
        if capacity >= weight:
            total_value += value_per_weight * weight
            capacity -= weight

        else:
            total_value += value_per_weight * capacity
            break
    return total_value

weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50  # Capacity of the knapsack

total_value = fractional_knapsack(weights,values,capacity)

print(total_value)


def dijstra_algorithms(graph, source):

    distances = {i: float('inf') for i in graph}
    distances[source] = 0

    min_heap = [(0,source)]

    while min_heap:
        current_distnce, current_node = heapq.heappop(min_heap)

        if current_distnce > distances[current_node]:
            break

        for neighbor,weight in graph[current_node]:
            dist = current_distnce + weight
            
            if dist < distances[neighbor]:
                distances[neighbor] = dist

                heapq.heappush(min_heap,(dist, neighbor))

    return distances

graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    2: [(1, 8), (3, 7), (8, 2), (5, 4)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(4, 10), (3, 14), (2, 4), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (8, 7), (6, 1)],
    8: [(2, 2), (7, 7), (6, 6)]
}

source = 0

dist = dijstra_algorithms(graph,source)

print(dist)

def job_sequencing(jobs):

    jobs.sort(key=lambda x:x[1], reverse=True)

    max_dealine = max(job[0] for job in jobs)

    total_profit = 0
    slots = [-1] * (max_dealine+1)

    for dealine,profit in jobs:
        for j in range(min(dealine,max_dealine),0, -1):
            if slots[j] == -1:
                slots[j] = profit
                total_profit += profit

                break

    return total_profit


        

jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]

total_pro = job_sequencing(jobs)

print(f"Total profit of job squence {total_pro}")

def reduce_difference(heights,k):
    heights.sort()

    n = len(heights)
    intial_difference = heights[-1] - heights[0]

    min_difference = intial_difference

    for i in range(n - 1):
        new_max = max(heights[-1] -k, heights[i]+k)
        new_min = min(heights[0] + k, heights[i+1]-k)

        min_difference = min(min_difference, (new_max - new_min))

    return min_difference

heights = [1, 5, 15, 10]
k = 3

diff = reduce_difference(heights,k)
print("minimum diffirence",diff)



def max_platforms_needed(arrival,departure):

    arrival = [time.zfill(5) for time in arrival]
    departure = [time.zfill(5) for time in departure]

    arrival.sort()
    departure.sort()

    i,j = 0,0
    platform_needed = 0
    max_platforms = 0
    n = len(arrival)

    while i < n and j < n:
         if arrival[i] < departure[j]:
             platform_needed += 1
             max_platforms = max(max_platforms, platform_needed)
             i += 1
         else:
             platform_needed -= 1
             j += 1
    return max_platforms


arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

max_pla = max_platforms_needed(arrival,departure)

print(max_pla)

def largest_number(nums):

    nums_str = list(map(str,nums))
    nums_str.sort(key=lambda x:x*10, reverse=True)

    results = ''.join(nums_str)

    return results
nums = [3, 30, 34, 5, 9]

res = largest_number(nums)

print(res)

def single_day_max_profit(prices):

    min_prices = float('inf')
    max_profit = 0

    for price in prices:
        min_prices = min(min_prices, price)
        max_profit = max(max_profit, price - min_prices)
        
    return max_profit


prices = [7, 1, 5, 3, 6, 4]

best_profit = single_day_max_profit(prices)
print(best_profit)

def double_profit(prices):
    profit =0

    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit
prices =[7, 1, 5, 3, 6, 4]

pr = double_profit(prices)

print(pr)

## hash questions

def contains_duplicate(example_input):

    return len(example_input) != len(set(example_input))
example_input = [1, 2, 3, 4, 5, 1]
num = contains_duplicate(example_input)
print(num)

def remove_duplicates(example_input):
    return list(set(example_input))

example_input = [1, 2, 3, 4, 5, 1]
unique_numbers = remove_duplicates(example_input)
print(unique_numbers)


def groupanagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:
        sorted_strs = ''.join(sorted(s))
        anagrams[sorted_strs].append(s)
    return list(anagrams.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

ana = groupanagrams(strs)

print(ana)


def isIsomorphic(s,t):

    mapping_s_t = {}
    mapping_t_s = {}

    for c1,c2 in zip(s,t):

        if c1 not in mapping_s_t and c2 not in mapping_t_s:
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1

        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
    return True

s = "two"
t = "get"

tands = isIsomorphic(s,t)
print(tands)


def word_pattern(pattern,s):

    words = s.split()

    if len(pattern) != len(words):
        return False
    
    mapping_char_word = {}
    mapping_word_char = {}

    for cha, word in zip(pattern, words):

        if cha not in mapping_char_word and word not in mapping_word_char:
            mapping_char_word[cha] = word
            mapping_word_char[word] = cha
        elif mapping_char_word.get(cha) != word or mapping_word_char.get(word) != cha:
            return False
    return True
pattern = "abba"
s = "dog cat cat dog"

ans = word_pattern(pattern, s)

print(ans)
from collections import Counter
def construct_ransmNote(ransomNote,magazine):

    ransomnote_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    for char, count in ransomnote_count.items():

        if magazine_count[char] < count:
            return False
        
    return True
ransomNote = "aa"
magazine = "aab"

sol = construct_ransmNote(ransomNote, magazine)
print(f"Can construct '{ransomNote}' from '{magazine}'? {sol}")

def findthedifference(s,t):

    result = 0

    for c in s+t:
        result ^= ord(c)
    return chr(result)
s = "abcd"
t = "abcde"

extra = findthedifference(s,t)
print(extra)

from typing import List

def majority_element(nums):
    counts = Counter(nums)

    return max(counts,key=counts.get)
nums = [2, 2, 1, 1, 1, 2, 2]

n = majority_element(nums)
print(n)


def topkfrequentnum(nums, k):

    count = Counter(nums)

    return [item for item, freq in count.most_common(k)]

nums = [1,1,1,2,2,3,3,3,3]
k = 2

topk = topkfrequentnum(nums,k)
print(topk)

def twosum(numbers,target):

    left,right = 0, len(numbers) -1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left +1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

numbers = [2, 7, 11, 15]  # A sorted list of numbers.
target = 9

indicess =  twosum(numbers, target)

print (indicess)

def reverse_string(s):
    
    left, right = 0, len(s)-1

    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1

    return s
    
s = ["h", "e", "l", "l", "o"] 

tt = reverse_string(s)
print(tt)


def ispalindrome(s):
    left, right = 0, len(s)-1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -=1

        if s[left].lower() != s[right].lower():
            return False
        else:
            left +=1
            right -= 1
    return True
s = "A man, a plan, a canal: Panama"

palindrome = ispalindrome(s)
print(palindrome)

def maxArea(height):
    left,right = 0, len(height) -1

    max_area = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])

        max_area = max(max_area, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

area = maxArea(height)

print(area)


def trap_water(height):

    if  not height:
        return 0
    
    left, right = 0, len(height)-1

    left_max, right_max = height[left], height[right]

    water_trap = 0

    while left < right:
     if left_max < right_max:
         left += 1
         left_max = max(left_max, height[left])
         water_trap += left_max - height[left]

     else:
         right -= 1
         right_max = max(right_max, height[right])
         water_trap += right_max - height[right]
    return water_trap

height = [0,1,0,2,1,0,1,3,2,1,2,1]

trappedwater = trap_water(height)
print(trappedwater)

def sub_array_sum(arr,i,j):

    prefix_sum = [0]* len(arr)
    prefix_sum[0] = arr[0]

    for k in range(1, len(arr)):
        prefix_sum[k] = prefix_sum[k - 1] + arr[k]

    if i == 0:
        return prefix_sum[j]
    else:
        return prefix_sum[j] - prefix_sum[i-1]
arr = [2, 4, 1, 6, 3]
i, j = 1, 3

prefixsum = sub_array_sum(arr,i,j)
print(f"The total Prfix form {i} to {j}: {prefixsum}")

def sub_array_with_queries(arr,queries,n,m):

    prefix_sums = [0]* len(arrs)
    prefix_sums[0] = arrs[0]

    for k in range(1, len(arrs)):
        prefix_sums[k] = prefix_sums[k -1] + arr[k]

    if n == 0:
        return prefix_sums[m]
    else:
        return prefix_sums[m]-prefix_sums[n-1]
arrs = [3, 5, 2, 8, 6]
queries = [(1, 3), (0, 4), (2, 4)]

for n, m in queries:
    prexis = sub_array_with_queries(arr,queries,n,m)

    print(f" sum of sub array from {n} to {m}: {prexis}")

def sub_array_of_k(nums,k):

    current_sum = 0
    max_sum = 0

    for i in range(k):
        current_sum += nums[i]
    max_sum = current_sum

    for i in range(k, len(nums)):

        current_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum,current_sum)

    return max_sum


nums = [2, 1, 5, 1, 3, 2]
k = 3

sub_k = sub_array_of_k(nums,k)
print(f"the Maximum sub of array {k} is {sub_k}")




class Solution:
    def subarraySum(nums,target):

        current_sum = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left +=1

            if current_sum == target:
                # return nums[left:right+1]
                return nums[left:right + 1] 
        return []
nums = [1, 2, 3, 4, 5]
target = 9

subsub = Solution.subarraySum(nums,target)

print(subsub)


def maximu_request_in_k(requests,k):

    maximum_request = 0
    sum_windo = 0
    left =0

    for right in range(len(requests)):
        sum_windo += requests[right]

        if right >= k - 1:
             maximum_request = max(maximum_request, sum_windo)
             sum_windo -= requests[left]
             left +=1
    return maximum_request
    
requests = [10, 3, 15, 8, 25, 18, 12, 20]  # Number of requests per second
K = 3  # Window size in seconds

mmm_request = maximu_request_in_k(requests, k)

print(mmm_request)

def more_power_usage(power,s):

    sum_window = 0
    max_power_usage = 0
    left = 0

    for right in range(len(power)):
        sum_window+=power[right]

        if right >= s - 1:
            max_power_usage = max(max_power_usage, sum_window)
            sum_window -= power[left]
            left += 1
    return max_power_usage
power = [100, 200, 150, 300, 250, 400, 350, 500]
s = 4

usages = more_power_usage(power, s)
print(usages)

def suspesious_transactions(transactions,t,threshold):

    max_transaction = 0
    normal_transactions = 0
    left = 0

    for right in range(len(transactions)):
        normal_transactions += transactions[right]

        if right > t -1:

            if normal_transactions > threshold:
                print("fraud detected on  the following window")
                return  (transactions[left:right +1])

            normal_transactions -= transactions[left]
            max_transaction = max(max_transaction, normal_transactions)
            left += 1

    return "No Fraud detected"


transactions = [1000, 2000, 1500, 500, 120000, 3000, 700]  # Daily transaction amounts
t = 3  # Window size (number of consecutive days to check)
threshold = 5000  # Fraud detection threshold

fraud = suspesious_transactions(transactions,t,threshold)

print (fraud)


def longest_review(reviews,r):

    max_review = 0
    current_review = 0
    left = 0

    for right in range(len(reviews)):
        current_review += reviews[right]

        if right >= r -1:
            current_review -= reviews[left]
            left +=1
            max_review = max(max_review, current_review)
    return max_review
reviews = [1, 1, 0, 1, 1, 1, 0, 1, 1]  # 1 represents a good review, 0 represents a bad review
r = 4 
 
rev = longest_review(reviews, r)

print(rev)


def make_denominations(denomination,amounts):

    denomination.sort(reverse=True)
    num_coins = 0
    coins_name = []

    for coin in denomination:
        if coin <= amounts:
            num_coins +=1
            coins_name.append(coin)
            amounts -= coin
    return num_coins, coins_name


denomination = [25,10, 5, 1,16]
amounts = 41  # Target amount in cents

n,c = make_denominations(denomination,amounts)

print(f"the number of coins: {n}")
print (f"the coins : {c}")