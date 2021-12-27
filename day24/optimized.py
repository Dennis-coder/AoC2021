def refactor_indata(indata):
    monad = [[op.split() for op in num.splitlines()] for num in indata.split("inp ")[1:]]
    return monad

def inp(alu, x, y):
    alu[x] = y

def add(alu, x, y):
    if y in alu:
        alu[x] += alu[y]
    else:
        alu[x] += int(y)

def mul(alu, x, y):
    if y in alu:
        alu[x] *= alu[y]
    else:
        alu[x] *= int(y)

def div(alu, x, y):
    if y in alu:
        alu[x] = alu[x] // alu[y]
    else:
        alu[x] = alu[x] // int(y)

def mod(alu, x, y):
    if y in alu:
        alu[x] = alu[x] % alu[y]
    else:
        alu[x] = alu[x] % int(y)

def eql(alu, x, y):
    if y in alu:
        alu[x] = int(alu[x] == alu[y])
    else:
        alu[x] = int(alu[x] == int(y))

def reset(alu, w=0, x=0, y=0, z=0):
    alu["w"] = w
    alu["x"] = x
    alu["y"] = y
    alu["z"] = z

def calc_a(monad): 
    alu = {"w": 0, "x": 0, "y": 0, "z": 0}
    funcs = {"add": add, "mul": mul, "div": div, "mod": mod, "eql": eql}
    ops = monad[0]
    possible_outcomes = set()
    for j in range(1, 10):
        reset(alu)
        alu[ops[0][0]] = j
        for op, x, y in ops[1:]:
            funcs[op](alu, x, y)
        possible_outcomes.add((alu["w"], alu["x"], alu["y"], alu["z"], str(j)))
    
    for ops in monad[1:]:
        new_possible_outcomes = set()
        print(len(possible_outcomes))
        for j in range(1, 10):
            for *vals, prev_num in possible_outcomes:
                reset(alu, *vals)
                alu[ops[0][0]] = j
                for op, x, y in ops[1:]:
                    funcs[op](alu, x, y)
                new_possible_outcomes.add((alu["w"], alu["x"], alu["y"], alu["z"], j))
        possible_outcomes = new_possible_outcomes


def calc_b(indata):
    pass