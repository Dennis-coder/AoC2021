from copy import deepcopy

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n")
    return indata

def calc_a(indata):
    bits_count = [0 for _ in range(len(indata[0]))]
    for binary in indata:
        for i, bit in enumerate(binary):
            if (bit) == "1":
                bits_count[i] += 1
    gamma = 0
    epsilon = 0
    for bit_count in bits_count:
        gamma *= 2
        epsilon *= 2
        if bit_count * 2 > len(indata):
            gamma += 1
        else:
            epsilon += 1
    return gamma * epsilon

def calc_b(indata):
    oxygen_list = deepcopy(indata)
    for i in range(len(oxygen_list[0])):
        bit_count = 0
        for binary in oxygen_list:
            if binary[i] == "1":
                bit_count += 1
        bit = ""
        if bit_count * 2 >= len(oxygen_list):
            bit += "1"
        else:
            bit += "0"
        oxygen_list = list(filter(lambda x: x[i] == bit, oxygen_list))
        if len(oxygen_list) == 1:
            break

    co2_list = deepcopy(indata)
    for i in range(len(co2_list[0])):
        bit_count = 0
        for binary in co2_list:
            if binary[i] == "1":
                bit_count += 1
        bit = ""
        if bit_count * 2 >= len(co2_list):
            bit += "0"
        else:
            bit += "1"
        co2_list = list(filter(lambda x: x[i] == bit, co2_list))
        if len(co2_list) == 1:
            break
    return int(oxygen_list[0], 2) * int(co2_list[0], 2)
    
def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    a = calc_a(indata)
    b = calc_b(indata)
    print(a,b)

if __name__ == "__main__":
    main()