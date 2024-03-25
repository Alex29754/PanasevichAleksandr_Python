n = int(input())
cities = set()
for i in range(n):
    city = input()
    if city in cities:
        print("REPEAT")
    else:
        print("OK")
        cities.add(city)