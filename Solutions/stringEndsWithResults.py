# Instructions:
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Kata: 7kyu

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    # your code here...
    if ending == "":
        return True
    return string[-len(ending):] == ending

# Tests:
# test.assert_equals(solution('abcde', 'cde'), True)
# test.assert_equals(solution('abcde', 'abc'), False)
# test.assert_equals(solution('abcde', ''), True)

# Solutions:

# Solution 1:
# def solution(string, ending):
#     if string.endswith(ending):
#         return True
#     return False

# Solution 2:
# def solution(string, ending):
#     return ending in string[-len(ending):]

# Solution 3:
# def solution(string, ending):
#     return string.endswith(ending)