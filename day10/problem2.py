with open('input.txt', 'r') as file:
    numbers = [int(number.strip()) for number in file.readlines()]

    number = 0
    preamble = 25

    for index in range(0, len(numbers), 1):
        if (index + preamble) < len(numbers):
            did_find = False
            for i in range(index, index+preamble, 1):
                for val_i in range(i+1, index+preamble+1, 1):
                    if numbers[i] + numbers[val_i] == numbers[index+preamble]:
                        did_find = True
                        break
                else: continue
                break
            if not did_find:
                number = numbers[index+preamble]
                print(f'did not find at {numbers[index+preamble]}')
                break
        else:
            break

    for index in range(0, len(numbers)-1, 1):
        list_numbers = [numbers[index]]
        sum = list_numbers[0]
        for i in range(index+1, len(numbers), 1):
            sum += numbers[i]
            list_numbers.append(numbers[i])
            if sum == number:
                list_numbers.sort()
                print(list_numbers[0] + list_numbers[-1])
                break
        else: continue
        break
