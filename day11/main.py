from copy import deepcopy

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[int(x) for x in y] for y in indata.split("\n")]
    return indata

def flash(point, flash_indexes, indata):
    (x, y) = point
    flash_indexes.append((x,y))
    neighbours = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    for n in neighbours:
        x2, y2 = x + n[0], y + n[1]
        if x2 < 0 or x2 == len(indata[0]) or y2 < 0 or y2 == len(indata):
            continue
        indata[y2][x2] += 1
        if indata[y2][x2] > 9 and (x2,y2) not in flash_indexes:
            flash([x2, y2], flash_indexes, indata)

def calcA(indata):
    count_flashes = 0
    for _ in range(100):
        flash_indexes = []
        for y in range(len(indata)):
            for x in range(len(indata[0])):
                indata[y][x] += 1
                if indata[y][x] > 9 and (x,y) not in flash_indexes:
                    flash([x, y], flash_indexes, indata)
        count_flashes += len(flash_indexes)
        for (x,y) in flash_indexes:
            indata[y][x] = 0
    print(count_flashes)

def calcB(indata):
    i = 1
    while True:
        flash_indexes = []
        for y in range(len(indata)):
            for x in range(len(indata[0])):
                indata[y][x] += 1
                if indata[y][x] > 9 and (x,y) not in flash_indexes:
                    flash([x, y], flash_indexes, indata)
        for (x,y) in flash_indexes:
            indata[y][x] = 0
        if len(flash_indexes) == len(indata) * len(indata[0]):
            break
        i += 1
    print(i)

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    calcA(deepcopy(indata))
    calcB(indata)

if __name__ == "__main__":
    main()