
def solution1(input_text, preamble_len) :
    middle_out = input_text[:preamble_len] #Get first 20 inputs

    for n in range(len(input_text) - preamble_len) :
        valid = False
        x = int(input_text[n + preamble_len])
        for i in middle_out :
            for j in middle_out :
                if int(i) != int(j) :
                    #print(int(i),int(j))
                    if (int(i) + int(j)) == x :
                        valid = True
        
        if (valid == False):
            print(x)
        middle_out.pop(0)
        middle_out.append(input_text[n + preamble_len])


def solution2(input_text, flaw) : 

    for n in range(len(input_text)) :
        count = int(input_text[n])
        for y in range(n + 1,len(input_text), 1) :
            count += int(input_text[y])
            if count >= flaw :
                break
        if count == flaw :
            break

    if count != flaw :
        exit
    
    #print(count, int(input_text[n]), int(input_text[y]))

    arr = input_text[n:y+1]
    arr = [int(j) for j in arr]
    arr.sort()
    #print(arr)
    count = arr[0] + arr[-1]


    return count

with open("input.txt") as f:
    input_text = f.readlines()
print (solution1(input_text, 25))

with open("test.txt") as f:
    input_text = f.readlines()
print (solution1(input_text, 5))

with open("input.txt") as f:
    input_text = f.readlines()
print (solution2(input_text, 542529149))

with open("test.txt") as f:
    input_text = f.readlines()
print (solution2(input_text, 127))