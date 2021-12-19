def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    return indata

def calc_a(indata):
    pass

def calc_b(indata):
    pass

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    a = calc_a(indata)
    b = calc_b(indata)
    print(a,b)

if __name__ == "__main__":
    main()