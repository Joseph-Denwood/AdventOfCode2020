
def solution1(input_text) :
    count = 0
    location = 0
    repeat = False
    seen_locations = []
    
    while repeat == False :
        if location not in seen_locations :
            seen_locations.append(location)
            inst, offset = input_text[location].split(" ")
            #print(inst, offset, int(offset))
            
            if (inst == "acc") :
                count += int(offset)
                location += 1
            elif (inst == "nop") :
                location += 1
            elif (inst == "jmp") :
                location += int(offset)
        else :
            repeat = True

    return count

def find_loop (input_text, location, seen_so_far, acc_so_far) :
    count = acc_so_far
    repeat = False
    seen_locations = seen_so_far

    while repeat == False :
        if location >= len(input_text) :
            print (count)
            return True, seen_locations, count 
        if location not in seen_locations :
            seen_locations.append(location)
            inst, offset = input_text[location].split(" ")
            #print(inst, offset, int(offset))
            
            if (inst == "acc") :
                count += int(offset)
                location += 1
            elif (inst == "nop") :
                location += 1
            elif (inst == "jmp") :
                location += int(offset)
        else :
            repeat = True
    #print(count)
    return False, seen_locations, count 

def solution2(input_text) :
    count = 0
    location = 0
    repeat = False
    seen_locations = []
    null, seen_locations, count = find_loop(input_text, 0, [], 0)

    #found repeat, now work backwards & swap last nop/jmp, then work forward until loop or end
    seen_locations.reverse()
    n = 0
    for loc in seen_locations :
        inst, offset = input_text[loc].split(" ")
        if inst == "acc" :
            count -= int(offset)
        elif inst == "nop" :
            test, null, null = find_loop(input_text, loc + int(offset), seen_locations[n:], count)
            if  test:
                break
        elif inst == "jmp" :
            test, null, null = find_loop(input_text, loc + 1, seen_locations[n:], count)
            if  test:
                break
        n += 1

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