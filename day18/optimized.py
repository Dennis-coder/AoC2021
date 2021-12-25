from math import ceil, floor
from copy import deepcopy

def parse_num(num, i = 0):
    parsed_num = []
    cur_num = ""
    while i < len(num):
        char = num[i]
        i += 1
        if char == "[":
            a_num, i = parse_num(num, i)
            parsed_num.append(a_num)
        elif char == "]":
            if cur_num.isnumeric():
                parsed_num.append(int(cur_num))
            return parsed_num, i
        elif char == ",":
            if cur_num.isnumeric():
                parsed_num.append(int(cur_num))
            cur_num = ""
        elif char.isnumeric():
            cur_num += char
    return parsed_num

def refactor_indata(indata):
    indata = [parse_num(x)[0] for x in indata.split("\n")]
    return indata

def is_pair(num):
    if not isinstance(num, list):
        return False
    if len(num) != 2:
        return False
    if not (isinstance(num[0], int) and isinstance(num[1], int)):
        return False
    return True

def _explode_num(num, data):
    for i in range(len(num)):
        if data["has_reduced"]:
            break
        
        elif data["is_reducing"] and isinstance(num[i], int):
            num[i] += data["num_to_add"]
            data["is_reducing"] = False
            data["has_reduced"] = True
            break

        elif data["is_reducing"] and isinstance(num[i], list):
            _explode_num(num[i], data)
            
        elif data["is_reducing"]:
            continue

        elif isinstance(num[i], int):
            data["prev_num"] = num
            data["prev_num_i"] = i

        elif is_pair(num[i]) and data["depth"] >= 4:
            if data["prev_num"]:
                data["prev_num"][data["prev_num_i"]] += num[i][0]
            data["num_to_add"] = num[i][1]
            data["is_reducing"] = True
            num[i] = 0

        elif isinstance(num[i], list):
            data["depth"] += 1
            _explode_num(num[i], data)

    data["depth"] -= 1

def _split_num(num, data):
    for i in range(len(num)):
        if data["has_reduced"]:
            break

        elif isinstance(num[i], int) and num[i] >= 10:
            num[i] = [floor(num[i] / 2), ceil(num[i] / 2)]
            data["has_reduced"] = True
            break

        elif isinstance(num[i], list):
            _split_num(num[i], data)

def calc_magnitude(num):
    if isinstance(num, int):
        return num
    return 3 * calc_magnitude(num[0]) + 2 * calc_magnitude(num[1])

def reduce_num(num):
    while True:
        data = {
            "is_reducing": False,
            "has_reduced": False,
            "depth": 1,
            "prev_num": None
        }
        _explode_num(num, data)
        _split_num(num, data)
        if not (data["has_reduced"] or data["is_reducing"]):
            break
    return num

def calc_a(indata):
    num = reduce_num(indata[0])
    for i in range(1, len(indata)):
        num = reduce_num([num, indata[i]])
    return calc_magnitude(num)

def calc_b(indata):
    highest_magnitude = 0
    for i in range(len(indata)):
        for j in range(len(indata)):
            if i == j:
                continue
            num = reduce_num([deepcopy(indata[i]), deepcopy(indata[j])])
            magnitude = calc_magnitude(num)
            if magnitude > highest_magnitude:
                highest_magnitude = magnitude
    return highest_magnitude