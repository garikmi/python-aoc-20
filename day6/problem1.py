with open('input.txt', 'r') as file:
    data = [entry.replace('\n', '') for entry in file.read().split('\n\n')]
    counter = 0
    for entry in data:
        answered = ''
        for letter in entry:
            if letter not in answered:
                counter += 1
                answered += letter
    print(counter)
