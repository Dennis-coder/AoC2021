def refactor_indata(indata):
    indata = [[y.split() for y in x.split(" | ")] for x in indata.split("\n")]
    return indata

def calc_a(indata):
    looking_for = [1,4,7,8]
    count = 0
    for row in indata:
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