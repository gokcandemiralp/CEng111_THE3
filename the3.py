import copy
import sys
#reding the map
map_raw = open(sys.argv[1] ,"r")
map = map_raw.read()
lenght = int(map.find("\n"))
linemap = copy.deepcopy(list(map.replace("\n", "")))
height = int(len(linemap)/lenght)
#reading rules and generation
rules_raw = open(sys.argv[2] ,"r")
rules = rules_raw.read().replace("\n", "")
rlenght = int(len(rules) / 4)
gen = int(sys.argv[3])

#functions
def sayac(m, x, h):
    a = []
    c = 0
    if x*h == 1: #dot map
        return [0]
    elif x == 2  and h == 1: # 2 lenght map
        if m[1] == "*":
            a.append(1)
        if m[1] == "-":
            a.append(0)
        if m[0] == "*":
            a.append(1)
        if m[0] == "-":
            a.append(0)
        return a
    elif x == 1  and h == 2: # 2 height map
        if m[1] == "*":
            a.append(1)
        if m[1] == "-":
            a.append(0)
        if m[0] == "*":
            a.append(1)
        if m[0] == "-":
            a.append(0)
        return a
    elif x > 2  and h == 1: # 1 height long map
        for i in range(x):
            if i == 0:
                if m[1] == "*":
                    a.append(1)
                if m[1] == "-":
                    a.append(0)
            elif i == x-1:
                if m[-2] == "*":
                    a.append(1)
                if m[-2] == "-":
                    a.append(0)
            else:
                if m[i+1]=="*":
                    c+=1
                if m[i-1]=="*":
                    c+=1
                a.append(c)
                c=0
        return a
    elif h > 2  and x == 1: # 1 lenght high map
        for i in range(h):
            if i == 0:
                if m[1] == "*":
                    a.append(1)
                if m[1] == "-":
                    a.append(0)
            elif i == h-1:
                if m[-2] == "*":
                    a.append(1)
                if m[-2] == "-":
                    a.append(0)
            else:
                if m[i + 1] == "*":
                    c += 1
                if m[i - 1] == "*":
                    c += 1
                a.append(c)
                c=0
        return a
    for i in range(0, x*h):
        if i == 0:  # left upper corner
            for n in (i + 1, i + x + 1, i + x):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
        elif i == x - 1:  # right upper corner
            for n in (i - 1, i + x - 1, i + x):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
        elif i == x * (h - 1):  # left lower corner
            for n in (i - x, i - x + 1, i + 1):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
        elif i == (x * h) - 1:  # right lower corner
            for n in (i - 1, i - x - 1, i - x):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
        elif i < x - 1:  # upper edge
            for n in (i - 1, i + x - 1, i + x, i + x + 1, i + 1):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
        elif i % x == 0:  # left edge
            for n in (i - x, i - x + 1, i + 1, i + x + 1, i + x):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
        elif i % x == x - 1:  # right edge
            for n in (i - x, i - x - 1, i - 1, i + x - 1, i + x):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
        elif i > x * (h - 1):  # lower edge
            for n in (i - 1, i - x - 1, i - x, i - x + 1, i + 1):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
        else: #middle
            for n in (i - 1, i - x - 1, i - x, i - x + 1, i + 1, i + x + 1, i + x, i + x - 1):
                if m[n] == "*":
                    c += 1
            a.append(c)
            c = 0
    return a
def construct(m, x, h):
    a = []
    if x*h==1:
        return "".join(m)
    for i in range(0, h):
        a.append("".join(m[i * x:(i + 1) * x]))
    return "\n".join(a)
def rule():
    global linemap, lenght , gen , height
    while gen != 0:
        linemap2 = copy.deepcopy(linemap)
        c = sayac(linemap, lenght, height)
        for i in range(0, lenght * height ):
            for m in range(0, rlenght):
                r0 = rules[m * 4]
                r1 = rules[m * 4 + 1]
                r2 = rules[m * 4 + 2]
                r3 = rules[m * 4 + 3]
                if linemap[i] == "*" and r0 == "*":
                    if r1 == ">":
                        if c[i] > int(r2):
                            linemap2[i] = r3
                    if r1 == "<":
                        if c[i] < int(r2):
                            linemap2[i] = r3
                    if r1 == "=":
                        if c[i] == int(r2):
                            linemap2[i] = r3
                if linemap[i] == "-" and r0 == "-":
                    if r1 == ">":
                        if c[i] > int(r2):
                            linemap2[i] = r3
                    if r1 == "<":
                        if c[i] < int(r2):
                            linemap2[i] = r3
                    if r1 == "=":
                        if c[i] == int(r2):
                            linemap2[i] = r3
        gen -= 1
        linemap = linemap2
    return construct(linemap, lenght , height)

print rule()