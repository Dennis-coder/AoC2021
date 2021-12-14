import math

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in indata.split("\n")]
    return indata

def calcA(indata):
    count_dict = {}
    for line in indata:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            continue
        if line[0][0] == line[1][0]:
            x = line[0][0]
            it = range(line[0][1], line[1][1] + 1) if line[0][1] < line[1][1] else range(line[1][1], line[0][1] + 1)
            for y in it:
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1
        elif line[0][1] == line[1][1]:
            y = line[0][1]
            it = range(line[0][0], line[1][0] + 1) if line[0][0] < line[1][0] else range(line[1][0], line[0][0] + 1)
            for x in it:
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1
    count = 0
    for key in count_dict.keys():
        if count_dict[key] > 1:
            count += 1
    return count

def calcB(indata):
    count_dict = {}
    for line in indata:
        if line[0][0] == line[1][0]:
            x = line[0][0]
            it = range(line[0][1], line[1][1] + 1) if line[0][1] < line[1][1] else range(line[1][1], line[0][1] + 1)
            for y in it:
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1
        elif line[0][1] == line[1][1]:
            y = line[0][1]
            it = range(line[0][0], line[1][0] + 1) if line[0][0] < line[1][0] else range(line[1][0], line[0][0] + 1)
            for x in it:
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1
        else:
            for i in range(abs(line[0][0] - line[1][0]) + 1):
                x = line[0][0] + i if line[0][0] < line[1][0] else line[0][0] - i
                y = line[0][1] + i if line[0][1] < line[1][1] else line[0][1] - i
                if f"{x},{y}" in count_dict:
                    count_dict[f"{x},{y}"] += 1
                else:
                    count_dict[f"{x},{y}"] = 1

    count = 0
    for key in count_dict.keys():
        if count_dict[key] > 1:
            count += 1
    return count

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    a = calcA(indata)
    b = calcB(indata)
    print(a,b)

if __name__ == "__main__":
    main()