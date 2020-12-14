
def solution1(input_text) :
    time = int(input_text[0])
    arr_t = input_text[1].split(',')
    arr = []
    for i in arr_t :
        if i.isnumeric() :
            arr.append(int(i))
    #print(arr)
    exit_arr = {}

    for i in arr :
        #Want to get value - value%time, which will give us time after 
        exit_arr.update({i - time%i : i})
    #print(exit_arr)
    x = min(exit_arr.keys())


    return x * exit_arr.get(x)

#Shamelessly stolen from: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 


def solution2(input_text) :
    count = 0
    arr_t = input_text[1].strip().split(',')
    off_arr = []
    val_arr = []
    for i in arr_t:
        if i.isnumeric():
            off_arr.append(-1 * count)
            val_arr.append(int(i))
            #dict_.update({int(i) : count})
        count += 1
    #print(val_arr, off_arr)
    
    #I need a number that is i - number%i = dict_.get(i) 
    #worst case: Loop through all multiples of arr_t[0], check if they hold above true
    # Due to this being based on remainder, can't use a search algorithm to reduce search time
    # Based on the hint, even the largest interval isn't usable - over 100 billion options would need to be tried
    


    return chinese_remainder(val_arr, off_arr)


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
