with open('input.txt', 'r') as file:
    numbers = [int(number) for number in file.read().strip().split(',')]
    sum = 0
    for number in numbers:
        sum += number
    pos = int(sum / len(numbers))
    total = 0
    for number in numbers:
        if pos > number:
            val = (pos - number)
            total += int(val * (val + 1) / 2)
        if number > pos:
            val = (number - pos)
            total += int(val * (val + 1) / 2)
    print(total)
