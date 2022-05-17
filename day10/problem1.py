with open('input.txt', 'r') as file:
    numbers = [int(number.strip()) for number in file.readlines()]

    preamble = 25

    for index in range(0, len(numbers), 1):
        if (index + preamble) < len(numbers):
            did_find = False
            for i in range(index, index+preamble, 1):
                for val_i in range(i+1, index+preamble+1, 1):
                    if numbers[i] + numbers[val_i] == numbers[index+preamble]:
                        print(f'{numbers[i]} + {numbers[val_i]} = {numbers[index+preamble]}')
                        did_find = True
                        break
                    print(f'{numbers[i]} + {numbers[val_i]} != {numbers[index+preamble]}')
                else: continue
                break
            if not did_find:
                print(f'did not find at {numbers[index+preamble]}')
                break
        else:
            break
