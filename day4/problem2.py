with open('input.txt', 'r') as file:
    data = [[entry.split(':') for entry in password] for password in [line.split(' ') for line in [line.replace('\n', ' ') for line in file.read().strip().split('\n\n')]]]
    counter = 0
    for password_index in range(len(data)):
        byr = iyr = eyr = hgt = hcl = ecl = pid = cid = False
        for entry_index in range(len(data[password_index])):
            key = data[password_index][entry_index][0]
            value = data[password_index][entry_index][1]
            if key == 'byr' and len(value) == 4 and 1920 <= int(value) <= 2002:
                byr = True
            if key == 'iyr' and len(value) == 4 and 2010 <= int(value) <= 2020:
                iyr = True
            if key == 'eyr' and len(value) == 4 and 2020 <= int(value) <= 2030:
                eyr = True
            if key == 'hgt':
                if value[-2:] == 'cm' and 150 <= int(value[0:-2]) <= 193:
                    hgt = True
                if value[-2:] == 'in' and 59 <= int(value[0:-2]) <= 76:
                    hgt = True
            if key == 'hcl' and len(value[1:]) == 6:
                validate = True
                for char_index in range(1, len(value)-1):
                    if not value[char_index].isnumeric() and not 'A' <= value[char_index].upper() <= 'F':
                        validate = False
                        break
                if validate:
                    hcl = True
            if key == 'ecl':
                if value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth':
                    ecl = True
            if key == 'pid' and len(value) == 9:
                pid = True
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            counter += 1
    print(counter)
