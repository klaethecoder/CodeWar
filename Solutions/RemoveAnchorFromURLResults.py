# Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

# Kata 7 kyu


def remove_url_anchor(url):
    # TODO: complete
    return url[0:url.index("#")] if "#" in url else url

# Testing:
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
#         test.assert_equals(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
#         test.assert_equals(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")

# Solutions:

# Solition 1:
# def remove_url_anchor(url):
    # index = url.find('#')
    # return url[:index] if index >= 0 else url

# Solution 2:
# def remove_url_anchor(url):
#   import re
#   return re.sub('#.*$','',url)

# Solution 3:
# def remove_url_anchor(url):
#   return url.partition('#')[0]

# Solution 4:
# def remove_url_anchor(url):
#   return url.split('#')[0]