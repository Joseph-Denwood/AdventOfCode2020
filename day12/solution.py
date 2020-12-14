
def solution1(input_text) :
    x = 0
    y = 0
    direction = 90

    for line in input_text :
        instruction = line[0]
        distance = int(line[1:])
        if (instruction == 'N') :
            y += distance
        if (instruction == 'S') :
            y -= distance
        if (instruction == 'E') :
            x += distance
        if (instruction == 'W') :
            x -= distance
        if (instruction == 'L') :
            direction = (direction - distance) % 360
        if (instruction == 'R') :
            direction = (direction + distance) % 360
        if (instruction == 'F') :
            if direction == 0 :
                y += distance
            elif direction == 180 :
                y -= distance
            elif direction == 90 :
                x += distance
            elif direction == 270 :
                x -= distance
            else :
                print(line)
        #print(x, y)


    return abs(x) + abs(y)

def solution2(input_text) :
    x = 0
    y = 0
    way_x = 10
    way_y = 1
    direction = 90

    for line in input_text :
        instruction = line[0]
        distance = int(line[1:])
        if (instruction == 'N') :
            way_y += distance
        if (instruction == 'S') :
            way_y -= distance
        if (instruction == 'E') :
            way_x += distance
        if (instruction == 'W') :
            way_x -= distance
        if (instruction == 'L') :
            hold_x = way_x
            hold_y = way_y
            if (distance%360) == 90 :
                way_x = -hold_y
                way_y = hold_x
            if (distance%360) == 180 :
                way_x = -hold_x
                way_y = -hold_y
            if (distance%360) == 270 :
                way_x = hold_y
                way_y = -hold_x
        if (instruction == 'R') :
            hold_x = way_x
            hold_y = way_y
            if (distance%360) == 90 :
                way_x = hold_y
                way_y = -hold_x
            if (distance%360) == 180 :
                way_x = -hold_x
                way_y = -hold_y
            if (distance%360) == 270 :
                way_x = -hold_y
                way_y = hold_x
        if (instruction == 'F') :
            x += way_x * distance
            y += way_y * distance
        #print(x, y)


    return abs(x) + abs(y)


with open("test.txt") as f:
    input_text = f.readlines()
print (solution1(input_text))

with open("input.txt") as f:
    input_text = f.readlines()
print (solution1(input_text))

with open("test.txt") as f:
    input_text = f.readlines()
print (solution2(input_text))

with open("input.txt") as f:
    input_text = f.readlines()
print (solution2(input_text))
