with open('input.txt', 'r') as f:
    numbers = list(map(int, f.readlines()))

    for index in range(0, len(numbers), 1):
        for index2 in range(1, len(numbers), 1):
            if numbers[index] + numbers[index2] == 2020:
                print(numbers[index] * numbers[index2])
                break
        else: continue
        break
