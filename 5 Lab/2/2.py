with open('input.txt', 'r') as file:
    numbers = [int(num) for num in file.read().splitlines()]

sorted_numbers = sorted(numbers)

with open('output.txt', 'w') as file:
    for num in sorted_numbers:
        file.write(str(num) + '\n')