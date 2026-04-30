def longest_substring_length(s):

    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_length = max(max_length, right -left + 1)
    return max_length

s = ("abcabcbb")

print(longest_substring_length(s))

def longest_substring(s):

    seen = set()
    left = 0
    max_lenght = 0
    result = ""

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left +=1 

        seen.add(s[right])

        if right - left + 1 > max_lenght:
            max_lenght = right - left + 1
            result = s[left:right+1]

    return result 

s = "pwwkew"

print(longest_substring(s))

def longest_palindrome(s):

    def expand(left,right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]
    
    result = ""

    for i in range(len(s)):

        odd = expand(i,i)

        even  = expand(i,i+1)

        result = max(result,odd,even,key=len)

    return result

s = "babad"

print(longest_palindrome(s))

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Helper function to expand around a given center
        def expand_around_center(left: int, right: int) -> int:
            # Expand while:
            # 1. We are within bounds
            # 2. Characters on both sides are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1   # move left pointer outward
                right += 1  # move right pointer outward
            
            # After loop ends, pointers go one step too far
            # So actual palindrome length = (right - 1) - (left + 1) + 1
            # Simplified to:
            return right - left - 1  

        max_len = 0  # Store maximum palindrome length found

        # Try every index as the center
        for i in range(len(s)):
            # Case 1: Odd-length palindrome (center at i)
            odd_length = expand_around_center(i, i)

            # Case 2: Even-length palindrome (center between i and i+1)
            even_length = expand_around_center(i, i + 1)

            # Take the maximum of current results
            max_len = max(max_len, odd_length, even_length)

        return max_len


# Example usage
solution = Solution()
print(solution.longestPalindrome("bbbab"))  # Output: 3


def length_longest_palindrome_substring(s):

    def expand_from_center(left,right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
    

    max_len = 0

    for i in range(len(s)):

        odd_len = expand_from_center(i,i)

        even_len = expand_from_center(i,i+1)

        max_len = max(max_len, odd_len,even_len)

    return max_len

s = "babad"

print(length_longest_palindrome_substring(s))


def length_LIS(nums):

    n = len(nums)

    dp = [1] * n

    for i in range(n):
        for j in range(i):

            if nums[i] < nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(length_LIS(nums))

def longset_increaing_subsquence(nums):

    n = len(nums)

    dp = [[num] for num in nums]

    for i in range(n):
        for j in range(i):

            if nums[i] > nums[j] and len(dp[j]) + 1 > len(dp[i]):
                
                dp[i] = dp[j] + [nums[i]]

    return max(dp,key=len)


nums = [10, 9, 2, 5, 3, 7, 101, 18]


print(longset_increaing_subsquence(nums))


def longest_Increasing_substring(nums):

    left = 0
    best_start = 0
    max_len = 0

    for right in range(len(nums)):

        if nums[right] <= nums[right-1]:

            left = right

        curr_len = right - left + 1

        if curr_len > max_len:
            max_len = curr_len
            best_start = left

    return nums[best_start:best_start+max_len]

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(longest_Increasing_substring(nums))

def longest_increasing_substring_length(nums):

    if not nums:
        return 0
    
    left  = 0
    max_len = 1

    for right in range(1,len(nums)):

        if nums[right] <= nums[right - 1]:

            left = right


        curr_len = right - left + 1

        max_len = max(max_len,curr_len)

    return max_len



nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(longest_increasing_substring_length(nums))

from collections import Counter
def longest_k_distincs(s,k):

    left = 0
    max_len = 0
    count = Counter()

    for right in range(len(s)):

        count[s[right]] += 1

        while len(count) > k:
            count[s[left]] -= 1

            if count[s[left]] == 0:
                del count[s[left]]
                
            left += 1
            
        current_len = right - left + 1
            
        max_len = max(max_len, current_len)

    return max_len

s = "eceba"
k = 2

print(longest_k_distincs(s,k))

def get_intent(payload):

    result = []

    for intent in payload["message"]["nlp"]["intents"]:

        result.append((intent["name"], intent["confidence"]))

    return result

   

payload = {
    "message": {
        "nlp": {
            "intents": [
                {"name": "greet", "confidence": 0.98},
                {"name": "help", "confidence": 0.85},
                {"name": "order", "confidence": 0.60},
                {"name": "bye", "confidence": 0.40},
                {"name": "fallback", "confidence": 0.20}
            ]
        }
    }
}

print(get_intent(payload))

def get_all_intents_plain(payload):

    result  = ""

    for intent in payload["message"]["nlp"]["intents"]:

        result += f"{intent["name"]}: {intent["confidence"]}\n"

    return result


payload = {
    "message": {
        "nlp": {
            "intents": [
                {"name": "greet", "confidence": 0.98},
                {"name": "help", "confidence": 0.85},
                {"name": "order", "confidence": 0.60},
                {"name": "bye", "confidence": 0.40},
                {"name": "fallback", "confidence": 0.20}
            ]
        }
    }
}
print(get_all_intents_plain(payload))

def get_all_messages(payload):

    result = []

    messeges = payload["entry"][0]["changes"][0]["value"]["messages"]

    for msg in messeges:
        result.append(msg["text"]["body"])
    return result


payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hello bot"}},
                    {"text": {"body": "How are you?"}},
                    {"text": {"body": "Order pizza"}}
                ]
            }
        }]
    }]
}

print(get_all_messages(payload))

def get_all_messages_plain(payload):

    result = ""

    messages = payload["entry"][0]["changes"][0]["value"]["messages"]

    for msg in messages:

        result += f"{msg["text"]["body"]}\n"

    return result

payload = {
    "entry": [{
        "changes": [{
            "value": {
                "messages": [
                    {"text": {"body": "Hello bot"}},
                    {"text": {"body": "How are you?"}},
                    {"text": {"body": "Order pizza"}}
                ]
            }
        }]
    }]
}

print(get_all_messages_plain(payload))

from collections import Counter

import re

def frequently_words(paragraph):

    result = []

    words = re.findall(r'\b\w+\b', paragraph.lower())

    count = Counter(words)

    max_freq = max(count.values())

    for word,freq in count.items():

        if freq >= max_freq:
            result.append(word)

    return result
paragraph = "Hello world. Hello everyone. World is beautiful."

print(frequently_words(paragraph))

import re
from collections import Counter


def most_popular_words(text):

    result = []

    words = re.findall(r'\b\w+\b', text.lower())

    count = Counter(words)

    for word, freq in count.most_common():

        result.append(word)

    return result

text = "apple banana apple apple orange banana"

print(most_popular_words(text))

import re

from collections import Counter

def most_frequent_letter_and_words(text):

    words = re.findall(r'\b[a-zA-Z]+\b',text.lower())
    count_words = Counter(words)
    top_5_words = count_words.most_common(5)

    letters = [char for char in text.lower() if char.isalpha()]
    count_letters = Counter(letters)
    top_5_letters = count_letters.most_common(5)

    print("Top 5 words")
    for word, freq in top_5_words:
          print(f'{word}:{freq}')
    
    print("\nTop 5 letters")
    for character, freq_ch in top_5_letters:
        print(f'{character}:{freq_ch}')

text = "This is a simple sentence example. This sentence is simple."

print(most_frequent_letter_and_words(text))

from collections import Counter, defaultdict

def group_words_by_idexes(sentences):

    group_word = defaultdict(set)
    
    for i, sentence in enumerate(sentences):

        words = sentence.split()

        for word in words:
            group_word[word].add(i)

    result  = []

    for indexes in group_word.values():
        if len(indexes) > 1:
            result.append(list(indexes))

    return result

sentences = [
  "hello world the world is beautiful",
  "i am tired today hello world",
]

print(group_words_by_idexes(sentences))

from collections import defaultdict

def group_words_by_words(paragraphs):

    map_word = defaultdict(set)

    for i,sentence in enumerate(sentences):

        words = sentence.split()

        for word in words:

            map_word[word].add(i)

    result = []


    for para,indexes in map_word.items():

        if len(indexes) == len(sentences):

            result.append(para)

    return result


paragraphs = [
    "hello world beautiful day",
    "hello everyone in the world",
    "what a beautiful world hello"
]

print(group_words_by_words(paragraphs))

def longest_sentence(sentences):

    max_words = 0

    result = ""

    for sentence in sentences:

        word_count = len(sentence.split())

        if word_count > max_words:
            max_words = word_count
            result = sentence

    return result

sentences = [
    "hello world",
    "this is a leetcode style problem",
    "python"
]

print(longest_sentence(sentences))


def longest_sentence_alphabet(sentences):

    result  = ""

    max_char = 0

    for sentence  in sentences:
        
        count_char = sum(1 for cha in sentence if cha.isalpha())
        

        if count_char > max_char:
            max_char = count_char
            result = sentence

    return result

sentences = [
    "hello world m l p k p pp pp pp",
    "this is a leetcode style problem",
    "python"
]


print(longest_sentence_alphabet(sentences))

def longest_substring_lenghts(s):

    seen  = set()
    left = 0
    max_len = 0

    for right in range(len(s)):

        if s[right] in seen:

            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        current_len = right - left + 1
        max_len = max(max_len,current_len)

    return max_len

s = ("abcabcbb")

print(longest_substring_lenghts(s))

def max_sliding_window(nums, k):

    result = []
    left = 0

    for right in range(len(nums)):

        if right - left + 1 == k:

            max_window = max(nums[left:right+1])
            result.append(max_window)
            left +=  1

    return result
 

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(max_sliding_window(nums,k))

def validate_expression(expressions):

    stack = []

    pairs = {']':'[','}':'{',')':'('}

    for char in expressions:
        if char in pairs.values():
            stack.append(char)

        elif char in pairs:

            if not stack or stack.pop() != pairs[char]:
                return False
            
    return not stack


expressions = "{[()]}"

print(validate_expression(expressions))


def calculate_points(ops):

    stack  = []

    for op in ops:

        if op == "C":
            stack.pop()

        elif op == "D":
            stack.append(2*stack[-1])
        
        elif op == "+":
            stack.append(stack[-1] + stack[-2])

        else:
            stack.append(int(op))

    return sum(stack)


ops = ["5", "2", "C", "D", "+"]

print(calculate_points(ops))

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


s = "egg"
t = "add"

print(isIsomorphic(s,t))

def twoSum(nums,target):

    left,right = 0,len(nums)-1

    current_sum = 0
    result = []

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left+1, right+1]
        

        elif current_sum < target:
            left += 1
        else:
            right -= 1


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums,target))

def isPalindrome(s):

    left,right = 0, len(s) -1


    while left < right:

        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1

        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))


def sub_arry_large_numer(nums,k):

    left = 0
    max_sum = 0
    current_sum = 0
    

    for right in range(len(nums)):

         current_sum += nums[right]
         
         
         if right -left+1 == k:
            
            max_sum = max(max_sum,current_sum)
            

            current_sum -= nums[left]
            left += 1

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3

print(sub_arry_large_numer(nums,k))


def group_messages(messages):

    n = len(messages)

    left = 0
    

    result  = []

    while left < n:

        group = []

        start_time = int(messages[left].split(":")[0])

        right  = left


        while right < n:

            current_time = int(messages[right].split(":")[0])


            if current_time <= start_time + 4:

                group.append(messages[right])

                right += 1

            else:
                break

        result.append(group)

        left = right
    

    return result


messages = [
    "1:Hello",
    "2:Hi",
    "6:How are you?",
    "7:I am fine",
    "11:Thanks",
    "15:Goodbye"
]


print(group_messages(messages))


def prefix_sum_cal(nums,i,j):

    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]

    for k in range(1,len(nums)):

        prefix_sum[k] = prefix_sum[k-1] + nums[k]


    if i == 0:

        return prefix_sum[j]
    
    else:
        return prefix_sum[j] - prefix_sum[i-1]

nums = [2, 4, 1, 6, 3]
i, j = 1, 3

print(prefix_sum_cal(nums,i,j))

def subsets(nums):

    result = []


    def backtrack(start,current):

        result.append(current[:])


        for i in range(start,len(nums)):

            current.append(nums[i])

            backtrack(i+1,current)

            current.pop()

    backtrack(0,[])

    return result


nums = [1, 2, 3]

print(subsets(nums))


def permutation(nums):

    result = []

    def backtrack(path,used):

        if len(path) == len(nums):
            result.append(path[:])
            return
        

        for i in range(len(nums)):

            if used[i]:
                continue

            used[i] = True

            path.append(nums[i])

            backtrack(path,used)

            path.pop()

            used[i] = False

    backtrack([0],[False]*len(nums))

    return result


nums = [1, 2, 3]

print(permutation(nums))

def  combination(candidates,target):

    result = []

    def backtrack(start,current,remaining):

        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        


        for i in range(start,len(candidates)):


            current.append(candidates[i])

            backtrack(i,current, remaining - candidates[i])

            current.pop()

    backtrack(0,[],target)

    return result

    

candidates = [2, 3, 6, 7]
target = 7

print(combination(candidates,target))


def lower_cost_travel_day(days,costs):

    dp = {}
    travel_days = set(days)

    for day in range(1, days[-1]+1):

        if day not in travel_days:

            dp[day] = dp.get(day-1, 1)

        else:
            dp[day] = min(
                dp.get(day-1, 0) + costs[0],
                dp.get(day-7 , 0) + costs[1],
                dp.get(day-30 , 0) + costs[2]
            )

    return dp[days[-1]]

days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

print(lower_cost_travel_day(days,costs))

def ways_climp_stairs(n):
 
 if n <= 2:
     return 2
 
 dp = [0] * (n+1)

 dp[1],dp[2] = 1,2
 
 for i in range(3,n+1):
     
     dp[i] = dp[i-1] + dp[i-2]

 return dp[i]


n = 5

print(ways_climp_stairs(n))

def max_rob(houses):

    prev=curr = 0

    for house in houses:

        prev,curr = curr,max(curr,prev+house)

    return curr


houses = [2, 7, 9, 3, 1]

print(max_rob(houses))



def rob_house_cycle(nums):

    def linear_rob(houses):

        prev = curr = 0

        for house in houses:

            prev,curr = curr,max(curr,prev+house)

        return curr
    
    if len(nums) == 1:
        return nums[0]
    if len(nums)  == 2:
        return max(nums[0],nums[1])
    

    first_exclude = linear_rob(nums[:-1])
    last_exclude = linear_rob(nums[1:])

    return max(first_exclude,last_exclude)

nums = [1,2,3,1]

print(rob_house_cycle(nums))


def minimum_platforms_required(arrival,departure):

    arrival = [time.zfill(5) for time in arrival]

    departure = [time.zfill(5) for time in departure]

    arrival.sort()

    departure.sort()

    i,j = 0,0
    platform_needed = 0
    max_platform = 0

    n = len(arrival)

    while i < n and j < n:

        if arrival[i] < departure[j]:

            platform_needed += 1

            max_platform = max(max_platform,platform_needed)

            i += 1

        else:
            platform_needed -= 1
            j += 1

    return max_platform

    
arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

print(minimum_platforms_required(arrival,departure))

def job_sequencing(jobs):

    jobs.sort(key=lambda x: x[1],reverse=True)

    maxdealine = max(job[0] for job in jobs)

    slots = [-1] * (maxdealine+ 1)

    total_profit = 0


    for dealine, profit in jobs:

        for j in range(min(maxdealine,dealine),0,-1) :

            if slots[j] == -1:
                slots[j] = profit
                total_profit += profit

                break

    return total_profit

jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]

print(job_sequencing(jobs))

