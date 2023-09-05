#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print("{:02d}, ".format(i), end='')
    else:
        print("{:02d}".format(i))

# Output will print numbers from 0 to 99 in the specified format.
