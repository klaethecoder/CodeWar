# Task:
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# 7kyu Example:

def odd_or_even(arr):
    sum = 0
    for num in arr:
        sum+= num   
    return "even" if sum %2 == 0 else "odd"


# Testing:
# import codewars_test as test
# from solution import odd_or_even

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(odd_or_even([0, 1, 2]), "odd")
#         test.assert_equals(odd_or_even([0, 1, 3]), "even")
#         test.assert_equals(odd_or_even([1023, 1, 2]), "even")

# Solution 1:
# def oddOrEven(arr):
#     return ('even', 'odd')[sum(arr) % 2]

# Solution 2:
# def oddOrEven(arr):
#     return "odd" if sum(arr)%2 else "even"

# Solution 3:
# def oddOrEven(arr):
#     return 'even' if sum(arr) % 2 == 0 else 'odd'