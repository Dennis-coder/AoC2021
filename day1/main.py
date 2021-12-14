def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n")
    indata = [int(x) for x in indata]
    return indata

def calcA(reports):
    higher = 0
    for i in range(1, len(reports)):
        if reports[i] > reports[i-1]:
            higher += 1
    return higher

def calcB(reports):
    higher = 0
    for i in range(3, len(reports)):
        if reports[i] + reports[i-1] + reports[i-2] > reports[i-1] + reports[i-2] + reports[i-3]:
            higher += 1
    return higher

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    a = calcA(indata)
    b = calcB(indata)
    print(a,b)


if __name__ == "__main__":
    main()