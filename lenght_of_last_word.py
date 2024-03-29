# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s: str) -> int:

    words = s.split(" ")
    # 1 idea
    # words = [x for x in words if x != ""]
    # 2 idea
    words = list(filter(lambda x: x != "", words))
    return len(words[-1])
