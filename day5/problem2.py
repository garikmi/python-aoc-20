import math

with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]
    ids = []
    for entry in data:
        lower_row = 0
        upper_row = 127
        for character in entry[0:-3]:
            if character == 'B':
                lower_row = math.ceil((upper_row - lower_row) / 2 + lower_row)
            if character == 'F':
                upper_row = math.floor((upper_row - lower_row) / 2 + lower_row)
        lower_col = 0
        upper_col = 7
        for character in entry[-3:]:
            if character == 'R':
                lower_col = math.ceil((upper_col - lower_col) / 2 + lower_col)
            if character == 'L':
                upper_col = math.floor((upper_col - lower_col) / 2 + lower_col)
        ids.append(lower_row * 8 + lower_col)
    ids.sort()
    for number in range(ids[0], ids[-1]+1):
        if number not in ids:
            print(number)
            break
