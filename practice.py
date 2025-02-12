from collections import defaultdict
import heapq
from typing import List, Tuple


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

