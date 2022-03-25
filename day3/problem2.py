with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]
    data = [list(character) for character in data]

    def count_trees(right_amount, line_amount):
        counter = 0
        charPos = 0
        linePos = 0

        while linePos < len(data)-1:
            charPos += right_amount
            if charPos >= len(data[0]):
                charPos -= len(data[0])
            linePos += line_amount
            if data[linePos][charPos] == '#':
                counter += 1
        return counter

    print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))
