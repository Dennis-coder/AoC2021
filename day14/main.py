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
    new_val = pairs[a+b]
    if new_val in count:
        count[new_val] += 1
    else:
        count[new_val] = 1
    recursion_a(pairs, a, new_val, count, depth+1)
    recursion_a(pairs, new_val, b, count, depth+1)

def calcA(indata):
    start_val = indata[0]
    pairs = dict(indata[1])

    count = {}
    for char in start_val:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            
    for i in range(1, len(start_val)):
        recursion_a(pairs, start_val[i-1], start_val[i], count)
    
    most_common = max(count, key=count.get)
    least_common = min(count, key=count.get)
    print(count[most_common] - count[least_common])

def calcB(indata):
    start_val = indata[0]
    new_val = dict(indata[1])
    pairs = dict([[x[0], [x[0][0] + x[1], x[1] + x[0][1]]] for x in indata[1]])

    count_pairs = {}
    for i in range(len(start_val) - 1):
        pair = start_val[i] + start_val[i+1]
        if pair in count_pairs:
            count_pairs[pair] += 1
        else:
            count_pairs[pair] = 1

    count = {}
    for char in start_val:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for _ in range(40):
        new_count_pairs = {}
        for pair in count_pairs.keys():
            if new_val[pair] in count:
                count[new_val[pair]] += count_pairs[pair]
            else:
                count[new_val[pair]] = 1
            for new_pair in pairs[pair]:
                if new_pair in new_count_pairs:
                    new_count_pairs[new_pair] += count_pairs[pair]
                else:
                    new_count_pairs[new_pair] = count_pairs[pair]
        count_pairs = new_count_pairs

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