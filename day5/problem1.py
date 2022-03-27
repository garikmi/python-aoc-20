import math

with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]
    highest_id = 0
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
        if (lower_row * 8 + lower_col) > highest_id:
            highest_id = (lower_row * 8 + lower_col)
    print(highest_id)
