
def solution1(input_text) :
    count_1 = 0
    count_3 = 0
    arr = [int(i) for i in input_text]
    arr.sort()
    last = 0
    #print(arr)
    for i in arr :
        if (i - last == 3) :
            count_3 += 1
        elif (i - last == 1) :
            count_1 += 1
        last = i
    #print(count_1, count_3)
    count_3 += 1

    return count_1 * count_3   

def solution2(input_text) :
    count = 0

    arr = [int(i) for i in input_text]
    arr.sort()
    print(arr)
    dict_ = {0 : 1}
    for n in arr :
        count = 0
        if n - 1 in dict_ :
            count += dict_.get(n-1)
        if n - 2 in dict_ :
            count += dict_.get(n-2)
        if n - 3 in dict_ :
            count += dict_.get(n-3)
        #print (n, count)
        dict_.update({n : count})





    return count

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