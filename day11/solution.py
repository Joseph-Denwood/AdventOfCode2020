import copy

def check_switch_L(x_len, y_len, x, y, arr) :
    if x != x_len - 1 and arr[x+1][y] == '#' :
        return False
    if x != 0 and arr[x-1][y] == '#' :
        return False
    if y != y_len - 1 and arr[x][y+1] == '#' :
        return False
    if y != 0 and arr[x][y-1] == '#' :
        return False

    if x != x_len - 1 and y != y_len - 1 and arr[x+1][y+1] == '#' :
        return False
    if x != x_len - 1 and y != 0 and arr[x+1][y-1] == '#' :
        return False
    if x != 0 and y != y_len - 1 and arr[x-1][y+1] == '#' :
        return False
    if x != 0 and y != 0 and arr[x-1][y-1] == '#' :
        return False

    return True

def check_switch_other(x_len, y_len, x, y, arr) :
    count = 0
    if x != x_len - 1 and arr[x+1][y] == '#' :
        count += 1
    if x != x_len - 1 and y != y_len - 1 and arr[x+1][y+1] == '#' :
        count += 1
    if x != x_len - 1 and y != 0 and arr[x+1][y-1] == '#' :
        count += 1
    if x != 0 and arr[x-1][y] == '#' :
        count += 1
    if x != 0 and y != y_len - 1 and arr[x-1][y+1] == '#' :
        count += 1
    if x != 0 and y != 0 and arr[x-1][y-1] == '#' :
        count += 1
    if y != y_len - 1 and arr[x][y+1] == '#' :
        count += 1
    if y != 0 and arr[x][y-1] == '#' :
        count += 1
    
    return count >= 4

def solution1(input_text) :
    count = 0
    arr = []
    loop = True
    for line in input_text :
        arr.append([i for i in line.strip()])
    x_len = len(arr)
    y_len = len(arr[0])
    arr_old = copy.deepcopy(arr)


    while loop == True :
        for x in range(len(arr)) :
            for y in range(len(arr[0])) :
                if arr[x][y] == 'L' and check_switch_L(x_len, y_len, x, y, arr_old) :
                    arr[x][y] = '#'
                elif arr[x][y] == '#' and check_switch_other(x_len, y_len, x, y, arr_old) :
                    arr[x][y] = 'L'

        if arr == arr_old :
            loop = False
        else :
            arr_old = copy.deepcopy(arr)

    for x in range(len(arr)) :
        for y in range(len(arr[0])) :
            if arr[x][y] == '#' :
                count += 1

    return count

def check_switch_L_2(x_len, y_len, x, y, arr) :
    options = [-1, 0, 1]
    keep_going = True
    x_hold = x
    y_hold = y

    for x_var in options :
        for y_var in options :
            x = x_hold
            y = y_hold
            if x_var == 0 and y_var == 0 : 
                #to nothing
                keep_going = True
            else :
                while keep_going :
                    x += x_var
                    y += y_var
                    if x != x_len and x >= 0 and y != y_len and y >= 0 :
                        if arr[x][y] != '.' :
                            keep_going = False
                        if arr[x][y] == '#' :
                            return False
                    else :
                        keep_going = False
                keep_going = True

    return True

def check_switch_other_2(x_len, y_len, x, y, arr) :
    count = 0
    options = [-1, 0, 1]
    keep_going = True
    x_hold = x
    y_hold = y

    for x_var in options :
        for y_var in options :
            x = x_hold
            y = y_hold
            if x_var == 0 and y_var == 0 : 
                count += 0
            else :
                while keep_going :
                    x += x_var
                    y += y_var
                    if x != x_len and x >= 0 and y != y_len and y >= 0 :
                        if arr[x][y] != '.' :
                            keep_going = False
                        if arr[x][y] == '#' :
                            count += 1
                    else :
                        keep_going = False
            keep_going = True
    return count >= 5

def solution2(input_text) :
    count = 0
    arr = []
    loop = True
    for line in input_text :
        arr.append([i for i in line.strip()])
    x_len = len(arr)
    y_len = len(arr[0])
    arr_old = copy.deepcopy(arr)


    while loop == True :
        for x in range(len(arr)) :
            for y in range(len(arr[0])) :
                if arr[x][y] == 'L' and check_switch_L_2(x_len, y_len, x, y, arr_old) :
                    arr[x][y] = '#'
                elif arr[x][y] == '#' and check_switch_other_2(x_len, y_len, x, y, arr_old) :
                    arr[x][y] = 'L'

        if arr == arr_old :
            loop = False
        else :
            arr_old = copy.deepcopy(arr)
    
    for i in arr:
        print(i)
    print()

    for x in range(len(arr)) :
        for y in range(len(arr[0])) :
            if arr[x][y] == '#' :
                count += 1

    return count

with open("test.txt") as f:
    input_text = f.readlines()
print (solution1(input_text))

with open("input.txt") as f:
    input_text = f.readlines()
#print (solution1(input_text))

with open("test.txt") as f:
    input_text = f.readlines()
print (solution2(input_text))

with open("input.txt") as f:
    input_text = f.readlines()
print (solution2(input_text))
