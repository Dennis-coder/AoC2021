def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n\n")
    indata[1] = [x.split(" -> ") for x in indata[1].split("\n")]
    return indata

def recursion_a(pairs, a, b, count, depth=0, max_depth=10):
    if depth == max_depth:
        return a+b
    out = a
    new_val = pairs[a+b]
    if new_val in count:
        count[new_val] += 1
    else:
        count[new_val] = 1
    out += recursion_a(pairs, a, new_val, count, depth+1)[1:]
    out += recursion_a(pairs, new_val, b, count, depth+1)[1:]
    return out

def calcA(indata):
    start_val = indata[0]
    pairs = dict(indata[1])
    count = {}
    for char in start_val:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    out = start_val[0]
    for i in range(1, len(start_val)):
        out += recursion_a(pairs, start_val[i-1], start_val[i], count)[1:]
    
    most_common = max(count, key=count.get)
    least_common = min(count, key=count.get)
    
    print(count[most_common] - count[least_common])

def recursion_b(pairs, a, b, count, depth=0, max_depth=40):
    if depth == max_depth:
        return a+b
    out = a
    new_val = pairs[a+b]
    if new_val in count:
        count[new_val] += 1
    else:
        count[new_val] = 1
    out += recursion_b(pairs, a, new_val, count, depth+1)[1:]
    out += recursion_b(pairs, new_val, b, count, depth+1)[1:]
    return out

def calcB(indata):
    start_val = indata[0]
    pairs = dict(indata[1])
    count = {}
    for char in start_val:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    out = start_val[0]
    for i in range(1, len(start_val)):
        out += recursion_b(pairs, start_val[i-1], start_val[i], count)[1:]
    
    most_common = max(count, key=count.get)
    least_common = min(count, key=count.get)
    
    print(count[most_common] - count[least_common])

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    calcA(indata)
    calcB(indata)

if __name__ == "__main__":
    main()