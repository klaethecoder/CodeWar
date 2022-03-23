# Instructions
# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

# Kata 6kyu

def expanded_form(num):
    num = str(num)
    st = ""
    for index, element in enumerate(num):
        if element !="0":
            st+= " + " + element+(len(num)-(index+1))*'0'
        else:
            pass
    return st.strip(" + ")

# Testing:
# test.assert_equals(expanded_form(12), '10 + 2');
# test.assert_equals(expanded_form(42), '40 + 2');
# test.assert_equals(expanded_form(70304), '70000 + 300 + 4');

# Solutions:

# Solution 1:
# def expanded_form(num):
#     return ' + '.join([x+'0'*i for i,x in enumerate(str(num)[::-1]) if x != '0'][::-1])

# Solution 2:
# def expanded_form(num):
#     return " + ".join([str(int(d) * 10**p) for p, d in enumerate(str(num)[::-1]) if d != "0"][::-1])

# Solution 3:
# def expanded_form(n):
#     result = []
#     for a in range(len(str(n)) - 1, -1, -1):
#         current = 10 ** a
#         quo, n = divmod(n, current)
#         if quo:
#             result.append(str(quo * current))
#     return ' + '.join(result)

# Solution 4:
# def expanded_form(num):
#     num = list(str(num))
#     return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')