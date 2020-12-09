
def recurse_dict (value, bag_dict, already_counted) :
    if value not in already_counted :
        count = 1
        already_counted.append(value)
    else :
        count = 0
    if value not in bag_dict :
        return already_counted, count
    arr = bag_dict.get(value)
    for i in arr :
        already_counted, num = recurse_dict(i, bag_dict, already_counted)
        count += num
    return already_counted, count

def solution1(input_text) :
    dict_bags = {}
    for line in input_text :
        outer_bag, inner_bags = line.split("contain")
        outer_bag = ''.join([i for i in outer_bag if i.isalpha() or i == ' '])
        inner_bags = ''.join([i for i in inner_bags if i.isalpha() or i == ',' or i == ' '])
        inner_bags = inner_bags.replace("bags", "")
        inner_bags = inner_bags.replace("bag", "")
        outer_bag = outer_bag.replace("bags", "")
        outer_bag = outer_bag.replace("bag", "")
        outer_bag = outer_bag.strip()
        inner_bags = inner_bags.split(",")
        #print (outer_bag, inner_bags)
        for bag in inner_bags :
            bag = bag.strip()
            if bag != "no other" :
                if bag in dict_bags :
                    arr = dict_bags.get(bag)
                    arr.append(outer_bag)
                    dict_bags[bag] = arr
                else :
                    dict_bags[bag] = [outer_bag]

    null, count = recurse_dict("shiny gold", dict_bags, ["shiny gold"])
    return count

def recurse_dict_2 (value, bag_dict) :
    count = 1

    if value not in bag_dict :
        return count
    arr = bag_dict.get(value)
    for i in arr :
        #print (value,i, recurse_dict_2(i[1], bag_dict), recurse_dict_2(i[1], bag_dict) * int(i[0]))
        count += recurse_dict_2(i[1], bag_dict) * int(i[0])
    return count

def solution2(input_text) :
    dict_bags = {}
    for line in input_text :
        outer_bag, inner_bags = line.split("contain")
        outer_bag = ''.join([i for i in outer_bag if i.isalpha() or i == ' '])
        inner_bags = ''.join([i for i in inner_bags if i.isalnum() or i == ',' or i == ' '])
        inner_bags = inner_bags.replace("bags", "")
        inner_bags = inner_bags.replace("bag", "")
        outer_bag = outer_bag.replace("bags", "")
        outer_bag = outer_bag.replace("bag", "")
        outer_bag = outer_bag.strip()
        inner_bags = inner_bags.strip()
        inner_bags = inner_bags.split(",")
        #print (outer_bag, inner_bags)

        arr = [n.split() for n in inner_bags]
        for n in arr :
            if n[0] != "no" :
                if outer_bag in dict_bags:
                    arr = dict_bags[outer_bag]
                    arr.append((n[0], n[1] + ' ' + n[2]))
                    dict_bags.update({outer_bag : arr})
                else :
                    dict_bags[outer_bag] = [(n[0], n[1] + ' ' + n[2])]
    

    return recurse_dict_2("shiny gold", dict_bags) - 1

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