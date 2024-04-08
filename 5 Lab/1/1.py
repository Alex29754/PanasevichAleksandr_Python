with open('input.txt', 'r') as file:
    numbers = list(map(int, file.readline().split()))

product = 1
for num in numbers:
    product *= num

with open('output.txt', 'w') as file:
    file.write(str(product))