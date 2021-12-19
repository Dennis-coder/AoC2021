from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    hex_to_bin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }
    indata = "".join([hex_to_bin[x] for x in indata])
    return indata

def read_packet_a(indata, read_pos = 0):
    version_number = int(indata[read_pos:read_pos + 3], 2)
    read_pos += 3
    type_id = int(indata[read_pos:read_pos + 3], 2)
    read_pos += 3
    if type_id == 4:
        num = ""
        while indata[read_pos] == "1":
            num += indata[read_pos + 1:read_pos + 5]
            read_pos += 5
        num += indata[read_pos + 1:read_pos + 5]
        read_pos += 5
        num = int(num, 2)
        return version_number, read_pos
    else:
        length_type_id = int(indata[read_pos:read_pos + 1], 2)
        read_pos += 1
        if length_type_id:
            subpackets_amount = int(indata[read_pos:read_pos + 11], 2)
            read_pos += 11
            for _ in range(subpackets_amount):
                num, read_pos = read_packet_a(indata, read_pos)
                version_number += num
        else:
            subpackets_end_pos = int(indata[read_pos:read_pos + 15], 2) + read_pos + 15
            read_pos += 15
            while read_pos < subpackets_end_pos:
                num, read_pos = read_packet_a(indata, read_pos)
                version_number += num
        return version_number, read_pos

def calc_a(indata):
    sum_version_number, _ = read_packet_a(indata)
    return sum_version_number
    
def read_packet_b(indata, read_pos = 0):
    version_number = int(indata[read_pos:read_pos + 3], 2)
    read_pos += 3
    type_id = int(indata[read_pos:read_pos + 3], 2)
    read_pos += 3
    if type_id == 4:
        num = ""
        while indata[read_pos] == "1":
            num += indata[read_pos + 1:read_pos + 5]
            read_pos += 5
        num += indata[read_pos + 1:read_pos + 5]
        read_pos += 5
        num = int(num, 2)
        return num, read_pos
    else:
        length_type_id = int(indata[read_pos:read_pos + 1], 2)
        read_pos += 1
        nums = []
        if length_type_id:
            subpackets_amount = int(indata[read_pos:read_pos + 11], 2)
            read_pos += 11
            for _ in range(subpackets_amount):
                num, read_pos = read_packet_b(indata, read_pos)
                nums.append(num)
        else:
            subpackets_end_pos = int(indata[read_pos:read_pos + 15], 2) + read_pos + 15
            read_pos += 15
            while read_pos < subpackets_end_pos:
                num, read_pos = read_packet_b(indata, read_pos)
                nums.append(num)
        if type_id == 0:
            return sum(nums), read_pos
        if type_id == 1:
            prod = 1
            for num in nums:
                prod *= num
            return prod, read_pos
        if type_id == 2:
            return min(nums), read_pos
        if type_id == 3:
            return max(nums), read_pos
        if type_id == 5:
            return int(nums[0] > nums[1]), read_pos
        if type_id == 6:
            return int(nums[0] < nums[1]), read_pos
        if type_id == 7:
            return int(nums[0] == nums[1]), read_pos

def calc_b(indata):
    val, _ = read_packet_b(indata)
    return val

def main():
    total_start = perf_counter()
    indata = read_indata()
    refactor_start = perf_counter()
    indata = refactor_indata(indata)
    refactor_end = perf_counter()
    part1_start = perf_counter()
    a = calc_a(indata)
    part1_end = perf_counter()
    part2_start = perf_counter()
    b = calc_b(indata)
    part2_end = perf_counter()
    total_end = perf_counter()
    print(f"Refactoring time: {time_to_str(refactor_end - refactor_start)}")
    print(f"Part 1 calc time: {time_to_str(part1_end - part1_start)}")
    print(f"Part 2 calc time: {time_to_str(part2_end - part2_start)}")
    print(f"Total time:       {time_to_str(total_end - total_start)}")
    print(f"Answer part 1:    {a}")
    print(f"Answer part 2:    {b}")

def time_to_str(time):
    suffixes = {
        "s": 1,
        "ms": 0.001,
        "µs": 0.000001,
        "ns": 0.000000001,
    }
    for suffix in suffixes:
        if time > suffixes[suffix]:
            return f"{(time/suffixes[suffix]):.2f}" + suffix
    return f"{time}"

if __name__ == "__main__":
    main()