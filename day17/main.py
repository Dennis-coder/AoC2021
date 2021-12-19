def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = [[int(y) for y in x.split("=")[1].split("..")] for x in indata.split(": ")[1].split(", ")]
    return indata

def calc_a(indata):
    y = abs(indata[1][0]) - 1 if indata[1][1] < 0 else indata[1][1] if indata[1][1] > 0 else None
    return (y*(y+1)//2)

def sim(x_vel, y_vel, target):
    x, y = 0, 0
    while x < target[0][0] or y > target[1][1]:
        x += x_vel
        y += y_vel
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
    if target[0][0] <= x and x <= target[0][1] and target[1][0] <= y and y <= target[1][1]:
        return True
    else:
        return False

def calc_b(indata):
    lowest_x = 0
    while (lowest_x*(lowest_x+1)//2) < indata[0][0]:
        lowest_x += 1
    highest_x = indata[0][1]
    lowest_y = indata[1][0]
    highest_y = abs(indata[1][0]) - 1 if indata[1][1] < 0 else indata[1][1] if indata[1][1] > 0 else None
    
    vel = []
    for x in range(lowest_x, highest_x + 1):
        for y in range(lowest_y, highest_y + 1):
            if sim(x, y, indata):
                vel.append([x,y])

    return len(vel)

def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    a = calc_a(indata)
    b = calc_b(indata)
    print(a,b)

if __name__ == "__main__":
    main()