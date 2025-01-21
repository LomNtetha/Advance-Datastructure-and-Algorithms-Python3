"""
1. Find the Number That Appears Once (XOR Property)
Question: Given a list where every element appears twice except for one, find the unique element.
Input: [4, 1, 2, 1, 2]
Output: 4
"""

def single_number(nums):
    # Initialize result to 0
    result = 0
    # XOR all numbers in the list
    for num in nums:
        result ^= num  # XOR operation cancels out duplicates
    return result

# Input: [4, 1, 2, 1, 2]
# Output: 4
print(single_number([4, 1, 2, 1, 2]))

# Time Complexity: O(n), where n is the size of the list
# Space Complexity: O(1)


"""
2. Count the Number of 1s in a Binary Representation
Question: Write a function to count the number of 1s in the binary representation of a number.
Input: 9 (binary: 1001)
Output: 2
"""
def count_ones(n):
    # Initialize count to 0
    count = 0
    # Loop until n becomes 0
    while n:
        n &= n - 1  # Removes the rightmost 1-bit
        count += 1  # Increment count for each 1-bit removed
    return count

# Input: 9
# Output: 2 (Binary representation of 9 is 1001)
print(count_ones(9))

# Time Complexity: O(k), where k is the number of set bits
# Space Complexity: O(1)


"""
3. Check if a Number is a Power of Two
Question: Determine if a number is a power of 2 using bitwise operations.
Input: 16
Output: True
"""

def is_power_of_two(n):
    # A number is a power of two if it has exactly one 1-bit in its binary representation
    return n > 0 and (n & (n - 1)) == 0

# Input: 16
# Output: True (16 = 2^4)
print(is_power_of_two(16))

# Time Complexity: O(1)
# Space Complexity: O(1)


"""
4. Reverse the Bits of an Integer
Question: Reverse the bits of a 32-bit unsigned integer.
Input: 43261596 (binary: 00000010100101000001111010011100)
Output: 964176192 (binary: 00111001011110000010100101000000)

"""
def reverse_bits(n):
    result = 0
    # Iterate through all 32 bits
    for _ in range(32):
        result = (result << 1) | (n & 1)  # Shift result left and add the least significant bit of n
        n >>= 1  # Shift n to the right
    return result

# Input: 43261596 (Binary: 00000010100101000001111010011100)
# Output: 964176192 (Binary: 00111001011110000010100101000000)
print(reverse_bits(43261596))

# Time Complexity: O(32) = O(1)
# Space Complexity: O(1)


"""
5. Find XOR of All Numbers in a Range
Question: Compute the XOR of all numbers in the range [L, R].
Input: L = 3, R = 6
Output: 0
"""

def xor_range(L, R):
    # Helper function to calculate XOR from 0 to x
    def xor_upto(x):
        if x % 4 == 0: return x
        if x % 4 == 1: return 1
        if x % 4 == 2: return x + 1
        return 0

    # XOR from L to R is XOR(0 to R) ^ XOR(0 to L-1)
    return xor_upto(R) ^ xor_upto(L - 1)

# Input: L = 3, R = 6
# Output: 0 (3 ^ 4 ^ 5 ^ 6 = 0)
print(xor_range(3, 6))

# Time Complexity: O(1)
# Space Complexity: O(1)


"""
6. Swap Two Numbers Without Using a Temporary Variable
Question: Swap two numbers using XOR.
Input: a = 5, b = 9
Output: a = 9, b = 5
"""

def swap(a, b):
    # XOR-based swap
    a = a ^ b
    b = a ^ b  # Now b = original a
    a = a ^ b  # Now a = original b
    return a, b

# Input: a = 5, b = 9
# Output: a = 9, b = 5
print(swap(5, 9))

# Time Complexity: O(1)
# Space Complexity: O(1)


"""
7. Find the Two Non-Repeating Numbers in an Array
Question: In an array where all elements appear twice except for two, find those two unique numbers.
Input: [2, 4, 6, 8, 4, 2]
Output: [6, 8]
"""

def find_two_unique(nums):
    # XOR all numbers to find the XOR of the two unique numbers
    xor = 0
    for num in nums:
        xor ^= num

    # Find the rightmost set bit in xor (difference between the two numbers)
    diff = xor & -xor
    a, b = 0, 0

    # Divide numbers into two groups based on the rightmost set bit
    for num in nums:
        if num & diff:
            a ^= num  # XOR of one group
        else:
            b ^= num  # XOR of the other group
    return a, b

# Input: [2, 4, 6, 8, 4, 2]
# Output: (6, 8)
print(find_two_unique([2, 4, 6, 8, 4, 2]))

# Time Complexity: O(n)
# Space Complexity: O(1)


"""
8. Turn Off the Rightmost 1 Bit
Question: Write a function to turn off the rightmost set bit of an integer.
Input: 12 (binary: 1100)
Output: 8 (binary: 1000)
"""

def turn_off_rightmost_bit(n):
    # Turn off the rightmost 1-bit using n & (n - 1)
    return n & (n - 1)

# Input: 12 (Binary: 1100)
# Output: 8 (Binary: 1000)
print(turn_off_rightmost_bit(12))

# Time Complexity: O(1)
# Space Complexity: O(1)


"""

9. Check if a Number has Alternating Bits
Question: Determine if the binary representation of a number has alternating 0s and 1s.
Input: 5 (binary: 101)
Output: True
"""
def has_alternating_bits(n):
    # XOR the number with itself shifted right by 1, and check if the result has all bits set
    x = n ^ (n >> 1)
    return (x & (x + 1)) == 0

# Input: 5 (Binary: 101)
# Output: True
print(has_alternating_bits(5))

# Time Complexity: O(1)
# Space Complexity: O(1)


"""
10. Find the Only Missing Number in an Array
Question: An array contains all numbers from 0 to n except one. Find the missing number.
Input: [0, 1, 3]
Output: 2"""

def missing_number(nums):
    # XOR all indices and numbers to find the missing number
    n = len(nums)
    expected_xor = 0
    actual_xor = 0
    for i in range(n + 1):
        expected_xor ^= i
    for num in nums:
        actual_xor ^= num
    return expected_xor ^ actual_xor

# Input: [0, 1, 3]
# Output: 2
print(missing_number([0, 1, 3]))

# Time Complexity: O(n)
# Space Complexity: O(1)


"""11. Count Flipped Bits to Convert A to B
Question: Count the number of bits to be flipped to convert integer A to B.
Input: A = 10, B = 20
Output: 4"""

def count_flipped_bits(a, b):
    # XOR a and b to find differing bits, then count 1s
    xor = a ^ b
    return bin(xor).count('1')

# Input: A = 10 (Binary: 1010), B = 20 (Binary: 10100)
# Output: 4
print(count_flipped_bits(10, 20))

# Time Complexity: O(k), where k is the number of set bits
# Space Complexity: O(1)


"""12. Determine if Two Numbers Differ by One Bit
Question: Check if two integers differ by exactly one bit.
Input: a = 5, b = 7
Output: True"""

def differ_by_one_bit(a, b):
    # XOR a and b, and check if the result is a power of two
    xor = a ^ b
    return (xor & (xor - 1)) == 0

# Input: a = 5 (Binary: 101), b = 7 (Binary: 111)
# Output: True
print(differ_by_one_bit(5, 7))

# Time Complexity: O(1)
# Space Complexity: O(1)


"""
13. Find Position of Rightmost Set Bit
Question: Find the position of the rightmost set bit in an integer.
Input: 18 (binary: 10010)
Output: 2"""
def rightmost_set_bit_position(n):
    # If n is 0, there are no set bits
    if n == 0:
        return 0
    # Calculate position using n & -n, and find the bit length
    return (n & -n).bit_length()

# Input: 18 (binary: 10010)
# Output: 2
print(rightmost_set_bit_position(18))



"""
14. Check if a Number is Odd or Even
Question: Check whether a number is odd or even using a bitwise operator.
Input: 15
Output: Odd
"""
def is_odd_or_even(n):
    # Use bitwise AND with 1 to check the least significant bit
    return "Odd" if n & 1 else "Even"

# Input: 15
# Output: Odd
print(is_odd_or_even(15))


"""
15. Add Two Numbers Without Using Arithmetic Operators
Question: Add two integers without using + or -.
Input: a = 5, b = 3
Output: 8
"""
def add_without_arithmetic(a, b):
    while b != 0:
        carry = a & b  # Calculate carry
        a = a ^ b      # Perform addition without carry
        b = carry << 1 # Shift carry to the left
    return a

# Input: a = 5, b = 3
# Output: 8
print(add_without_arithmetic(5, 3))

"""
16. Divide Two Numbers Without Using Division Operator
Question: Divide two integers without using / or //.
Input: dividend = 15, divisor = 3
Output: 5"""
def divide_without_operator(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed")
    # Handle edge case for overflow
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1

    negative = (dividend < 0) ^ (divisor < 0)  # Determine the result's sign
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    while dividend >= divisor:
        temp_divisor, multiple = divisor, 1
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        dividend -= temp_divisor
        quotient += multiple

    return -quotient if negative else quotient

# Input: dividend = 15, divisor = 3
# Output: 5
print(divide_without_operator(15, 3))


"""
17. Determine if a Bit is Set at a Given Position
Question: Check if the bit at a specific position (0-indexed) is set.
Input: number = 5, position = 1 (binary: 101)
Output: True"""

def is_bit_set(n, position):
    # Check if the bit at the given position is set
    return (n & (1 << position)) != 0

# Input: number = 5, position = 1 (binary: 101)
# Output: True
print(is_bit_set(5, 1))


"""
18. Toggle a Specific Bit
Question: Toggle the bit at a given position in an integer.
Input: number = 10, position = 1 (binary: 1010)
Output: 8 (binary: 1000)"""
def toggle_bit(n, position):
    # Toggle the bit at the given position
    return n ^ (1 << position)

# Input: number = 10, position = 1 (binary: 1010)
# Output: 8 (binary: 1000)
print(toggle_bit(10, 1))


"""
19. Clear All Bits from MSB to ith Bit
Question: Clear all bits from the most significant bit (MSB) to a specified bit.
Input: number = 31, position = 2 (binary: 11111)
Output: 3 (binary: 00011)"""

def clear_bits_msb_to_i(n, position):
    # Create a mask with all bits after the specified position set
    mask = (1 << position) - 1
    return n & mask

# Input: number = 31, position = 2 (binary: 11111)
# Output: 3 (binary: 00011)
print(clear_bits_msb_to_i(31, 2))


"""
20. Rotate Bits of a Number
Question: Rotate the bits of an integer left by k positions.
Input: number = 16, k = 2 (binary: 10000)
Output: 64 (binary: 1000000)
"""
def rotate_bits_left(n, k, bit_width=32):
    # Perform rotation to the left by k positions
    k %= bit_width  # Ensure k is within bit width
    return ((n << k) | (n >> (bit_width - k))) & ((1 << bit_width) - 1)

# Input: number = 16, k = 2 (binary: 10000)
# Output: 64 (binary: 1000000)
print(rotate_bits_left(16, 2))

