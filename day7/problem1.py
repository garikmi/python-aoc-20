with open('input.txt', 'r') as file:
    numbers = [int(number) for number in file.read().strip().split(',')]
    repeats = []
    sp_repeats = []
    highest_count = 0
    for number in numbers:
        if number not in repeats:
            repeats.append(number)
            counter = 0
            for inner_number in numbers:
                if number == inner_number:
                    counter += 1
            if counter > highest_count:
                highest_count = counter
                sp_repeats = []
            sp_repeats.append(number)
    total = None
    for number in sp_repeats:
        sum = 0
        for inner_number in numbers:
            if inner_number > number:
                sum += inner_number - number
            if number > inner_number:
                sum += number - inner_number
        if total == None:
            total = sum
        elif sum < total:
            total = sum
    print(total)
