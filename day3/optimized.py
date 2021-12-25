def refactor_indata(indata):
    diagnostic_report = (*indata.split("\n"),)
    return diagnostic_report

def calc_a(diagnostic_report):
    bits_count = [0] * len(diagnostic_report[0])
    for binary in diagnostic_report:
        for i, bit in enumerate(binary):
            if bit == "1":
                bits_count[i] += 1
    gamma = 0
    epsilon = 0
    majority = len(diagnostic_report) / 2
    for bit_count in bits_count:
        gamma <<= 1
        epsilon <<= 1
        if bit_count > majority:
            gamma += 1
        else:
            epsilon += 1
    return gamma * epsilon

def calc_b(diagnostic_report):
    oxygen_list = diagnostic_report
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

    co2_list = diagnostic_report
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