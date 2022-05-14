with open('input.txt', 'r') as file:
    commands = [command.strip().split(' ') for command in file.readlines()]
    repeated = [0 for _ in range(len(commands))]

    accumulator = 0
    offset = 0
    
    while True:
        repeated[offset] += 1
        if repeated[offset] > 1:
            print('Accumulator: ', accumulator)
            break
        if commands[offset][0] == 'acc':
            accumulator += int(commands[offset][1])
        if commands[offset][0] == 'jmp':
            offset += int(commands[offset][1])
            continue
        offset += 1
