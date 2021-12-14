from time import perf_counter

def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n")
    return indata

def calcA(indata):
    opening = {
        "(": ")", 
        "[": "]",
        "{": "}",
        "<": ">"
    }
    closing = {
        ")": "(", 
        "]": "[",
        "}": "{",
        ">": "<"
    }
    points = {
        ")": 3, 
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    score = 0
    for row in indata:
        opened = []
        for char in row:
            if char in opening:
                opened.append(char)
            elif char in closing and opened[-1] == closing[char]:
                opened.pop()
            else:
                score += points[char]
                break

    return score

def calcB(indata):
    opening = {
        "(": ")", 
        "[": "]",
        "{": "}",
        "<": ">"
    }
    closing = {
        ")": "(", 
        "]": "[",
        "}": "{",
        ">": "<"
    }
    points = {
        ")": 1, 
        "]": 2,
        "}": 3,
        ">": 4
    }
    scores = []
    for row in indata:
        opened = []
        is_corrupt = False
        for char in row:
            if char in opening:
                opened.append(char)
            elif char in closing and opened[-1] == closing[char]:
                opened.pop()
            else:
                is_corrupt = True
                break
        if is_corrupt:
            continue
        score = 0
        for char in opened[::-1]:
            score *= 5
            score += points[opening[char]]
        scores.append(score)
    scores = sorted(scores)
    return scores[len(scores)//2]

def main():
    total_start = perf_counter()
    indata = read_indata()
    refactor_start = perf_counter()
    indata = refactor_indata(indata)
    refactor_end = perf_counter()
    part1_start = perf_counter()
    a = calcA(indata)
    part1_end = perf_counter()
    part2_start = perf_counter()
    b = calcB(indata)
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