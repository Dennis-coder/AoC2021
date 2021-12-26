from math import ceil, floor
from ast import literal_eval
from re import findall, finditer, search
from sre_constants import RANGE_UNI_IGNORE

def refactor_indata(indata):
    numbers = (*indata.split("\n"),)
    return numbers

def pair(x, y):
    return f"[{x},{y}]"

def explode(num):
    for pair in finditer(r'\[\d+,\d+\]', num):
        p_start = pair.start()
        p_end = pair.end()
        before = num[:p_start]
        if before.count('[') - before.count(']') >= 4:
            l_num, r_num = [int(x) for x in findall(r"\d+", num[p_start:p_end])]
            
            r_string = num[p_end:]
            next_num_r = search(r'\d+', r_string)
            if next_num_r:
                r_start = next_num_r.start()
                r_end = next_num_r.end()
                r_string = r_string[:r_start] + str(r_num + int(r_string[r_start:r_end])) + r_string[r_end:]

            l_string = num[:p_start]
            next_num_l = search(r'\d+', l_string[::-1])
            if next_num_l:
                l_start = p_start - next_num_l.end()
                l_end = p_start - next_num_l.start()
                l_string = l_string[:l_start] + str(l_num + int(l_string[l_start:l_end])) + l_string[l_end:]
            
            return l_string + "0" + r_string, True
    return num, False

def split(num):
    match = search(r"\d{2,}", num)
    if not match:
        return num, False
    start = match.start()
    end = match.end()
    num_to_split = int(num[start:end])
    return num[:start] + pair(floor(num_to_split/2), ceil(num_to_split/2)) + num[end:], True

def reduce(num):
    while True:
        num, has_exploded = explode(num)
        if has_exploded:
            continue
        num, has_split = split(num)
        if has_split:
            continue
        return num

def calc_magnitude(num):
    if isinstance(num, int):
        return num
    return 3 * calc_magnitude(num[0]) + 2 * calc_magnitude(num[1])

def calc_a(numbers):
    num = reduce(numbers[0])
    for i in range(1, len(numbers)):
        num = pair(num, numbers[i])
        num = reduce(num)
    return calc_magnitude(literal_eval(num))

def calc_b(numbers):
    highest_magnitude = 0
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            highest_magnitude = max((
                calc_magnitude(literal_eval(reduce(pair(numbers[i], numbers[j])))), 
                calc_magnitude(literal_eval(reduce(pair(numbers[j], numbers[i])))), 
                highest_magnitude))
    return highest_magnitude