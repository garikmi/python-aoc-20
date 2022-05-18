import re

with open('input.txt', 'r') as file:
    try:
        blocks = [line.strip().split('\n') for line in file.read().split('\n\n')]

        notes = []
        my_ticket = []
        nearby_tickets = []
        
        for line in blocks[0]:
            formatted = [[int(number) for number in range] for range in [num.split('-') for num in re.findall('\d+-\d+', line)]]
            for num in formatted:
                notes.append(num)

        blocks[1].pop(0)
        for line in blocks[1]:
            formatted = [int(number) for number in line.split(',')]
            for num in formatted:
                my_ticket.append(num)

        blocks[2].pop(0)
        for line in blocks[2]:
            formatted = [int(number) for number in line.split(',')]
            for num in formatted:
                nearby_tickets.append(num)

        sum = 0
        for number in nearby_tickets:
            in_Range = False
            for num_range in notes:
                if number >= num_range[0] and number <= num_range[1]:
                    in_Range = True
                    break
            if not in_Range:
                sum += number
        print(sum)
    finally:
        file.close()
