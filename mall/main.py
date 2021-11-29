def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    # Do stuff
    return indata

def calc(indata):
    pass

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    outdata = calc(indata)
    print(outdata)

if __name__ == "__main__":
    main()