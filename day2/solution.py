
def password_valid_counter(input_text) :
    count = 0
    for line in input_text :
        range_string, char, password = line.split()
        min, max = range_string.split('-')
        char = char.strip(':')
        if password.count(char) >= int(min) and password.count(char) <= int(max) :
            count += 1

    return count

def password_valid_counter_2(input_text) :
    count = 0
    for line in input_text :
        range_string, char, password = line.split()
        pos1, pos2 = range_string.split('-')
        pos1 = int(pos1) - 1 #Adjust for array indexing
        pos2 = int (pos2) - 1
        char = char.strip(':')
        if (password[pos1] == char) != (password[pos2] == char) :
            count += 1

    return count

with open("input.txt") as f:
    input_text = f.readlines()

print (password_valid_counter(input_text))

with open("test.txt") as f:
    input_text = f.readlines()

print (password_valid_counter(input_text))

with open("input.txt") as f:
    input_text = f.readlines()

print (password_valid_counter_2(input_text))

with open("test.txt") as f:
    input_text = f.readlines()

print (password_valid_counter_2(input_text))