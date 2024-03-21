# Given a roman numeral, convert it to an integer

def roman_to_int(s: str) -> int:
    value = 0
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, 'P': 12}
    prev_number = 0
    for char in s:
        if char in roman_dict:
            current_number = roman_dict[char]
            value += current_number
            if current_number > prev_number:
                value -= prev_number * 2
            prev_number = current_number

    return value




