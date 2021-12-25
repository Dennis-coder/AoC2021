def refactor_indata(indata):
    navigation_subsystem = (*indata.split("\n"),)
    return navigation_subsystem

def calc_a(navigation_subsystem):
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
    for row in navigation_subsystem:
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

def calc_b(navigation_subsystem):
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
    for row in navigation_subsystem:
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