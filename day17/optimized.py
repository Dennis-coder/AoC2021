def refactor_indata(indata):
    target = [[int(y) for y in x.split("=")[1].split("..")] for x in indata.split(": ")[1].split(", ")]
    return target

def calc_a(target):
    _, (bottom, top) = target
    y = abs(bottom) - 1 if top < 0 else top if top > 0 else None
    return (y*(y+1)//2)

def calc_b(target):
    (left, right), (bottom, top) = target
    lowest_x = 0
    while (lowest_x*(lowest_x+1)//2) < left:
        lowest_x += 1
    highest_x = right
    lowest_y = bottom
    highest_y = abs(bottom) - 1 if top < 0 else top if top > 0 else None
    
    x_coords = {}
    for x in range(lowest_x, highest_x+1):
        x_pos = 0
        x_vel = x
        from_steps = 0
        while x_pos < left:
            from_steps += 1
            x_pos += x_vel
            x_vel -= 1
            if x_vel == 0:
                break
        if left <= x_pos <= right:
            to_steps = from_steps
            while x_pos <= right:
                to_steps += 1
                x_pos += x_vel
                x_vel -= 1
                if x_vel <= 0:
                    to_steps = float('inf')
                    break
            if (from_steps, to_steps - 1) not in x_coords:
                x_coords[(from_steps, to_steps - 1)] = 0
            x_coords[(from_steps, to_steps - 1)] += 1

    y_coords = {}
    for y in range(lowest_y, highest_y+1):
        y_pos = 0
        y_vel = y
        from_steps = 0
        while top < y_pos:
            from_steps += 1
            y_pos += y_vel
            y_vel -= 1
        if bottom <= y_pos <= top:
            to_steps = from_steps
            while bottom <= y_pos:
                to_steps += 1
                y_pos += y_vel
                y_vel -= 1
            if (from_steps, to_steps - 1) not in y_coords:
                y_coords[(from_steps, to_steps - 1)] = 0
            y_coords[(from_steps, to_steps - 1)] += 1
        
    count = 0
    for (x1, x2), n in x_coords.items():
        for (y1, y2), m in y_coords.items():
            if x1 <= y2 and y1 <= x2:
                count += n*m
    
    return count
