"""2. Count Positive Numbers

Problem: Count positive numbers in an array.

Input:
arr = [-1, 2, 3, -4]

Output:
2"""

def countPositive(arr):
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    return count

print(countPositive([-1, 2, 3, -4]))  # 2

"""3. Count Negative Numbers

Problem: Count negative numbers in an array.

Input:
arr = [-1, 2, -3, 4]

Output:
2
"""
def countNegative(arr):
    count = 0
    for num in arr:
        if num < 0:
            count += 1
    return count

print(countNegative([-1, 2, -3, 4]))  # 2

"""4. Sum of Odd Numbers

Problem: Return the sum of odd numbers in an array.

Input:
arr = [1,2,3,4,5]

Output:
9
"""
def sumOdd(arr):
    total = 0
    for num in arr:
        if num % 2 != 0:
            total += num
    return total

print(sumOdd([1,2,3,4,5]))  # 9

"""5. Reverse String

Problem: Return a reversed version of a string.

Input:
s = "hello"

Output:
"olleh"
"""
def reverseString(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result

print(reverseString("hello"))  # olleh

"""6. Count Character Occurrences

Problem: Count how many times a character appears in a string.

Input:
s = "hello", ch = "l"

Output:
2
"""
def countChar(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count

print(countChar("hello", "l"))  # 2

"""7. Sum of Squares

Problem: Return the sum of squares of numbers in an array.

Input:
arr = [1,2,3]

Output:
14
"""
def sumSquares(arr):
    total = 0
    for num in arr:
        total += num*num
    return total

print(sumSquares([1,2,3]))  # 14

"""8. Find Maximum Difference

Problem: Find the difference between the largest and smallest number.

Input:
arr = [1, 5, 3, 9]

Output:
8"""

def maxDifference(arr):
    maximum = arr[0]
    minimum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum - minimum

print(maxDifference([1, 5, 3, 9]))  # 8

"""9. Count Words Starting with Vowel

Problem: Count words in a sentence that start with a vowel.

Input:
s = "apple orange banana umbrella"

Output:
3"""

def wordsStartingWithVowel(s):
    words = s.split()
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        if word[0].lower() in vowels:
            count += 1
    return count

print(wordsStartingWithVowel("apple orange banana umbrella"))  # 3

"""10. Sum of Digits

Problem: Return the sum of digits of a number.

Input:
n = 123

Output:
6"""

def sumDigits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

print(sumDigits(123))  # 6

"""11. Count Uppercase Letters

Problem: Count uppercase letters in a string.

Input:
s = "Hello World"

Output:
2
"""
def countUppercase(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    return count

print(countUppercase("Hello World"))  # 2

"""12. Count Lowercase Letters

Problem: Count lowercase letters in a string.

Input:
s = "Hello World"

Output:
8"""

def countLowercase(s):
    count = 0
    for c in s:
        if c.islower():
            count += 1
    return count

print(countLowercase("Hello World"))  # 8

"""13. Remove Duplicates from String

Problem: Remove duplicate characters from a string while preserving order.

Input:
s = "programming"

Output:
"progamin"
"""

def removeDuplicatesString(s):
    result = ""
    for c in s:
        if c not in result:
            result += c
    return result

print(removeDuplicatesString("programming"))  # progamin

"""14. Count Spaces in String

Problem: Count the number of spaces in a string.

Input:
s = "Hello World"

Output:
1
"""
def countSpaces(s):
    count = 0
    for c in s:
        if c == ' ':
            count += 1
    return count

print(countSpaces("Hello World"))  # 1

"""15. Count Even Digits

Problem: Count even digits in a number.

Input:
n = 123456

Output:
3"""

def countEvenDigits(n):
    count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            count += 1
    return count

print(countEvenDigits(123456))  # 3

"""16. Count Odd Digits

Problem: Count odd digits in a number.

Input:
n = 123456

Output:
3"""

def countOddDigits(n):
    count = 0
    for digit in str(n):
        if int(digit) % 2 != 0:
            count += 1
    return count

print(countOddDigits(123456))  # 3

"""17. Count Pairs with Sum

Problem: Count pairs of elements in an array whose sum equals k.

Input:
arr = [1,2,3,4], k = 5

Output:
2"""

def countPairs(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1
    return count

print(countPairs([1,2,3,4], 5))  # 2

"""18. Find First Positive

Problem: Return the first positive number in an array.

Input:
arr = [-1, -2, 3, 4]

Output:
3
"""
def firstPositive(arr):
    for num in arr:
        if num > 0:
            return num
    return None

print(firstPositive([-1, -2, 3, 4]))  # 3

"""19. Count Words Longer than N

Problem: Count words longer than length n in a sentence.

Input:
s = "Hello Python Developers", n = 5

Output:
2"""

def countLongWords(s, n):
    words = s.split()
    count = 0
    for word in words:
        if len(word) > n:
            count += 1
    return count

print(countLongWords("Hello Python Developers", 5))  # 2
"""
20. Sum of Positive Numbers

Problem: Return the sum of positive numbers in an array.

Input:
arr = [-1, 2, 3, -4]

Output:
5"""

def sumPositive(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

print(sumPositive([-1, 2, 3, -4]))  # 5


"""1. Problem:
Given an array arr and integer k, return "YES" if k exists, else "NO".

Input:
arr = [1,2,3,4,5], k = 3

Output:
YES"""
def findNumber(arr, k):
    if k in arr:
        return "YES"
    else:
        return "NO"


# Example usage
arr = [1, 2, 3, 4, 5]
k = 1
result = findNumber(arr, k)
print(result)



"""
2. Count Occurrences

Problem:
Count how many times k appears in the array.

Input:
arr = [1,2,2,3], k = 2

Output:
2
"""
def countOccurrences(arr, k):
    count = 0
    for num in arr:
        if num == k:
            count += 1
    return count

arr = [1, 2, 2, 3]
k = 2
print(countOccurrences(arr, k))  # Output: 2

"""3. Sum of Array

Problem:
Return the sum of all numbers in the array.

Input:
[1,2,3,4]

Output:
10"""
def arraySum(arr):
    total = 0
    for num in arr:
        total += num
    return total

arr = [1, 2, 3, 4]
print(arraySum(arr))  # Output: 10

"""4. Maximum Element

Problem:
Find the largest element.

Input:
[10, 5, 8]

Output:
10"""
def maxElement(arr):
    if not arr:
        return None
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

arr = [10, 5, 8]
print(maxElement(arr))  # Output: 10

"""5. Minimum Element

Problem:
Find the smallest element.

Input:
[10, 5, 8]

Output:
5"""
def minElement(arr):
    if not arr:
        return None
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum

arr = [10, 5, 8]
print(minElement(arr))  # Output: 5

"""6. Even or Odd Count

Problem:
Return count of even and odd numbers.

Input:
[1,2,3,4]

Output:
(2, 2)"""
def evenOddCount(arr):
    even = 0
    odd = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

arr = [1, 2, 3, 4]
print(evenOddCount(arr))  # Output: (2, 2)

"""7. Reverse an Array

Problem:
Reverse the array.

Input:
[1,2,3]

Output:
[3,2,1]"""
def reverseArray(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

arr = [1, 2, 3]
print(reverseArray(arr))  # Output: [3, 2, 1]

"""8. Check Sorted Array

Problem:
Check if array is sorted in ascending order.

Input:
[1,2,3]

Output:
YES"""
def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return "NO"
    return "YES"

arr = [1, 2, 3]
print(isSorted(arr))  # Output: YES

"""9. Find Index

Problem:
Return index of k or -1.

Input:
arr=[1,2,3], k=2

Output:
1"""
def findIndex(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

arr = [1, 2, 3]
k = 2
print(findIndex(arr, k))  # Output: 1

"""10. Remove Duplicates

Problem:
Remove duplicates while preserving order.

Input:
[1,2,2,3]

Output:
[1,2,3]"""
def removeDuplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result

arr = [1, 2, 2, 3]
print(removeDuplicates(arr))  # Output: [1, 2, 3]

"""11. Sum of Even Numbers

Input:
[1,2,4,5]

Output:
6"""
def sumEven(arr):
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total

arr = [1, 2, 4, 5]
print(sumEven(arr))  # Output: 6

"""12. String Length Check

Input:
"hello"

Output:
NO"""
def checkLength(s):
    if len(s) > 5:
        return "YES"
    else:
        return "NO"

s = "hello"
print(checkLength(s))  # Output: NO

"""13. Count Vowels

Input:
"hello"

Output:
2"""
def countVowels(s):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

s = "hello"
print(countVowels(s))  # Output: 2

"""14. Palindrome Check

Input:
"madam"

Output:
YES"""
def isPalindrome(s):
    n = len(s)
    is_palindrome = True
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            is_palindrome = False
            break
    if is_palindrome:
        return "YES"
    else:
        return "NO"

s = "madam"
print(isPalindrome(s))  # Output: YES

"""15. Second Largest Number

Input:
[1,5,3,4]

Output:
4"""
def secondLargest(arr):
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)
    largest = None
    second = None
    for num in unique:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif second is None or (num > second and num != largest):
            second = num
    return second

arr = [1, 5, 3, 4]
print(secondLargest(arr))  # Output: 4

"""16. Merge Two Arrays

Input:
[1,2] , [3,4]

Output:
[1,2,3,4]"""
def mergeArrays(a, b):
    merged = []
    for num in a:
        merged.append(num)
    for num in b:
        merged.append(num)
    return merged

a = [1, 2]
b = [3, 4]
print(mergeArrays(a, b))  # Output: [1, 2, 3, 4]

"""17. Product of Array

Input:
[1,2,3]

Output:
6"""
def productArray(arr):
    product = 1
    for num in arr:
        product *= num
    return product

arr = [1, 2, 3]
print(productArray(arr))  # Output: 6

"""18. Replace Negatives

Input:
[-1,2,-3]

Output:
[0,2,0]"""
def replaceNegatives(arr):
    new_arr = []
    for num in arr:
        if num < 0:
            new_arr.append(0)
        else:
            new_arr.append(num)
    return new_arr

arr = [-1, 2, -3]
print(replaceNegatives(arr))  # Output: [0, 2, 0]

"""19. Count Words

Input:
"Hello world from Python"

Output:
4"""
def countWords(s):
    words = s.split()
    count = 0
    for word in words:
        count += 1
    return count

s = "Hello world from Python"
print(countWords(s))  # Output: 4

"""20. Common Elements

Input:
[1,2,3], [2,3,4]

Output:
[2,3]"""
def commonElements(a, b):
    common = []
    for num in a:
        if num in b and num not in common:
            common.append(num)
    return common

a = [1, 2, 3]
b = [2, 3, 4]
print(commonElements(a, b))  # Output: [2, 3]

"""21. Factorial

Input:
5

Output:
120"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120
"""22. Fibonacci Series

Input:
5

Output:
[0,1,1,2,3]"""
def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]

"""23. Problem: Check if a number n is prime. Return "YES" or "NO".

Input:
n = 7

Output:
YES
"""
def isPrime(n):
    if n < 2:
        return "NO"
    for i in range(2, n):
        if n % i == 0:
            return "NO"
    return "YES"

# Example usage
print(isPrime(7))  # YES


"""24. Count Digits

Input:
1234

Output:
4"""
def countDigits(n):
    count = 0
    for digit in str(n):
        count += 1
    return count

print(countDigits(1234))  # Output: 4

"""25. Sum of Digits

Input:
123

Output:
6"""

def sumDigits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

print(sumDigits(123))  # Output: 6
"""26. Remove Spaces

Input:
"hello world"

Output:
"helloworld"""
def removeSpaces(s):
    result = ""
    for c in s:
        if c != " ":
            result += c
    return result

print(removeSpaces("hello world"))  # Output: helloworld

"""27. Uppercase String

Input:
"python"

Output:
"PYTHON"
"""
def toUpper(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

print(toUpper("python"))  # Output: PYTHON

"""28. Count Positive Numbers

Input:
[-1, 2, 3, -4]

Output:
2"""
def countPositive(arr):
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    return count

print(countPositive([-1, 2, 3, -4]))  # Output: 2

"""29. Find Missing Number

Input:
[1,2,4,5]

Output:
3"""
def missingNumber(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in arr:
        actual_sum += num
    return expected_sum - actual_sum

print(missingNumber([1, 2, 4, 5]))  # Output: 3

"""30. Swap First and Last

Input:
[1,2,3,4]

Output:
[4,2,3,1]"""
def swapFirstLast(arr):
    if len(arr) < 2:
        return arr
    first = arr[0]
    last = arr[-1]
    arr[0] = last
    arr[-1] = first
    return arr

print(swapFirstLast([1, 2, 3, 4]))  # Output: [4, 2, 3, 1]

"""
Problem

Given an integer n, return the numbers from 1 to n following these rules:

If the number is divisible by 3, print "Fizz".

If the number is divisible by 5, print "Buzz".

If the number is divisible by both 3 and 5, print "FizzBuzz".

Otherwise, print the number itself.

Example

For n = 15

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

class Solution:
    def fizzBuzz(self, n: int):

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

solution = Solution()
solution.fizzBuzz(15)