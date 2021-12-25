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
    transmission = "".join([hex_to_bin[x] for x in indata])
    return transmission

def read_packet_a(transmission, read_pos = 0):
    version_number = int(transmission[read_pos:read_pos + 3], 2)
    read_pos += 3
    type_id = int(transmission[read_pos:read_pos + 3], 2)
    read_pos += 3
    if type_id == 4:
        num = ""
        while transmission[read_pos] == "1":
            num += transmission[read_pos + 1:read_pos + 5]
            read_pos += 5
        num += transmission[read_pos + 1:read_pos + 5]
        read_pos += 5
        num = int(num, 2)
        return version_number, read_pos
    else:
        length_type_id = int(transmission[read_pos:read_pos + 1], 2)
        read_pos += 1
        if length_type_id:
            subpackets_amount = int(transmission[read_pos:read_pos + 11], 2)
            read_pos += 11
            for _ in range(subpackets_amount):
                num, read_pos = read_packet_a(transmission, read_pos)
                version_number += num
        else:
            subpackets_end_pos = int(transmission[read_pos:read_pos + 15], 2) + read_pos + 15
            read_pos += 15
            while read_pos < subpackets_end_pos:
                num, read_pos = read_packet_a(transmission, read_pos)
                version_number += num
        return version_number, read_pos

def calc_a(transmission):
    sum_version_number, _ = read_packet_a(transmission)
    return sum_version_number
    
def read_packet_b(transmission, read_pos = 0):
    read_pos += 3
    type_id = int(transmission[read_pos:read_pos + 3], 2)
    read_pos += 3
    if type_id == 4:
        num = ""
        while transmission[read_pos] == "1":
            num += transmission[read_pos + 1:read_pos + 5]
            read_pos += 5
        num += transmission[read_pos + 1:read_pos + 5]
        read_pos += 5
        num = int(num, 2)
        return num, read_pos
    else:
        length_type_id = int(transmission[read_pos:read_pos + 1], 2)
        read_pos += 1
        nums = []
        if length_type_id:
            subpackets_amount = int(transmission[read_pos:read_pos + 11], 2)
            read_pos += 11
            for _ in range(subpackets_amount):
                num, read_pos = read_packet_b(transmission, read_pos)
                nums.append(num)
        else:
            subpackets_end_pos = int(transmission[read_pos:read_pos + 15], 2) + read_pos + 15
            read_pos += 15
            while read_pos < subpackets_end_pos:
                num, read_pos = read_packet_b(transmission, read_pos)
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

def calc_b(transmission):
    val, _ = read_packet_b(transmission)
    return val