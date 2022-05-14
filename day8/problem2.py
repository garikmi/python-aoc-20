with open('input.txt', 'r') as file:
    commands = [command.strip().split(' ') for command in file.readlines()]

    indexes = []
    for index in range(0, len(commands)-1, 1):
        if commands[index][0] == 'jmp':
            indexes.append(index)
        if commands[index][0] == 'nop' and commands[index][1] != '+0' and commands[index][1] != '-0':
            indexes.append(index)

    def will_complete():
        repeated = [0 for _ in range(len(commands))]
        accumulator = 0
        offset = 0

        while True:
            if offset <= len(commands)-1 and repeated[offset] <= len(commands)-1:
                repeated[offset] += 1
                if repeated[offset] == 2:
                    return False, accumulator
            else:
                return True, accumulator
            if commands[offset][0] == 'acc':
                accumulator += int(commands[offset][1])
            if commands[offset][0] == 'jmp':
                offset += int(commands[offset][1])
                continue
            offset += 1

    check = will_complete()
    if check[0]:
        print('Finishes with accum: ', check[1])
    else:
        for index in indexes:
            if commands[index][0] == 'jmp':
                commands[index][0] = 'nop'
                inner_check = will_complete()
                if inner_check[0]:
                    print('Worked by reversing with accum: ', inner_check[1])
                    break
                else:
                    commands[index][0] = 'jmp'
            if commands[index][0] == 'nop':
                commands[index][0] = 'jmp'
                inner_check = will_complete()
                if inner_check[0]:
                    print('Worked by reversing with accum: ', inner_check[1])
                    break
                else:
                    commands[index][0] = 'nop'
