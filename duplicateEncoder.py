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

def duplicate_encode(word):
    #your code here
    

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