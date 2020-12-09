
def solution1(input_text, right_increment, down_increment) :
    count = 0
    x = 0
    y = 0
    line_width = 0 #Should be 32

    for line in input_text :
        if (y % down_increment == 0) :
            line_width = len(line) - 1
            if (line[x % line_width] == '#') :
                count += 1
            x += right_increment
        y += 1

    return count




def solution2(input_text) :
    count = solution1(input_text, 1, 1)
    count *= solution1(input_text, 3, 1)
    count *= solution1(input_text, 5, 1)
    count *= solution1(input_text, 7, 1)
    count *= solution1(input_text, 1, 2)

    return count

with open("input.txt") as f:
    input_text = f.readlines()
print (solution1(input_text, 3, 1))

with open("test.txt") as f:
    input_text = f.readlines()
print (solution1(input_text, 3, 1))

with open("input.txt") as f:
    input_text = f.readlines()
print (solution2(input_text))

with open("test.txt") as f:
    input_text = f.readlines()
print (solution2(input_text))