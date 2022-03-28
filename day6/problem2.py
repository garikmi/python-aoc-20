with open('input.txt', 'r') as file:
    data = [entry.split() for entry in file.read().split('\n\n')]
    counter = 0
    for group in data:
        answered = ''       
        for entry in group:
            for character in entry:
                if character not in answered:
                    contains = True
                    answered += character 
                    for entry_inner in group:
                        if character not in entry_inner:
                            contains = False
                            break
                    if contains:
                        counter += 1
    print(counter)
