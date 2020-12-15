
def solution1(input_text) :
    inputs = input_text[0].split(",")
    num = 0
    dict_ = {}
    count = 0
    for i in inputs :
        dict_.update({int(i) : count})
        num = int(i)
        count += 1
    for i in range(count, 30000000) :
        #print(num, dict_.get(num))
        next_num = 0
        if num in dict_ :
            next_num = i - 1 - dict_.get(num)
        dict_.update({num : i - 1})
        num = next_num
    #print(dict_)



    return num

def solution2(input_text) :
    count = 0

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
#print (solution2(input_text))
