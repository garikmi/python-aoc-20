with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        lineList = line.split(' ')
        positions = list(map(int, lineList[0].split('-')))
        letter = lineList[1][0]
        password = lineList[2].strip("\n")

        if (password[positions[0]-1] == letter and password[positions[1]-1] != letter) or (password[positions[0]-1] != letter and password[positions[1]-1] == letter):
            count += 1

print(count)
