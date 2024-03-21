# Given an integer x, return true if x is a palindrome and false otherwise.
# Easy solution  return str(x) == str(x)[::-1]

def isPalindrome(x: int) -> bool:
    tmp = x
    reversedx = 0
    if x < 0:
        return False
    while x != 0:
        digit = x % 10
        reversedx = reversedx * 10 + digit
        x //= 10
    return reversedx == tmp
