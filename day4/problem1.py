with open('input.txt', 'r') as file:
    data = [[entry.split(':') for entry in password] for password in [line.split(' ') for line in [line.replace('\n', ' ') for line in file.read().strip().split('\n\n')]]]
    counter = 0
    for password_index in range(len(data)):
        byr = iyr = eyr = hgt = hcl = ecl = pid = cid = False
        for entry_index in range(len(data[password_index])):
            key = data[password_index][entry_index][0]
            if key == 'byr':
                byr = True
            if key == 'iyr':
                iyr = True
            if key == 'eyr':
                eyr = True
            if key == 'hgt':
                hgt = True
            if key == 'hcl':
                hcl = True
            if key == 'ecl':
                ecl = True
            if key == 'pid':
                pid = True
            if key == 'cid':
                cid = True
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            counter += 1
    print(counter)
