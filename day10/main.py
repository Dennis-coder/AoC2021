def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n")
    return indata

def calc_a(indata):
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

def calc_b(indata):
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
    indata = read_indata()
    indata = refactor_indata(indata)
    a = calc_a(indata)
    b = calc_b(indata)
    print(a,b)

if __name__ == "__main__":
    main()