#!/usr/bin/python3
for let in range(ord('z'), ord('a') - 1, -1):
    if let % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(let - diff)), end='')
