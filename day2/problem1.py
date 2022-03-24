with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        lineList = line.split(' ')
        range = list(map(int, lineList[0].split('-')))
        letter = lineList[1][0]
        password = lineList[2].strip("\n")

        if range[0] <= password.count(letter) <= range[1]:
            count += 1

print(count)
