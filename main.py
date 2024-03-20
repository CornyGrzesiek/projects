list = []

with open("bin_przyklad.txt") as file:
    for line in file:
        list.append(str(line.strip()))


def count_blocks(number):
    blocks = 0
    prev_letter = ''
    for letter in number:
        if blocks == 0:
            blocks += 1
            prev_letter = letter
        else:
            if letter != prev_letter:
                blocks += 1
                prev_letter = letter
    return blocks


counter = 0
for number in list:
    if count_blocks(number) <= 2:
        counter += 1

print(counter)

