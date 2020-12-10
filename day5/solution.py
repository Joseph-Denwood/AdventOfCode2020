
def solution1(input_text) :
    count = 0
    max_num = 0
    y = input_text[0][0:7]
    x = input_text[0][7:10]
    #print(y, x)

    for line in input_text :
        y = line[0:7]
        x = line[7:10]
        min = 0
        max = 127
        inc = 1
        for i in y[:-1]:
            if (i == "B") :
                min += 128 / (2 ** inc)
            else :
                max -= 128 / (2 ** inc)
            inc += 1
        #print (min, max, inc)
        if (y[-1] == 'B'):
            count = max * 8
        else :
            count = min * 8
        #print(count)
        
        min = 0
        max = 7
        inc = 1
        for i in x[:-1] :
            if (i == "R") :
                min += 8 / (2 ** inc)
            else :
                max -= 8 / (2 ** inc)
            inc += 1
        #print (min, max, inc)
        if (x[-1] == 'R'):
            count += max
        else :
            count += min
        if (count > max_num) :
            max_num = count




    return max_num

def solution2(input_text) :
    count = 0
    max_num = 0
    y = input_text[0][0:7]
    x = input_text[0][7:10]
    arr = []
    #print(y, x)

    for line in input_text :
        y = line[0:7]
        x = line[7:10]
        min = 0
        max = 127
        inc = 1
        for i in y[:-1]:
            if (i == "B") :
                min += 128 / (2 ** inc)
            else :
                max -= 128 / (2 ** inc)
            inc += 1
        #print (min, max, inc)
        if (y[-1] == 'B'):
            count = max * 8
        else :
            count = min * 8
        #print(count)
        
        min = 0
        max = 7
        inc = 1
        for i in x[:-1] :
            if (i == "R") :
                min += 8 / (2 ** inc)
            else :
                max -= 8 / (2 ** inc)
            inc += 1
        #print (min, max, inc)
        if (x[-1] == 'R'):
            count += max
        else :
            count += min
        arr.append(count)

    arr.sort()
    #print (arr[0:20])
    n = arr[0]
    for i in arr[1:] :
        if i != n + 1 :
            print(i, n)
            return i - 1
        n = i


    return max_num

with open("input.txt") as f:
    input_text = f.readlines()
print (solution1(input_text))

with open("test.txt") as f:
    input_text = f.readlines()
print (solution1(input_text))

with open("input.txt") as f:
    input_text = f.readlines()
print (solution2(input_text))

with open("test.txt") as f:
    input_text = f.readlines()
print (solution2(input_text))