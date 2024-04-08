with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

ages = [int(line.split()[-1]) for line in lines]

oldest_idx = ages.index(max(ages))
youngest_idx = ages.index(min(ages))

oldest_child = lines[oldest_idx]
youngest_child = lines[youngest_idx]

with open("oldest_child.txt", "w") as file:
    file.write(oldest_child)

with open("youngest_child.txt", "w") as file:
    file.write(youngest_child)
