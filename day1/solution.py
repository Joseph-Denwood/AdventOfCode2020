import sys

print('Length of input array:', len(sys.argv))
print('Input is: ', sys.argv)

f = open(sys.argv[1], "r")
arr = [0] * 2021
for x in f:
    y = int(x)
    if (arr[y] != 0) :
        print (y * (2020 - y))
    else :
        arr[2020 - y] = 1;
