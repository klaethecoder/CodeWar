# Instructions

# The main idea is to count all the occurring characters in a string. If you have a string like aba, 
# then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

# Kata 6kyu

def count(string):
    # The function code should be here
    d = {}
    for letter in string:
        if letter in d.keys():
            d[letter] += 1
        else:
            d[letter] = 1
    return d

# Testing
# test.assert_equals(count('aba'), {'a': 2, 'b': 1})
# test.assert_equals(count(''), {})

# Solutions:

# Solution 1:
# from collections import Counter

# def count(string):
#     return Counter(string)

# Solution 2:
# def count(string):
  
    # return {i: string.count(i) for i in string}

    