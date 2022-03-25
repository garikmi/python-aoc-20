with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]
    data = [list(character) for character in data]

    counter = 0
    charPos = 0
    linePos = 0

    while linePos < len(data)-1:
        charPos += 3
        if charPos >= len(data[0]):
            charPos -= len(data[0])
        linePos += 1
        if data[linePos][charPos] == '#':
            counter += 1

    print(counter)
