# Given two binary strings a and b, return their sum as a binary string.

def add_binary(a: str, b: str) -> str:
    # int(x, 2) changes it into binary. Argument 2 means the binary system
    # bin() changes it into binary
    # [2:] cuts 2 starting letters that are 0b
    return str(bin(int(a, 2)+int(b, 2)))[2:]
