# Instructions:
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
# without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    new_list = []
    for letter in iterable:
        if new_list == []:
            new_list.append(letter)
        elif new_list[-1] != letter:
            new_list.append(letter)
    return new_list

print(unique_in_order('AAAABBBCCDAABBB'))


# Testing:
# test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])

# Examples:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# Solution 1:
# def unique_in_order(iterable):
#     new_list = []
#     for letter in iterable:
#         letter in new_list[-1:] or new_list.append(letter)
#     return new_list
