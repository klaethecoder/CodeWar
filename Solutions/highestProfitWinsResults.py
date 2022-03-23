# Instructions
# Story
# Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't 
# give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it 
# for the lowest possible price and sell it at the highest.

# Task
# Write a function that returns both the minimum and maximum number of the given list/array.

# Examples
# min_max([1,2,3,4,5])   == [1,5]
# min_max([2334454,5])   == [5, 2334454]
# min_max([1])           == [1, 1]
# Remarks
# All arrays or lists will always have at least one element, so you don't need to check the length. Also, your 
# function will always get an array or a list, you don't have to check for null, undefined or similar.

# Kata 7kyu

def min_max(lst):
  return [min(lst), max(lst)]



# import codewars_test as test
# from solution import min_max
# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(min_max([1,2,3,4,5]), [1, 5])
#         test.assert_equals(min_max([2334454,5]), [5, 2334454])

# Solutions:

# Solution 1:
# def min_max(lst):
#     return [sorted(lst)[0],sorted(lst)[-1]]

# Solution 2:
# min_max = lambda l: [min(l), max(l)]

# Solution 3:
# def min_max(lst):
#   lst.sort()
#   tempor = [lst[0],lst[-1]]
#   return tempor

# Solution 4:
# def min_max(lst):
#   # Too easy, but requires two pases
#   # return[min(lst), max(lst)]
  
#   # Single pass:
#   l, u = None, None
#   for n in lst:
#       if l is None or n < l:
#           l = n
#       if u is None or n > u:
#           u = n
#   return [l, u]

