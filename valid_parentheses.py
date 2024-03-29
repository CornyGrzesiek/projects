
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def is_valid(s):
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or \
                    (char == ')' and stack[-1] != '(') or \
                    (char == '}' and stack[-1] != '{') or \
                    (char == ']' and stack[-1] != '['):
                return False
            stack.pop()
    return True
