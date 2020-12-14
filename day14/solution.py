import copy

def solution1(input_text) :
    count = 0
    dict_ = {}
    add = 0
    sub = 0

    for line in input_text :
        inst, value = line.strip().strip(" ").split("=")
        inst = inst.strip()
        value = value.strip()
        #print(inst, value)
        #print(inst)
        if inst == "mask" :
            count = 0
            add = 0
            sub = 0
            #print("test")
            for char in value[ : :-1] :
                #print(char)
                if char == "1" :
                    add += 2 ** count
                if char == "0" :
                    sub += 2 ** count
                count += 1
        if inst[0:3] == "mem" :
            value = int(value)
            key = inst[3:-1].strip("]").strip("[")
            value = value | add
            value = value & ~sub
            dict_.update({key : value})

        #print(dict_, add, sub)

    count = 0
    for i in dict_.keys():
        count += dict_.get(i)
            

    return count

def solution2(input_text) :
    count = 0

    count = 0
    dict_ = {}
    add = 0
    sub = 0
    x = []

    for line in input_text :
        inst, value = line.strip().strip(" ").split("=")
        inst = inst.strip()
        value = value.strip()
        #print(inst, value)
        #print(inst)
        if inst == "mask" :
            count = 0
            add = 0
            sub = 0
            x = []
            #print("test")
            for char in value[ : :-1] :
                #print(char)
                if char == "1" :
                    add += 2 ** count
                if char == "0" :
                    sub += 2 ** count
                if char == "X" :
                    x.append(count)
                count += 1

        if inst[0:3] == "mem" :
            value = int(value)
            key = int(inst[3:-1].strip("]").strip("["))
            key = key | add
            #key = key & ~sub
            key = str('{0:36b}'.format(key))
            #print(int(inst[3:-1].strip("]").strip("[")), key, add, sub)
            key = list(key)
            key.reverse()
            arr_ = [key]
            for i in x :
                hold_arr = []
                for j in arr_ :
                    j[i] = "1"
                    hold_arr.append(copy.deepcopy(j))
                    j[i] = "0"
                    hold_arr.append(copy.deepcopy(j))
                arr_ = hold_arr
                #key[i] = "X"
            #key = str(key)
            #print(arr_)
            for i in arr_ :
                #print(str(i))
                dict_.update({str(i).replace(' ', '0') : value})

    #print(dict_, add, sub)

    count = 0
    for i in dict_.keys():
        inc = i.count('X')
        count += (2 ** inc) * dict_.get(i)


    return count

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
