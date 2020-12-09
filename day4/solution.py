
def solution1(input_text) :
    count = 0
    check = True
    important_headers = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for line in input_text :
        for header in important_headers :
            if line.count(header) == 0 :
                check = False
        if check :
            count += 1
        check = True


    return count

def check_years (year, min, max) :
    if int(year) >= min and int(year) <= max and len(year) == 4:
        return True
    return False

def check_height (height) :
    if height.endswith("in") == 1 and len(height) == 4:
        height = int(''.join(filter(str.isdigit, height)))
        if height >= 59 and height <= 76 :
            return True

    elif height.endswith("cm") == 1 and len(height) == 5:
        height = int(''.join(filter(str.isdigit, height)))
        if height >= 150 and height <= 193 :
            return True

    return False

def fun (letter) :
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if letter not in chars :
        return False
    return True

def check_hair (hair) :
    if (len(hair) == 7) and hair[0] == '#' and len(''.join(filter(fun, hair[1:]))) == 6 :
        return True
    return False

def check_eye (eye) :
    valid_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return eye in valid_color

def check_passport (pass_id):
    if len(pass_id) == 9 and pass_id.isdigit() :
        return True
    return False

def solution2(input_text) :
    count = 0
    check = True

    for line in input_text :
        pairs = line.split()
        num_inputs = 0
        for pair in pairs :
            header, value = pair.split(":")
            if header == "byr" :
                num_inputs += 1
                if not check_years(value, 1920, 2002): 
                    check = False
            elif header == "iyr" :
                num_inputs += 1
                if not check_years(value, 2010, 2020) :
                    check = False
            elif header == "eyr" :
                num_inputs += 1
                if not check_years(value, 2020, 2030) :
                    check = False
            elif header == "hgt" :
                num_inputs += 1
                if not check_height(value) :
                    check = False
            elif header == "hcl" :
                num_inputs += 1
                if not check_hair(value) :
                    check = False
            elif header == "ecl" :
                num_inputs += 1
                if not check_eye(value) :
                    check = False
            elif header == "pid" :
                num_inputs += 1
                if not check_passport(value) :
                    check = False
            elif header == "cid" :
                test = 1
            else :
                check = False
        if check and num_inputs == 7:
            count += 1
        check = True
        num_inputs = 0


    return count

with open("input.txt") as f:
    input_text = f.read().split("\n\n")
    input_text = [string.replace('\n', ' ') for string in input_text]
print (solution1(input_text))

with open("test.txt") as f:
    input_text = f.read().split("\n\n")
    input_text = [string.replace('\n', ' ') for string in input_text]
print (solution1(input_text))

with open("input.txt") as f:
    input_text = f.read().split("\n\n")
    input_text = [string.replace('\n', ' ') for string in input_text]
print (solution2(input_text))

with open("test.txt") as f:
    input_text = f.read().split("\n\n")
    input_text = [string.replace('\n', ' ') for string in input_text]
print (solution2(input_text))