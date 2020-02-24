#problem
#Given a string, return a new string where the first and last chars have been exchanged.

if len(str) <= 1:
    return str
else:
    return str[len(str) - 1] + str[1:(len(str) - 1)] + str[0]