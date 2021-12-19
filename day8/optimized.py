from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[y.split() for y in x.split(" | ")] for x in indata.split("\n")]
    return indata

def calc_a(indata):
    looking_for = [1,4,7,8]
    count = 0
    for row in indata:
        nums = {}
        for num in row[0]:
            if len(num) == 2:
                nums[1] = set(num)
            elif len(num) == 3:
                nums[7] = set(num)
            elif len(num) == 4:
                nums[4] = set(num)
            elif len(num) == 7:
                nums[8] = set(num)

        for num in row[1]:
            num_set = set(num)
            for key in looking_for:
                if nums[key] == num_set:
                    count += 1
                    break
        
    return count

def calc_b(indata):
    sum = 0
    for row in indata:
        val = ""
        nums = {}
        len_five = []
        len_six = []
        for num in row[0]:
            if len(num) == 2:
                nums[1] = num
            elif len(num) == 3:
                nums[7] = num
            elif len(num) == 4:
                nums[4] = num
            elif len(num) == 7:
                nums[8] = num
            elif len(num) == 6:
                len_six.append(num)
            elif len(num) == 5:
                len_five.append(num)

        nums[6] = [x for x in len_six if nums[1][0] not in x or nums[1][1] not in x][0]
        len_six.remove(nums[6])

        nums[9] = [x for x in len_six if nums[4][0] in x and nums[4][1] in x and nums[4][2] in x and nums[4][3] in x][0]
        len_six.remove(nums[9])

        nums[0] = len_six[0]
        len_six.remove(nums[0])

        nums[3] = [x for x in len_five if nums[1][0] in x and nums[1][1] in x][0]
        len_five.remove(nums[3])

        nums[5] = [x for x in len_five if x[0] in nums[6] and x[1] in nums[6] and x[2] in nums[6] and x[3] in nums[6] and x[4] in nums[6]][0]
        len_five.remove(nums[5])

        nums[2] = len_five[0]
        len_five.remove(nums[2])

        for key in nums.keys():
            nums[key] = set(nums[key])

        for num in row[1]:
            num_set = set(num)
            for key in nums.keys():
                if nums[key] == num_set:
                    val += f"{key}"
                    break
        sum += int(val)
        
    return sum

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