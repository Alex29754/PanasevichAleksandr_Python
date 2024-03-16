def count_string_repetitions(strings):
    count_dict = {}
    for string in strings:
        if string in count_dict:
            count_dict[string] += 1
        else:
            count_dict[string] = 1
    for key, value in count_dict.items():
        print(value, end=' ')


strings1 = input().split()

count_string_repetitions(strings1)