str = input("")
str2 = ""

for i in range(0, len(str)):
    if str[i].isdigit():
        n = int(str[i])
        str2 += str[i - 1] * (n - 1)
    else:
        str2 += str[i]

print(str2)