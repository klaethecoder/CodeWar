# Instructions:
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if 
# that character appears only once in the original string, or ")" if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.
# 
# 6kyu Examples:
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

# My Solution
def duplicate_encode(word):
    word = word.lower()
    count = {}
    temp = ""
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for letter in word:
        if letter in count and count[letter] > 1:
            temp+=")"
        else:
            temp+="("
    return temp

print(duplicate_encode("Success"))

# Tests: 
# import codewars_test as test
# from solution import duplicate_encode

# @test.describe("Duplicate Encoder")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(duplicate_encode("din"),"(((")
#         test.assert_equals(duplicate_encode("recede"),"()()()")
#         test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
#         test.assert_equals(duplicate_encode("(( @"),"))((")


# Solution 1:
#This solution is O(n) instead of O(n^2) like the methods that use .count()
#because .count() is O(n) and it's being used within an O(n) method.
#The space complexiety is increased with this method.
# import collections
# def duplicate_encode(word):
#     new_string = ''
#     word = word.lower()
#     #more info on defaultdict and when to use it here:
#     #http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python
#     d = collections.defaultdict(int)
#     for c in word:
#         d[c] += 1
#     for c in word:
#         new_string = new_string + ('(' if d[c] == 1 else ')')
#     return new_string

# Solution 2:
# def duplicate_encode(word):
# return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# Solution 3:
# from collections import Counter

# def duplicate_encode(word):
#     word = word.lower()
#     counter = Counter(word)
#     return ''.join(('(' if counter[c] == 1 else ')') for c in word)