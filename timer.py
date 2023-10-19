import sys
import math
import matplotlib.pyplot as plt
import string
import time
link = []
escape = 2
blink = []
bamboo = lambda boobs: math.ceil(math.comb(ord(boobs), f))
for char in str(str(sys.argv[1]).islower()):
    blink.append(char)
f = 97

link =  []
for char in string.ascii_lowercase:
    link.append(char)


for char in blink:
    while escape != 1:
        enc = ""
        for boop in range(len(link)):
            f = ord(link[boop]) - ord(link[math.ceil(time.time()) % len(link)])
            if f < 0 :
                f = f * -1
            f += 97
            enc += chr(f)
        link = []
        for boo in enc:
            link.append(boo) 
        escape = len(link)
        print(r''.join(link), end="\r")
        if ''.join(link) == char:
            print(''.join(link), end="\r")



