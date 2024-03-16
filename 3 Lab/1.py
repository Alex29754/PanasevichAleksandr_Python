def encode_string(s):
    encoded_string = ""
    current_char = ""
    char_count = 0

    for char in s:
        if char != current_char:
            if char_count > 1:
                encoded_string += current_char + str(char_count)
            elif char_count == 1:
                encoded_string += current_char
            current_char = char
            char_count = 1
        else:
            char_count += 1

    if char_count > 1:
        encoded_string += current_char + str(char_count)
    elif char_count == 1:
        encoded_string += current_char

    return encoded_string

input_string = input()
encoded_string = encode_string(input_string)

print(encoded_string)
